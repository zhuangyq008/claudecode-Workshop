# CLAUDE.md — 团队编码规范

## 技术栈

- **后端**: Python 3.11+, FastAPI, SQLAlchemy, Pydantic
- **基础设施**: AWS CDK (Python), CloudFormation
- **数据库**: PostgreSQL 15
- **容器**: Docker, ECS Fargate
- **CI/CD**: GitHub Actions

## 代码风格

- 使用 `ruff` 做 linting 和 formatting（配置见 `pyproject.toml`）
- 变量名使用有意义的英文命名，禁止单字母变量（循环索引除外）
- 函数不超过 50 行；超过时拆分
- 所有公开函数必须有 docstring（Google 风格）
- Type hints 必须写

## 安全红线 🚨

- **禁止**在代码中硬编码任何密钥、密码、Token
- 敏感配置一律用环境变量 + AWS Secrets Manager
- SQL 必须用参数化查询，**禁止字符串拼接**
- API 必须有认证中间件
- IAM Policy 遵循最小权限原则
- Security Group 禁止对公网开放数据库端口

## Git 规范

<!-- TODO: 请补充以下内容 -->
<!-- 
- commit message 格式是什么？（比如 conventional commits）
- 分支命名规范？
- PR 合并策略？squash? rebase?
- 谁来 review？几个 approve 才能合？
-->

## 测试要求

<!-- TODO: 请补充以下内容 -->
<!--
- 最低覆盖率要求？
- 单元测试框架用什么？pytest? unittest?
- 需要写集成测试吗？
- CI 里跑哪些测试？
-->

## 项目结构

<!-- TODO: 请补充标准项目目录结构 -->

## 部署流程

<!-- TODO: 请补充从代码提交到上线的完整流程 -->
