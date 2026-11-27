# Cotal-AI/Cotal

⭐ 412 · TypeScript · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/Cotal-AI/Cotal) · [官网](https://cotal.ai) · 组织维护

**连接多应用多机器 AI agent 的消息与编排协调工具**

Cotal 是一个开源的 agent 协调与编排工具：通过身份、消息、presence 与端点控制的开放标准，让分散在不同应用和机器上的 AI agent 在共享空间中发现同伴、收发消息、请求协助或调用服务。支持多播/单播/任意播三种消息寻址、持久化收件箱、团队清单权限与 Cotal Lang 工作流编排。TypeScript 实现，基于 NATS + JetStream，提供 CLI、应用连接器、进程管理器与观察工具。可通过 Cotal Cloud 托管或本地自托管。

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

- 三种消息寻址模式：channel 多播、点对点单播、按角色任意播
- 基于 NATS + JetStream 的持久化消息与心跳/Presence 机制
- Cotal Lang JavaScript 子集编排多 agent 工作流，支持暂停、分支与断点恢复
- 提供 CLI 控制台、浏览器只读 dashboard 与 Linear 等服务集成接口

## 适用场景

- 让 Claude Code、OpenCode、Codex 等 agent 跨应用跨机器交接工作
- 搭建 supervisor-worker 或带人工审批节点的多 agent 团队
- 在终端实时查看 agent 团队状态、频道消息与拓扑
- 以工作流脚本编排 planner/builder 等多 agent 协作流程

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L35: Cotal lets AI agents and software services work together in a shared space, across
> L43: The open standard defines identity, messaging, presence and endpoint control. The
> L44: TypeScript implementation runs on NATS + JetStream and includes the

## 星数曲线

```mermaid
xychart-beta
    title "Cotal-AI/Cotal 星数(近 24 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 342 --> 418
    line [348, 359, 360, 362, 365, 369, 373, 374, 375, 348, 384, 387, 389, 392, 393, 394, 397, 401, 403, 405, 407, 409, 412, 412]
```

2026-10-25 348 → 2026-11-27 412（+64）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `88d091a1dd08` · [字段定义](../../DATASET.md)*
