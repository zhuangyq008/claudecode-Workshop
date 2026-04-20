# 韶音科技 Claude Code Workshop — Lab 详细步骤 v2

> 本文档是 Workshop 大纲的 Lab 细化版，每一步都有具体指令和预期输出。
> 核心原则：**每个 Lab 的产出 = 学员明天上班就能用的东西**

---

## Lab 1：SuperPowers 全流程实战（35min）

### 设计理念
不是"装个插件跑一下"，而是完整走一遍 **Explore → Plan → Execute → Review → Test** 的工程化工作流。学员体验到的是：用 SuperPowers 做事 vs 裸 prompt 做事，质量差距有多大。

---

### Step 0：安装（3min）

```bash
# 所有人一起做
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
/plugin list   # 确认安装成功，看到 20+ skills
```

讲师说明：
> "装完后你多了 20 多个斜杠命令。但今天我们只用核心的 5 个，走一遍完整的软件工程流程。"

---

### Step 1：Explore — 结构化头脑风暴（7min）

**任务：** 为 starter repo 中的烂代码设计重构方案

```
/brainstorm "我有一个 FastAPI 写的员工请假管理系统，代码质量很差：
- 变量名是单字母缩写（n, d, s）
- SQL 用 f-string 拼接（注入风险）
- 硬编码了 SECRET_KEY 和 AWS 密钥
- 一个 200 行的 God function
- 零测试

请从以下角度分析重构方案：
1. 安全修复优先级
2. 代码结构重组策略
3. 测试策略（单元测试 + E2E 测试）
4. 需要引入哪些工具链（lint / format / security scan）"
```

**预期体验：**
- CC 不会直接开始写代码，而是**先问你问题**（"你们用什么测试框架？""部署环境是什么？"）
- 提出 2-3 个方案，每个有 trade-off 分析
- 学员选择一个方案后才进入下一步

**讲师引导：**
> "注意这个过程。如果你直接说'帮我重构这段代码'，CC 会立刻动手，可能改错方向。用 /brainstorm 多花 3 分钟探索，能省 30 分钟返工。这就是 Harness 的第一层——引导层。"

---

### Step 2：Plan — 生成可审核的执行计划（7min）

```
/write-plan
```

**预期输出：** 一份结构化的 plan 文档，每个 task 包含：
- ⏱ 预估时间（2-5 分钟）
- 📁 涉及的文件路径
- ✅ 完成标准（verification steps）
- 🔗 依赖关系

**关键教学点 — 人工审核计划：**

讲师演示：
> "现在你是 Tech Lead。这份计划相当于一个 Junior 写的 PR description。你要审核：
> - 任务拆分合理吗？有没有遗漏？
> - 顺序对吗？应该先修安全问题还是先重构结构？
> - 每个 task 的范围控制好了吗？一个 task 改太多文件 = 风险"

**动手环节：** 每人至少修改计划中的 1 个 task（调整顺序、拆分过大 task、补充遗漏项），然后确认。

> "你刚才做的事情叫 HITL — Human In The Loop。这是 Harness Engineering 的核心：AI 出方案，人做决策。"

---

### Step 3：Execute — 按计划逐步执行（10min）

```
/execute-plan
```

**执行过程中的教学点：**

1. **观察 subagent 分派** — SuperPowers 会为每个 task 启动独立 subagent
   > "注意看，它不是一口气改完所有文件，而是每个 task 一个 subagent，互不干扰。这就是六层模型的第五层——规划与协调层。"

2. **RED-GREEN-REFACTOR 纪律** — SuperPowers 强制先写测试再写代码
   > "看它的顺序：先写一个 failing test，再写实现让 test pass，最后 refactor。这不是 CC 自己想的，是 SuperPowers 的 skill 规则强制的。"

3. **中途暂停检查（可选）** — 如果某个 task 跑偏了，可以暂停
   > "这就是 Harness 和裸 prompt 的区别——裸 prompt 跑起来你只能看着，plan 模式下你随时能踩刹车。"

---

### Step 4：Review — 代码质量评估（8min）⭐ 新增重点

**这一步是学员收获最大的环节。**

#### 4a. 用 CC 自评生成的代码

```
请对刚才重构后的代码做全面 Code Review，按以下维度打分（1-5）：

1. **安全性** — SQL 注入是否修复？密钥是否外部化？输入验证？
2. **可读性** — 命名规范？注释充分？函数长度合理？
3. **可维护性** — 单一职责？依赖注入？配置分离？
4. **测试覆盖** — 单元测试覆盖率？边界 case？异常路径？
5. **性能** — N+1 查询？不必要的全表扫描？

给出每个维度的分数和改进建议，最后给一个总分。
```

**讲师引导：**
> "让 AI 自评自己的代码，这听起来像'既当运动员又当裁判'。但实际上很有用——它能发现自己的盲点，因为评审和生成用的是不同的思维模式。"

#### 4b. 对比实验：裸 prompt vs SuperPowers

讲师提前准备好两份代码（或现场演示）：
- **A 版：** 裸 prompt "帮我重构这个 FastAPI 应用" 的输出
- **B 版：** SuperPowers 工作流的输出

用同一套评估维度打分，对比差异。

**预期结论：**
- A 版通常安全修复不完整、测试覆盖低、可能改错方向
- B 版因为有 brainstorm → plan → review 的流程约束，质量稳定且可预测

> "**工具决定下限，流程决定上限。** SuperPowers 的价值不是让 CC 更聪明，而是让输出质量从'看运气'变成'可预期'。"

---

## Lab 2 赛道 A — 开发场景深化（40min）

### 任务：从烂代码到生产级 API + E2E 测试

不再是简单的"重构代码"，而是走完一个**完整的开发交付流程**：

```
烂代码 → CLAUDE.md 规范 → 重构 → 单元测试 → E2E 测试 → CI 检查脚本
```

---

### Step 1：建立 CLAUDE.md 规范（5min）

打开 starter repo 的 `CLAUDE.md`（已有半成品），补完 TODO 部分：

```
把 CLAUDE.md 中的 TODO 部分补完：
- Git 规范：使用 Conventional Commits（feat/fix/refactor/test/docs）
- 测试要求：pytest，覆盖率 > 80%，必须覆盖异常路径
- 项目结构：service 层分离，不允许 route 里直接写业务逻辑
- 部署：Docker 容器化，环境变量注入配置
```

**教学点：**
> "CLAUDE.md 不是给人看的文档——它是给 Agent 看的操作手册。写得越精确，CC 的输出越符合你的预期。这比 prompt engineering 重要 10 倍。"

---

### Step 2：用 CLAUDE.md 驱动重构（10min）

```
按照 CLAUDE.md 中的规范，重构 dev-track/src/ 下的所有文件：
1. 先分析当前代码的问题清单
2. 按优先级排序（安全 > 结构 > 风格）
3. 逐文件重构，每个文件改完后说明做了什么
4. 最后输出一个变更摘要
```

**观察点：** CC 是否自动遵循 CLAUDE.md 中的规范（命名、测试要求、结构约定）

---

### Step 3：生成单元测试（8min）

```
为重构后的代码生成 pytest 单元测试：
- 每个 route 至少 3 个 test case（正常/异常/边界）
- 使用 fixture 管理测试数据库
- Mock 外部依赖（邮件通知等）
- 运行测试并确保全部通过
```

**动手环节：** 让学员跑 `pytest --cov` 看覆盖率报告

```bash
pytest --cov=src --cov-report=term-missing
```

> "看覆盖率数字。但更重要的是看 `MISSING` 列——那些没被测试覆盖的行，往往就是生产环境出 bug 的地方。"

---

### Step 4：生成 Playwright E2E 测试（12min）⭐ 重点新增

#### 4a. 建立应用上下文文件（3min）

```
为我们的请假管理 API 创建一个 app.context.md 文件，包含：
- 所有 API 端点列表（路径、方法、参数、响应）
- 业务规则（请假天数限制、审批流程、角色权限）
- 关键用户流程（申请→审批→查询→撤销）
- 已知的边界条件（跨年请假、余额不足、并发审批）
```

**教学点：**
> "这个 app.context.md 就是 E2E 测试的'产品需求书'。没有它，CC 只能看 DOM 结构猜测测试逻辑，写出来的测试脆弱且没有业务意义。有了它，CC 知道'审批后余额应该扣减'这种业务规则。"

#### 4b. 生成 Playwright 测试（5min）

```
基于 app.context.md，用 Playwright + pytest 生成 E2E 测试：

1. 测试场景覆盖：
   - 正常请假申请流程（提交→审批→查询状态变更）
   - 权限控制（普通员工不能审批自己的请假）
   - 边界条件（余额不足时申请应被拒绝）
   - 异常处理（无效日期、必填字段缺失）

2. 技术要求：
   - 使用 Page Object Model 组织代码
   - 用 getByRole / getByText 定位，不用 CSS selector
   - 每个测试独立，用 fixture 管理状态
   - 添加截图断言用于视觉回归（可选）

3. 输出结构：
   tests/
   ├── e2e/
   │   ├── conftest.py           # Playwright fixtures
   │   ├── pages/
   │   │   ├── login_page.py     # Page Object
   │   │   ├── leave_page.py
   │   │   └── approval_page.py
   │   ├── test_leave_flow.py    # 正常流程
   │   ├── test_permissions.py   # 权限测试
   │   └── test_edge_cases.py    # 边界条件
   └── ...
```

#### 4c. 运行并分析结果（4min）

```bash
# 运行 E2E 测试
npx playwright test --reporter=html

# 查看报告
npx playwright show-report
```

**讲师演示失败用例：**
> "看这个失败的 test——'余额不足时应该返回 400'。如果这个测试是手写的，你可能不会想到这个 case。但 CC 从 app.context.md 的业务规则自动推导出来了。这就是 AI + E2E 的价值。"

---

### Step 5：生成 CI 质量检查脚本（5min）

```
创建一个 ci-check.sh 脚本，集成以下检查：
1. ruff check（代码风格）
2. ruff format --check（格式化检查）
3. pytest --cov（单元测试 + 覆盖率门槛 80%）
4. bandit -r src/（安全扫描）
5. 任一步骤失败则脚本返回非零退出码

这个脚本可以直接集成到 Git pre-commit hook 或 CI pipeline。
```

**教学点：**
> "你刚才用 CC 5 分钟生成的这个脚本，很多团队花了几周才搭好。这不是 CC 替你写代码，是 CC 帮你建工程化体系。明天上班你就可以把这个脚本丢到你们的 repo 里。"

---

## Lab 2 赛道 B — 运维场景深化（40min）

### 任务：用 CC 构建完整的 AWS 运维工具箱

不是零散的"帮我查个东西"，而是产出一个**可复用的运维脚本集**。

---

### Step 1：安全审计实战（12min）

#### 1a. IAM Policy 审计（6min）

```
分析 ops-track/iam-policy-risky.json 这份 IAM Policy：

1. 逐条分析每个 Statement 的风险等级（高/中/低）
2. 指出具体的安全问题：
   - 过度授权（Action: * 或 Resource: *）
   - 缺少 Condition 约束（无 IP 限制、无 MFA 要求）
   - 违反最小权限原则的地方
3. 给出修复后的 Policy JSON
4. 解释修复逻辑——为什么这样改

最后生成一份安全审计报告（markdown 格式）。
```

**教学点：**
> "注意看 CC 不只告诉你'这里有风险'，还解释了为什么有风险以及怎么修。这比任何 IAM 教程都有效，因为它在分析你的真实配置。"

#### 1b. Security Group 审计（6min）

```
分析 ops-track/security-group-bad.json：

1. 标记所有 0.0.0.0/0 的入站规则
2. 按风险等级排序
3. 给出每条规则的修复建议（限制 IP 范围 / 使用 VPN / 改用 SSM）
4. 生成一个 Python 脚本，能自动扫描 AWS 账号中所有 SG 并输出类似报告

这个脚本我们要能在生产环境中使用。
```

**产出：** 一个可复用的 `sg-audit.py` 脚本 → 学员明天就能跑

---

### Step 2：排障实战（12min）

```
阅读 ops-track/troubleshoot-scenario.md 中的故障描述。

请作为一个资深 SRE，给出完整的排障流程：

1. **信息收集阶段** — 需要查看哪些 CloudWatch 指标？需要在服务器上跑哪些命令？
2. **根因分析** — 基于已知信息，最可能的根因是什么？列出排查决策树
3. **修复方案** — 短期止血 + 长期根治
4. **自动化预防** — 生成一个监控脚本：
   - 检测 CPU > 90% 持续 5 分钟
   - 检测磁盘使用率 > 85%
   - 检测内存使用率 > 90%
   - 触发时发送告警（SNS 或钉钉 Webhook）
5. **Runbook** — 生成一份 markdown 格式的 runbook，下次遇到同类故障可以按步骤操作

每一步都要给出具体的命令，不要只说"检查 CPU"，要给出 `top -bn1 | head -20` 这样的实际命令。
```

**产出：**
- `monitor.py` — 自动化监控脚本
- `runbook-ec2-performance.md` — 故障处理手册
- 这两个文件学员带走就能用

---

### Step 3：IaC 实战 + 代码评估（16min）

#### 3a. 用 CC 生成 CDK 代码（8min）

```
基于 ops-track/cdk-starter/app.py 的骨架，用 AWS CDK (Python) 实现：

1. VPC（2 个 AZ，公有/私有子网各 2 个）
2. NAT Gateway（单 AZ，节省成本）
3. Application Load Balancer
4. ECS Fargate Service（跑我们的请假管理 API）
5. RDS PostgreSQL（私有子网，Multi-AZ）
6. 所有安全组规则遵循最小权限

每写一个 Construct 前，先解释：
- 这个资源是做什么的？
- 为什么放在这个子网？
- 安全组规则的设计逻辑？

这样我不只得到代码，还学到了 AWS 架构知识。
```

**教学点：**
> "这就是目标 C——用 CC 学 AWS。你问它写 CDK，它不只给代码，还教你为什么这么写。比看文档快 10 倍，而且是针对你的具体场景。"

#### 3b. CC 自评 CDK 代码（4min）

```
对刚才生成的 CDK 代码做 Well-Architected Review，检查：

1. **安全性** — SG 规则是否最小权限？RDS 是否在私有子网？是否启用加密？
2. **可靠性** — Multi-AZ？健康检查配置？自动扩缩？
3. **成本** — NAT Gateway 数量合理吗？实例规格是否过大？
4. **运维** — CloudWatch 告警配了吗？日志输出到哪里？
5. **性能** — 子网 CIDR 够用吗？ALB 跨 AZ 了吗？

按 AWS Well-Architected 五大支柱打分（1-5），给出改进建议。
```

#### 3c. 生成 CDK 测试（4min）

```
为 CDK Stack 生成 pytest 断言测试：
- 验证 VPC 有 2 个 AZ
- 验证 RDS 在私有子网
- 验证 SG 没有 0.0.0.0/0 入站规则
- 验证 ECS Task 定义了健康检查

用 aws_cdk.assertions 模块的 Template.from_stack() 方式。
```

---

## 模块 6 Hooks Lab 补充：实操环节（融入 25min 中）

### Live Coding：现场写一个 Hook（10min）

不只是讲理论，现场带大家写一个真实的 Hook：

```
我们来写一个 PostToolUse Hook：
每次 CC 写入 .py 文件后，自动检测是否有硬编码的密钥。

要求：
1. 编辑 .claude/hooks.json，添加 PostToolUse hook
2. hook 调用 hooks-lab/secrets-detect.sh
3. 如果检测到密钥，返回警告信息到 CC 上下文
4. CC 收到警告后应该自动修复（用环境变量替换硬编码）

我们现场测试这个 Hook 的效果。
```

**演示步骤：**
1. 配置 hook → 2. 故意让 CC 写一段含密钥的代码 → 3. 看 hook 自动拦截 → 4. CC 自动修复

> "看到了吗？这个修复循环是自动的——hook 发现问题 → 反馈给 CC → CC 修复 → hook 再检查。这就是 PostToolUse 的自我修复循环，不需要人工干预。"

---

## 总结：每个 Lab 的可带走产出

| Lab | 产出物 | 工作中的用途 |
|---|---|---|
| Lab 1 | 重构方案 + 代码评估报告 | SuperPowers 工作流可用于任何新项目 |
| Lab 2A-1 | CLAUDE.md 团队规范 | 直接放到项目 repo，统一团队 CC 使用标准 |
| Lab 2A-2 | 单元测试 + E2E 测试 | pytest + Playwright 测试套件可直接集成 CI |
| Lab 2A-3 | ci-check.sh | pre-commit hook 或 CI pipeline 质量门禁 |
| Lab 2B-1 | sg-audit.py + 安全报告 | 定期扫描 AWS 账号安全配置 |
| Lab 2B-2 | monitor.py + runbook | 生产环境监控 + 故障处理手册 |
| Lab 2B-3 | CDK Stack + 测试 | IaC 模板可复用到新项目 |
| 模块 6 | hooks.json + 脚本 | 团队级自动化质量护栏 |

> **核心理念：Workshop 不是演示，是生产。每个人带走的不是笔记，是代码。**
