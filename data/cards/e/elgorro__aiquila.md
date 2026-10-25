# elgorro/aiquila

⭐ 39 · PHP · MIT · 推送 2026-10-24 · [GitHub](https://github.com/elgorro/aiquila) · 个人维护

**自托管 Nextcloud 的私有 AI 套件：MCP 服务、原生应用与一键部署**

由三个可独立使用的组件构成：MCP Server（342 个工具、44 类）向任意 MCP 兼容 AI 助手开放 Nextcloud 的文件、日历、任务、Talk/Deck/Mail 等数据读写；原生 Nextcloud 应用在 UI 内提供文档聊天、文本摘要改写、可复用的 Coworker 任务，并可按用户/组限制可用 provider；另有单命令 Hetzner 部署工具（含 Traefik、CrowdSec、TLS）。支持 Claude、Hetzner Inference、Mistral、DeepSeek 及本地 Ollama/LM Studio/llama.cpp 五类 provider，每会话可切换。许可为 AGPL-3.0（应用）/ MIT（MCP 服务）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP Server 提供 342 个工具覆盖文件、日历、任务、照片、笔记等 44 类操作
- 原生 Nextcloud 应用：文档聊天、摘要改写、可复用 Coworker 任务、按 Project 限定可见范围
- 五种 chat provider，含本地 Ollama/LM Studio/llama.cpp（支持 mTLS 与 bearer/basic/header 认证）
- aiquila-hetzner 单命令生产部署（Traefik、CrowdSec、TLS、可选监控）

## 适用场景

- 让 MCP 兼容的 AI 助手直接读写我的 Nextcloud 数据
- 在 Nextcloud 界面内对文档进行聊天、摘要与改写
- 数据不出自有服务器，用本地模型提供 AI 能力
- 在 Hetzner Cloud 一键部署生产级私有 AI 服务

## 场景标签

`AI 助手` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L10: AIquila brings AI to your self-hosted Nextcloud. Instead of keeping your files, notes, tasks and recipes locked ins
> L18: **Nextcloud App** — A native Nextcloud application that brings AI directly into the Nextcloud UI. Chat about your d

## 星数曲线

```mermaid
xychart-beta
    title "elgorro/aiquila 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-25 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `0fb84a90e54f` · [字段定义](../../DATASET.md)*
