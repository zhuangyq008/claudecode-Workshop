# 韶音科技（Shokz）团队知识库

## 业务术语

| 术语 | 英文 | 说明 |
|------|------|------|
| 骨传导 | Bone Conduction | 公司核心技术，通过颧骨传导声音 |
| OWS | Open-ear Wireless Stereo | 开放式无线立体声，新品类方向 |
| SKU | Stock Keeping Unit | 产品库存单位 |
| BOM | Bill of Materials | 物料清单 |
| OTA | Over-The-Air | 固件空中升级 |
| NPI | New Product Introduction | 新品导入流程 |
| DFM | Design for Manufacturing | 面向制造的设计 |

## 数据字典

### 员工表（employees）
- `employee_id`: 工号，格式 `SZ-{部门缩写}-{4位数字}`，如 `SZ-ENG-0042`
- `name`: 中文姓名
- `english_name`: 英文名
- `department`: 部门代码（ENG/PRD/MKT/SAL/OPS/HR/FIN）
- `level`: 职级（P1-P10, M1-M5）
- `hire_date`: 入职日期
- `manager_id`: 直属上级工号

### 请假表（leave_requests）
- `leave_id`: 请假单号，格式 `LV-{YYYYMMDD}-{4位序号}`
- `employee_id`: 工号
- `leave_type`: 假期类型（annual/sick/personal/maternity/paternity/compensatory）
- `start_date`: 开始日期
- `end_date`: 结束日期
- `status`: 状态（pending/approved/rejected/cancelled）
- `approver_id`: 审批人工号

### 部门代码

| 代码 | 部门 | 负责人 |
|------|------|--------|
| ENG | 工程部 | 张伟 |
| PRD | 产品部 | 李娜 |
| MKT | 市场部 | 王芳 |
| SAL | 销售部 | 刘强 |
| OPS | 运维部 | 陈明 |
| HR | 人力资源部 | 赵丽 |
| FIN | 财务部 | 周杰 |

## 技术栈

- 后端：Python (FastAPI) + Java (Spring Boot)
- 前端：React + TypeScript
- 数据库：PostgreSQL (RDS)
- 缓存：Redis (ElastiCache)
- 消息队列：SQS
- 基础设施：AWS CDK
- CI/CD：GitHub Actions → ECR → ECS Fargate
- 监控：CloudWatch + Grafana

## 编码规范摘要

- Python 代码用 `ruff` 格式化
- 分支命名：`feature/{ticket-id}-{简短描述}`
- Commit 格式：`{type}({scope}): {description}`，如 `fix(leave): 修复请假天数计算错误`
- PR 必须有至少 1 个 approve
- 合并用 squash merge
