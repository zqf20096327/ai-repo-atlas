# openchatui/openchat

⭐ 61 · TypeScript · NOASSERTION · 推送 2025-11-13 · [GitHub](https://github.com/openchatui/openchat) · [官网](https://openchatui.org) · 组织维护

**自托管的开源 AI 聊天用户界面（Web 应用）**

基于 Next.js/TypeScript 的自托管 AI 用户界面，面向需要私有部署聊天前端的用户。功能包括多提供商接入的文本生成（OpenAI/OpenRouter/Ollama）、图像生成、视频生成（Sora 2）、语音对话与 TTS、网页自动化工具、Google Drive/Docs 或本地文档集成，以及文件夹/标签/分享等聊天管理。数据层支持 SQLite 或 PostgreSQL（Prisma），带认证、角色与 REST API 文档。安装途径为源码 npm 运行或 Docker 单容器/Compose 部署。部分能力（如 Bedrock、Azure 等）列于 Wishlist 尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多提供商文本生成：OpenAI、OpenRouter、Ollama（经 AI SDK）
- 图像生成、视频生成（Sora 2）、语音对话与 TTS
- SQLite/PostgreSQL 双数据库支持，Docker 与 Docker Compose 部署
- 内置 REST API 文档（Swagger UI）与会话/角色认证

## 适用场景

- 私有部署一个多模型聊天界面供个人或团队使用
- 在本地或自有服务器上统一访问 OpenAI、OpenRouter、Ollama 等模型
- 结合 Google Drive/本地文档进行带文件阅读的对话

## 场景标签

`聊天机器人` `图像生成` `视频生成` `语音合成` · 领域:对话与助手

## 证据(README 行号)

> L12: **OpenChat is an open source, self-hosted, AI User Interface** with the goal of developing the most **feature rich,
> L95: - 🤖 Multi‑provider AI: OpenAI, OpenRouter, Ollama (via AI SDK)

## 星数曲线

```mermaid
xychart-beta
    title "openchatui/openchat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-26 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a4018e733f61` · [字段定义](../../DATASET.md)*
