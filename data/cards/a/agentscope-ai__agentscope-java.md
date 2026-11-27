# agentscope-ai/agentscope-java

⭐ 6,492 · Java · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/agentscope-ai/agentscope-java) · [官网](https://java.agentscope.io/) · 组织维护 · 中文 README

**Java 分布式生产级 Agent 构建框架**

AgentScope Java 2.0 是一个以 Maven 中央仓库发布的 Java 框架，用于构建分布式、可长期运行的 Agent。核心机制包括：32 类类型化事件流、工具调用三级权限门控（allow/approve/deny）、AOP 式 Middleware、本地/Docker/Kubernetes/E2B 沙箱工作区、子 Agent 编排（agent_spawn/agent_send），以及基于 Redis/MySQL/PostgreSQL 等的分布式会话与内存管理和跨副本会话恢复。要求 JDK 17+，模型提供方以独立扩展模块引入。许可为 Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 32 类类型化事件流支持实时前端渲染与 HITL
- 工具调用权限门控：allow / require approval / deny
- 分布式会话与状态存储（Redis/MySQL/PostgreSQL/OSS/COS）与跨副本恢复
- 沙箱隔离执行：本地/Docker/Kubernetes/E2B 云沙箱

## 适用场景

- 在 Java 企业技术栈中构建长期运行的 Agent 应用
- 需要多租户隔离与滚动重启下会话恢复的分布式 Agent 部署
- 对敏感工具调用要求人工审批的受控执行场景

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L48: AgentScope Java 2.0 is a production-ready framework for building distributed, enterprise-grade agents, providing es
> L82: > AgentScope Java requires **JDK 17** or higher.

## 星数曲线

```mermaid
xychart-beta
    title "agentscope-ai/agentscope-java 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 6063 --> 6531
    line [6102, 6109, 6126, 6138, 6161, 6181, 6198, 6202, 6205, 6102, 6294, 6320, 6334, 6351, 6364, 6367, 6374, 6386, 6401, 6411, 6423, 6437, 6444, 6449, 6461, 6477, 6492]
```

2026-10-25 6,102 → 2026-11-27 6,492（+390）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7b230e70f7b8` · [字段定义](../../DATASET.md)*
