# MatrixCoreX/RustClaw

⭐ 27 · Rust · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/MatrixCoreX/RustClaw) · [官网](https://rustclaw.matrixai.one/) · 组织维护 · 中文 README

**树莓派/Ubuntu/macOS 可自托管的 Rust AI agent 平台**

以 Rust 编写的自托管 AI agent 平台，通过浏览器控制台或绑定的消息渠道提问、处理文件并跟踪任务执行。核心机制：经 MCP 接入本地 stdio 或远程 HTTP 工具服务器，将文档导入 RAG 知识库并支持引用来源；clawd 服务负责任务运行时与 HTTP API，skill-runner 提供技能分发。支持 Telegram/微信/飞书/WhatsApp 等多渠道入口、任务检查点恢复、Bubblewrap/Seatbelt 进程隔离与加密备份等运维保护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 工具接入：本地 stdio 与远程 Streamable HTTP 服务器均可连接
- RAG 知识库：导入手册/FAQ/runbook，回答可引用来源
- 多渠道入口：Telegram、微信、飞书/Lark、WhatsApp 及浏览器 UI
- 任务检查点与恢复机制，支持长任务续跑

## 适用场景

- 在树莓派上自托管个人 AI 助手
- 把产品手册导入知识库让 agent 回答政策类问题并引用出处
- 通过微信/Telegram 等消息应用远程调用 agent 任务
- 用 MCP 接入自有工具让 agent 查询订单等实时信息

## 场景标签

`AI 助手` `RAG` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Agent Runtime is a self-hosted AI agent platform written in Rust for Raspberry Pi, Ubuntu, and macOS. Use the web co
> L5: Connect external tools through the Model Context Protocol (MCP) and import your own documents into a retrieval-augme

## 星数曲线

```mermaid
xychart-beta
    title "MatrixCoreX/RustClaw 星数(近 3 点)"
    x-axis ["2026-11-25", "2026-11-27", "2026-11-28"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-11-25 26 → 2026-11-28 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `9956318bdded` · [字段定义](../../DATASET.md)*
