# avifenesh/glide-mq

⭐ 95 · TypeScript · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/avifenesh/glide-mq) · [官网](https://www.glidemq.dev) · 个人维护

**面向 Node.js 的高性能消息队列，内置 LLM/Agent 编排原语**

基于 Valkey/Redis Streams 的 Node.js 任务队列，核心由 Rust NAPI 绑定（valkey-glide）实现，通过持久化 Valkey Function 在单次 FCALL 中完成当前任务并取下一任务（每任务 1 RTT），键带 hash-tag 实现零配置集群。除常规队列能力（工作流 DAG、调度、重试、限流、广播、批处理、去重、OpenTelemetry、内存测试）外，内置七种 AI 原语：成本追踪、token 流式输出、人工审批挂起/恢复、模型 fallback 链、TPM 限流、预算上限与用量汇总，并支持基于 Valkey Search 的向量检索。生产环境需 Valkey 7.0+ 或 Redis 7.0+，提供至少一次投递语义。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单次 FCALL 完成任务并取下一任务（1 RTT）
- Rust NAPI 绑定客户端，无 JS 协议解析
- 七种 AI 编排原语（成本/流式/挂起恢复/fallback/TPM/预算/用量汇总）
- FlowProducer 工作流：父子树、DAG、fan-in/fan-out、step jobs

## 适用场景

- Node.js 服务处理后台任务、定时任务与分布式工作流
- LLM 流水线中做成本追踪、token 限流与预算控制
- 需要人工审批环节的 agent 工作流（挂起/恢复）
- Valkey/Redis 集群上运行免配置的高吞吐队列

## 场景标签

`工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: High-performance message queue for Node.js with first-class AI orchestration. Built on Valkey/Redis Streams with a R
> L40: - **LLM pipelines and model orchestration** - cost tracking, token streaming, model failover, budget caps without e
> L54: ## AI-native primitives

## 星数曲线

```mermaid
xychart-beta
    title "avifenesh/glide-mq 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 92 --> 96
    line [93, 95, 95]
```

2026-10-18 93 → 2026-10-31 95（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9d002bc6201c` · [字段定义](../../DATASET.md)*
