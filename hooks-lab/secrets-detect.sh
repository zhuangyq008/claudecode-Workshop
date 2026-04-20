#!/bin/bash
# secrets-detect.sh
# 检测代码中的硬编码密钥

input=$(cat)

file_path=$(echo "$input" | grep -o '"file_path"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"file_path"[[:space:]]*:[[:space:]]*"//;s/"//')

if [[ -z "$file_path" || ! -f "$file_path" ]]; then
    exit 0
fi

# 常见密钥模式
patterns=(
    'AKIA[0-9A-Z]{16}'                          # AWS Access Key
    '["\x27]sk-[a-zA-Z0-9-]{20,}["\x27]'        # Secret Key 模式
    'password\s*=\s*["\x27][^"\x27]{3,}["\x27]'  # 硬编码密码
    'secret\s*=\s*["\x27][^"\x27]{3,}["\x27]'    # 硬编码 secret
    'token\s*=\s*["\x27][^"\x27]{3,}["\x27]'     # 硬编码 token
    'DB_PASSWORD\s*=\s*["\x27]'                   # 数据库密码
    'AWS_SECRET_KEY\s*=\s*["\x27]'                # AWS Secret Key
)

found=0
for pattern in "${patterns[@]}"; do
    matches=$(grep -nEi "$pattern" "$file_path" 2>/dev/null)
    if [[ -n "$matches" ]]; then
        if [[ $found -eq 0 ]]; then
            echo "🔑 检测到硬编码密钥！文件: $file_path" >&2
            found=1
        fi
        echo "$matches" >&2
    fi
done

if [[ $found -eq 1 ]]; then
    echo "⚠️ 请使用环境变量或 Secrets Manager 替代硬编码密钥" >&2
    exit 2
fi

exit 0
