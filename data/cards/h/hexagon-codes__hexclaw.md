# hexagon-codes/hexclaw

⭐ 31 · Go · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/hexagon-codes/hexclaw) · [官网](https://hexclaw.net) · 组织维护 · 中文 README

**可自托管 Go AI Agent 服务：对话接工具、知识库与自动化**

用 Go 编写的 Agent 服务，可独立运行或作为桌面客户端的本地 Sidecar / 云端后端。集成多模型接入（DeepSeek、OpenAI、Anthropic、通义千问、Gemini、Ollama、OpenAI 兼容服务）、ReAct 工具循环、MCP 与 Markdown 技能扩展、RAG 知识库（全文与向量混合检索）、长期记忆，以及 Cron/Webhook/工作流自动化；通过 HTTP API、桌面客户端和飞书、钉钉、Telegram 等十余种消息渠道使用。内置小学 K12 辅导场景（作业批改、错题复习、学情档案）。以 Apache 2.0 许可发布，提供二进制、Go 安装、Docker Compose 与桌面安装包。README 声明描述 v0.5.1 源码能力，Desktop 当前固定 v0.5.0 后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 Provider 接入并按文本/视觉/推理/Embedding 用途路由模型
- ReAct Agent 运行时 + MCP Server、Markdown 技能与插件/场景包扩展
- 全文与向量混合检索的 RAG 知识库，支持异步任务与恢复
- 飞书、钉钉、Telegram、Discord 等多平台 IM 接入与 Cron/Webhook 自动化

## 适用场景

- 自托管一个可通过 IM 和桌面客户端使用的个人 AI Agent
- 让对话连接工具执行代码、处理文件并自动投递结果
- 搭建带知识库与长期记忆的自动化任务服务（定时任务/Webhook）
- 家长通过桌面或钉钉发图完成小学作业批改与错题复习

## 场景标签

`聊天机器人` `RAG` `工作流自动化` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: HexClaw 是用 Go 编写的 Agent 服务，可独立运行，也可作为 HexClaw Desktop 的本地 Sidecar 或云端后端。它把模型调用、工具执行、知识检索、长期记忆和定时任务集成到同一服务中，通过桌面客户端、
> L136: |多模型接入|接入 DeepSeek、OpenAI、Anthropic、通义千问、Gemini、Ollama 和 OpenAI 兼容服务；按文本、视觉、推理、Embedding 等用途选择模型|
> L148: - **消息渠道**：飞书、钉钉、Telegram、Discord、Slack、企业微信、微信公众号、WhatsApp、LINE、Matrix、Email。

## 星数曲线

```mermaid
xychart-beta
    title "hexagon-codes/hexclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b421b5625fbc` · [字段定义](../../DATASET.md)*
