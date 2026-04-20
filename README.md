# 🎧 韶音科技 Claude Code Workshop — Lab 实战

## 环境准备

1. 确保已安装 Claude Code（`claude` 命令可用）
2. 进入本目录：`cd workshop-lab`
3. Claude Code 会自动读取 `CLAUDE.md` 作为项目规范

## Lab 结构

| 目录 | 内容 | 适合 |
|------|------|------|
| `dev-track/` | 赛道 A：一个写得很烂的 FastAPI 请假管理系统 | 开发同学 |
| `ops-track/` | 赛道 B：有风险的 IAM/SG + EC2 排障 + CDK 骨架 | 运维/DevOps 同学 |
| `hooks-lab/` | 模块 6：Hooks 实战脚本和示例 | 全员 |

## 快速开始

### Lab 1: SuperPowers 三步链（全员）

打开 `cheatsheet.md`，按顺序把三个 prompt 复制到 Claude Code 里执行。

### Lab 2: 选择赛道

- **赛道 A（开发）**：`cd dev-track && cat README.md`
- **赛道 B（运维）**：`cd ops-track && cat README.md`

### Lab 3: Hooks（模块 6）

进入 `hooks-lab/` 目录，按 README 指引配置 hooks。

## 注意事项

- 代码中的密钥都是 **假的**，专门用于演示安全风险
- 不要把这些代码部署到任何真实环境
- Workshop 结束后可以删除本目录
