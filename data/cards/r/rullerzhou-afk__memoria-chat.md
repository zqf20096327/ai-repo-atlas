# rullerzhou-afk/memoria-chat

⭐ 46 · JavaScript · MIT · 推送 2026-07-14 · [GitHub](https://github.com/rullerzhou-afk/memoria-chat) · 个人维护 · 中文 README

**自托管 AI 聊天客户端：跨模型持久化结构化记忆与人设定制**

面向个人用户的自托管 AI 聊天客户端，核心是跨模型切换仍保留的三层结构化记忆（身份/偏好/事件）：对话后自动提取与更新事实、按重要度在 token 预算内智能注入、支持记忆晋升/衰减生命周期与反思提炼。聊天功能覆盖 OpenAI/火山引擎/OpenRouter 三家提供商、语音对话（多种 STT/TTS 选项，含本地 Whisper）、PDF/Word 文件读取、ChatGPT 数据导入融合与人设版本管理。Node.js 后端 + 无框架前端，文件系统 JSON 存储，无构建步骤、无数据库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层结构化记忆（身份/偏好/事件）跨模型持久化，对话后自动学习
- 记忆重要度评分与 token 预算内智能注入，支持晋升/降级/衰减生命周期
- 人设（Persona）版本快照与回滚，指令优先级规则明确
- ChatGPT 导出数据导入并与现有记忆融合

## 适用场景

- 切换 AI 模型或平台后仍保留关于我的记忆
- 导入 ChatGPT 历史对话到自托管环境继续使用
- 通过语音与 AI 对话并自动沉淀记忆
- 长期维护一个了解自己偏好与近况的个人 AI

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L9: Memoria is a self-hosted AI chat client with **persistent, structured memory**. Your AI remembers who you are across
> L59: Memoria's memory system has three tiers, automatically maintained through conversations:
> L86: - **Three providers, one interface** — OpenAI, Volcengine, OpenRouter; auto-routed by model ID

## 星数曲线

```mermaid
xychart-beta
    title "rullerzhou-afk/memoria-chat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-31 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `ac3cda7ca730` · [字段定义](../../DATASET.md)*
