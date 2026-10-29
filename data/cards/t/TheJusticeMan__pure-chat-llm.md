# TheJusticeMan/pure-chat-llm

⭐ 18 · TypeScript · MIT · 推送 2026-08-11 · [GitHub](https://github.com/TheJusticeMan/pure-chat-llm) · 个人维护

**把 Obsidian 笔记变成 AI 对话界面的插件，带 Agent 工具**

Obsidian 社区插件，将任意笔记转为内联 AI 聊天界面，支持 OpenAI、Gemini、xAI、Anthropic、Cohere、Mistral AI、DeepSeek 等多家提供商切换。提供 13 个工具（读/写笔记、布尔与正则搜索、文件发现、反向链接分析、图像生成、RAG 语义搜索、工作区管理等），开启 Agent Mode 后 AI 可自主调用工具操作知识库，所有破坏性操作需经带 diff 视图的确认弹窗。另支持基于 OpenAI Realtime API 的 WebRTC 实时语音通话并可在通话中使用工具。可通过 Obsidian 社区插件市场或手动放置文件安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个 Agent 工具：笔记读写、布尔/正则搜索、反向链接、RAG 语义搜索（依赖 Smart Connections 插件）
- 多提供商接入：OpenAI、Gemini、xAI、Anthropic、Cohere、Mistral AI、DeepSeek
- 破坏性操作须经带可视化 diff 的用户确认弹窗
- 基于 OpenAI Realtime API 与 WebRTC 的实时语音通话，通话中可用工具

## 适用场景

- 在笔记内直接与 AI 对话并引用其他笔记内容
- 让 AI 自动搜索、汇总并写入笔记（经我确认后执行）
- 通过语音对话让 AI 记录会议并生成笔记
- 为不同笔记按 JSON 块配置不同模型与参数

## 场景标签

`知识库管理` `语音 Agent` `RAG` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L7: **Transform your Obsidian notes into powerful AI conversations with built-in agent capabilities.**
> L13: **Pure Chat LLM** turns Obsidian notes into interactive AI chat interfaces with unprecedented integration into your
> L60: - **Multiple AI providers**: Switch between OpenAI, Gemini, xAI, Anthropic, and more

## 星数曲线

```mermaid
xychart-beta
    title "TheJusticeMan/pure-chat-llm 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [18, 17, 18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4c3b1601ddd7` · [字段定义](../../DATASET.md)*
