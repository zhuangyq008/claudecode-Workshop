# EC2 排障场景：生产环境复合故障

## 背景

2026-04-20 周一早上 9:00，运维群收到告警：生产环境的订单处理服务（`i-0abc123def456`）响应超时。

## 告警信息

```
[CRITICAL] CloudWatch Alarm: shokz-order-service-cpu
  Instance: i-0abc123def456 (c5.2xlarge)
  Region: cn-northwest-1
  CPU Utilization: 98.7% (阈值: 80%)
  持续时间: 45 分钟

[WARNING] CloudWatch Alarm: shokz-order-service-disk
  Instance: i-0abc123def456
  Disk Usage /: 94.2% (阈值: 85%)
  Disk Usage /data: 97.8% (阈值: 85%)

[WARNING] 应用日志异常
  Java heap space OOM 错误: 过去 1 小时出现 237 次
  GC pause 时间: 平均 3.2s（正常 < 200ms）
```

## 已知信息

- **实例类型**: c5.2xlarge（8 vCPU, 16 GB RAM）
- **操作系统**: Amazon Linux 2023
- **应用**: Java Spring Boot 订单处理服务
- **JVM 参数**: `-Xmx4g -Xms2g`（总共 16G 内存只分了 4G）
- **数据库**: RDS PostgreSQL（连接池大小: 200）
- **最近变更**: 上周五部署了新版本 v2.3.1，增加了批量导出功能
- **EBS 卷**: 100GB gp2（/dev/xvda），200GB gp2（/data）

## 症状汇总

1. **CPU 100%**: `top` 显示 Java 进程占用 780% CPU（8核）
2. **磁盘快满**: `/data` 分区 97.8%，日志文件疯长
3. **内存泄漏**: Java heap 持续增长，Full GC 频繁但回收不了
4. **连接池耗尽**: 数据库连接池 200/200，新请求排队
5. **响应超时**: API P99 延迟从 200ms 飙升到 30s

## 你的任务

请用 Claude Code 帮你：

1. **分析根因**：梳理这些症状之间的因果关系
2. **制定紧急处置方案**：按优先级列出恢复步骤
3. **生成排查命令**：给出在 EC2 上执行的具体命令
4. **写复盘报告模板**：包含时间线、根因、修复措施、防范建议
5. **生成监控告警优化建议**：现有告警太晚了，怎么提前发现？

## 提示

```
请分析这个 EC2 故障场景（troubleshoot-scenario.md），给出：
1. 根因分析（画出因果链）
2. 紧急恢复的具体步骤和命令
3. 长期修复建议
4. 监控告警的优化方案
```
