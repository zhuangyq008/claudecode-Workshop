#!/bin/bash
# auto-lint.sh
# PostToolUse hook: 对修改的 .py 文件自动执行 lint

input=$(cat)

# 提取文件路径
file_path=$(echo "$input" | grep -o '"file_path"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"file_path"[[:space:]]*:[[:space:]]*"//;s/"//')

# 只处理 Python 文件
if [[ "$file_path" != *.py ]]; then
    exit 0
fi

# 检查文件是否存在
if [[ ! -f "$file_path" ]]; then
    exit 0
fi

# 尝试用 ruff 检查
if command -v ruff &> /dev/null; then
    echo "🔍 自动 lint: $file_path"
    ruff check "$file_path" 2>&1
    lint_exit=$?
    if [[ $lint_exit -ne 0 ]]; then
        echo "⚠️ Lint 发现问题，请修复后再继续" >&2
    else
        echo "✅ Lint 通过"
    fi
# 尝试用 flake8
elif command -v flake8 &> /dev/null; then
    echo "🔍 自动 lint (flake8): $file_path"
    flake8 "$file_path" 2>&1
else
    echo "ℹ️ 未安装 ruff 或 flake8，跳过 lint"
fi

exit 0
