#!/bin/bash
# block-dangerous-commands.sh
# PreToolUse hook: 拦截危险命令
# 从 stdin 读取 JSON，检查命令是否包含危险操作

input=$(cat)
tool_name=$(echo "$input" | grep -o '"tool_name"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"tool_name"[[:space:]]*:[[:space:]]*"//;s/"//')

# 只检查 Bash/Shell 类工具
if [[ "$tool_name" != *"Bash"* && "$tool_name" != *"bash"* && "$tool_name" != *"shell"* ]]; then
    exit 0
fi

command_text=$(echo "$input" | grep -o '"command"[[:space:]]*:[[:space:]]*"[^"]*"' | head -1 | sed 's/.*"command"[[:space:]]*:[[:space:]]*"//;s/"//')

# 危险命令列表
dangerous_patterns=(
    "rm -rf /"
    "rm -rf /*"
    "DROP TABLE"
    "DROP DATABASE"
    "DELETE FROM"
    "TRUNCATE TABLE"
    "mkfs"
    "> /dev/sda"
    "dd if=/dev/zero"
    "chmod -R 777 /"
    ":(){ :|:& };:"
)

for pattern in "${dangerous_patterns[@]}"; do
    if echo "$command_text" | grep -qi "$pattern"; then
        echo "🚫 危险命令被拦截: 检测到 '$pattern'" >&2
        exit 2
    fi
done

exit 0
