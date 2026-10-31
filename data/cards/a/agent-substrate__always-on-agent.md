# agent-substrate/always-on-agent

⭐ 27 · TypeScript · Apache-2.0 · 推送 2026-09-25 · [GitHub](https://github.com/agent-substrate/always-on-agent) · [官网](https://www.youtube.com/watch?v=D5a9tyPkaPY) · 组织维护

**在 GKE 上以可挂起 actor 形式运行常驻消息 agent 的参考实现**

基于 Agent Substrate 的 OpenClaw 部署方案：将在线表现（presence）与计算（cognition）分离——常驻多租户网关持有 WhatsApp 等渠道连接，每个会话作为可挂起的 Substrate actor 运行，会话空闲即检查点挂起以回收算力，下一条消息到达时自动恢复（实测 resume P50 为 3.4s）。以 OpenClaw 插件形式提供（extensions/substrate/，不改核心文件），配合 K8s manifests 与镜像构建脚本部署到 GKE。面向 agent 框架公司与基础设施工程师。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- presence/cognition 分离：网关常驻、agent 以可挂起 actor 运行
- OpenClaw 插件形式接入，不修改任何 OpenClaw 核心文件
- 提供 K8s manifests（WorkerPool/ActorTemplate/gateway）与 WhatsApp demo 部署脚本
- 在原生 Substrate 上运行，仅需调整 atenet-router 的 route-timeout 等参数

## 适用场景

- 让 24/7 在线的 WhatsApp 等 agent 在空闲时挂起以节省算力成本
- 在 GKE 上以多租户网关托管多个常驻 OpenClaw 实例
- agent 框架公司评估 checkpoint-restore 式部署架构

## 场景标签

 · 领域:AI 基础设施/云原生

## 证据(README 行号)

> L6: from cognition**: an always-on gateway holds the channel connections, while the
> L7: expensive agent runs as a suspendable Substrate actor. The gateway suspends it

## 星数曲线

```mermaid
xychart-beta
    title "agent-substrate/always-on-agent 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28", "2026-10-31"]
    y-axis "stars" 23 --> 28
    line [24, 25, 27, 27]
```

2026-10-18 24 → 2026-10-31 27（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bcb5c28d1eb5` · [字段定义](../../DATASET.md)*
