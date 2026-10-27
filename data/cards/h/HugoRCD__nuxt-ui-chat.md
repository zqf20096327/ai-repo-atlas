# HugoRCD/nuxt-ui-chat

⭐ 112 · Vue · 推送 2026-10-22 · [GitHub](https://github.com/HugoRCD/nuxt-ui-chat) · [官网](https://nuxt-ui-chat.hrcd.fr) · 个人维护

**基于 Nuxt 与 Vercel AI SDK 的流式多模型 AI 聊天应用**

使用 Nuxt 3、Nuxt UI Pro 与 Vercel AI SDK v5 构建的 AI 聊天应用：提供流式响应、经 Vercel AI Gateway 接入 OpenAI、Anthropic、Google 等多模型、推理模型支持与生成式 UI（AI 生成天气组件等交互组件）。持久化聊天历史存于 PostgreSQL（Drizzle ORM），GitHub OAuth 登录，语法高亮与响应式界面。部署推荐 Vercel，也可在任何支持 Node.js 与 PostgreSQL 的平台运行；生产使用需 Nuxt UI Pro 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Vercel AI SDK v5 流式响应与多模型接入（经 AI Gateway）
- Generative UI：AI 生成天气组件等交互界面
- PostgreSQL + Drizzle ORM 持久化聊天历史与搜索
- GitHub OAuth 认证与命令面板快捷键

## 适用场景

- 部署一个多模型切换的 AI 聊天网页应用
- 作为 Nuxt + AI SDK 全栈项目模板二次开发
- 体验生成式 UI 与流式推理模型输出

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: A modern, full-featured AI chatbot application built with Nuxt 3, Nuxt UI Pro, and the Vercel AI SDK v5. Features re
> L9: - ⚡️ **Streaming AI responses** powered by Vercel AI SDK v5
> L10: - 🤖 **Multiple AI models** support via Vercel AI Gateway - access OpenAI, Anthropic, Google, and more

## 星数曲线

```mermaid
xychart-beta
    title "HugoRCD/nuxt-ui-chat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 111 --> 114
    line [113, 112, 112]
```

2026-10-18 113 → 2026-10-27 112（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `35a21ab14978` · [字段定义](../../DATASET.md)*
