# mr-tbot/mesh-api

⭐ 183 · Python · GPL-3.0 · 推送 2026-07-28 · [GitHub](https://github.com/mr-tbot/mesh-api) · [官网](https://mesh-api.dev) · 个人维护

**LoRa 网格网络的 AI/API 路由桥，连接 Meshtastic 与 MeshCore**

单人开发的实验性项目：将 Meshtastic 与 MeshCore LoRa 网格网络同 AI 聊天服务与第三方 API 打通。定位为协议桥与网格骨干，可在两个网格网络间跨网路由消息，内置 30 个插件式扩展（通信、应急、智能家居、Ham Radio 等 7 类），支持 LM Studio、Ollama、OpenAI、Claude 等多种 AI 供应方，内置 MCP 服务器供外部 AI agent 调用，提供 REST API、WebUI 仪表盘与交互式节点地图。README 多处声明功能未经充分实测，不建议用于关键任务或紧急场景。可通过 pip 或 Docker 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 同时支持 Meshtastic 与 MeshCore，可跨网格网络路由消息
- 30 个内置插件式扩展，文件夹即插即用
- 支持 LM Studio/Ollama 本地模型及 OpenAI/Claude/Gemini 等多种 AI 供应方
- 内置 MCP 服务器（POST /mcp），外部 AI agent 可驱动网格功能

## 适用场景

- 离网环境下让 LoRa 网格用户通过短信式命令访问 AI 问答
- 将网格消息桥接到 Discord、Home Assistant 或 n8n 自动化流程
- 应急告警经 Twilio 短信/邮件/Discord 发送含 GPS 坐标的通知
- 通过 WebUI 仪表盘管理节点地图与消息收发

## 场景标签

`聊天机器人` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L48: - **Full Router / Mesh Operator**
> L92:  - Support for **Local** models (LM Studio, Ollama), **OpenAI**, **Claude**, **Gemini**, **Grok**, **OpenRouter**, 
> L82:  - Exposes MESH-API core functions **and** extensions as MCP **tools** at `POST /mcp`, so external AI agents (Claud

## 星数曲线

```mermaid
xychart-beta
    title "mr-tbot/mesh-api 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 179 --> 183
    line [180, 182, 182]
```

2026-10-18 180 → 2026-10-24 182（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `35f119970001` · [字段定义](../../DATASET.md)*
