# 🅱️ 赛道 B：运维/DevOps 场景

## 背景

你是韶音科技的 DevOps 工程师，需要处理以下安全和运维问题。

## 任务一：IAM Policy 审查（15 分钟）

文件：`iam-policy-risky.json`

1. 让 Claude Code 审查这个 IAM Policy
2. 找出所有违反最小权限原则的地方
3. 生成修复后的版本（按实际业务需求收窄权限）

```
请审查 iam-policy-risky.json，找出所有安全风险，并生成一个遵循最小权限原则的修复版本。假设这个角色只需要：读写特定 S3 bucket、管理特定 EC2 实例、只读 CloudWatch。
```

## 任务二：Security Group 修复（10 分钟）

文件：`security-group-bad.json`

1. 让 Claude Code 分析这个 Security Group 的风险
2. 生成修复后的版本

```
请审查 security-group-bad.json，列出所有安全风险，并生成修复版本。要求：SSH 只允许公司 VPN（10.100.0.0/16），关闭 RDP，MySQL 只允许应用子网（10.0.2.0/24）。
```

## 任务三：EC2 排障（20 分钟）

文件：`troubleshoot-scenario.md`

1. 阅读故障场景
2. 让 Claude Code 帮你分析根因、生成排查命令、写复盘报告

## 任务四：CDK 基础设施（20 分钟）

目录：`cdk-starter/`

1. 让 Claude Code 把空壳 Stack 补全为完整的 VPC 架构
2. 要求包含 VPC、子网、NAT Gateway、Flow Logs

```
请补全 cdk-starter/app.py 中的 ShokzVpcStack，按照注释中描述的目标架构实现完整的 VPC 基础设施。
```
