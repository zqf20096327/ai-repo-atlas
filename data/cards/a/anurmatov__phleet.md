# anurmatov/phleet

⭐ 21 · C# · MIT · 推送 2026-10-30 · [GitHub](https://github.com/anurmatov/phleet) · 个人维护

**自托管多 agent 平台：Docker 化 agent 由 Claude/Codex 驱动，Temporal 编排，Telegram 协调**

基于 .NET 10 的开源自托管多 agent 平台。agent 以 Docker 容器运行于用户主机，使用用户自己的 Claude 或 Codex 凭证，通过自有 GitHub App 访问仓库；控制面、运行时状态与记忆留存于用户基础设施。中央编排器由 Temporal 工作流支撑，RabbitMQ 中继消息，Qdrant 提供共享语义记忆，Telegram 作为人机交互入口。设置后先有一个 co-CTO agent，通过 Telegram 对话创建/管理其余 agent。要求 Docker、约 8 GB 内存与 20 GB 磁盘、两个 Telegram bot 与 GitHub App；macOS(Apple silicon) 端到端测试，Linux/Windows 未验证。支持本地模型（Ollama 等）与 Gemini CLI 作为 provider。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 以 Docker 容器运行，复用用户自有 Claude/Codex 凭证与 GitHub App
- Temporal 工作流编排多步骤多 agent 任务，含共识评审流程
- co-CTO agent 通过 Telegram 对话创建、供给与停用其他 agent
- Qdrant + 嵌入的共享 fleet 记忆，跨会话可检索

## 适用场景

- 在自有基础设施上运行由 Telegram 协调的自主 agent 集群
- 通过对话让 co-CTO 扩展和管理 agent 团队
- 用多 agent 共识评审走完从需求到合并 PR 的流程

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Phleet is an open-source, self-hosted multi-agent AI platform built on .NET 10, coordinated by a central orchestrato
> L118: - `fleet-orchestrator` — agent registry + lifecycle manager

## 星数曲线

```mermaid
xychart-beta
    title "anurmatov/phleet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `558775e2349f` · [字段定义](../../DATASET.md)*
