# 🅰️ 赛道 A：开发场景 — 请假管理系统重构

## 背景

你接手了一个"前同事"写的员工请假管理系统 API。代码能跑，但质量堪忧。

## 你的任务

用 Claude Code 帮你完成以下重构：

### P0 — 安全修复（必做）
1. **找出并修复所有硬编码密钥**（`config.py`, `routes.py`）
2. **修复 SQL 注入漏洞**（`routes.py` 里的 f-string SQL）
3. **添加 API 认证中间件**

### P1 — 代码质量（必做）
4. **修复 `models.py` 的变量命名**（`n`, `d`, `s` → 有意义的名称）
5. **拆分 `utils.py` 的 God function**（`process_leave_request` 太长了）
6. **消除重复的日期处理函数**（`fmt_date`, `format_date`, `convert_date`）

### P2 — 工程规范（选做）
7. 添加 type hints 和 docstring
8. 编写单元测试
9. 添加错误处理和日志

## 如何开始

```bash
cd dev-track/src
# 先让 Claude Code 了解代码
# 然后按 cheatsheet.md 的三步链执行
```

## 提示

- 先让 Claude Code 做全面分析，不要急着改
- 安全问题优先级最高
- 重构时保持 API 接口不变
