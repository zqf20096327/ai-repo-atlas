# Gr1shma/g7-chat

⭐ 19 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/Gr1shma/g7-chat) · 个人维护

**自托管极简 AI 聊天界面，BYOK 多模型对话**

基于 Next.js/tRPC/Drizzle/PostgreSQL 的自托管全栈 AI 聊天应用，面向重视数据自主权的个人用户。提供项目/线程管理、消息编辑与重试、线程导出、AI 人格设定（注入动态系统提示词）等功能。模型接入采用 BYOK 模式，通过 Vercel AI SDK 支持 Google、Groq、OpenRouter、OpenAI 四家提供商，API key 仅存于浏览器本地。需自行部署：克隆源码、配置 Google OAuth 与 PostgreSQL 环境变量后构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BYOK 模式：API key 存储在浏览器本地，不出现在服务端
- 支持 Google/Groq/OpenRouter/OpenAI 多提供商，运行时可切换模型（默认 Gemini 2.0 Flash）
- 项目/线程组织、消息编辑重试、线程 JSON 导出
- AI 人格与称呼偏好通过动态系统提示词生效

## 适用场景

- 自部署一个数据不被锁定的私人 AI 聊天界面
- 用同一个界面切换多家模型的 API key 使用
- 按项目组织并导出长期对话线程

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L13: g7-chat provides a distraction-free interface to interact with AI assistants, giving users full visibility and mana
> L243: g7-chat supports multiple AI model providers with a clean, type-safe integration using the Vercel AI SDK. The app 

## 星数曲线

```mermaid
xychart-beta
    title "Gr1shma/g7-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1d4b5fbec9a2` · [字段定义](../../DATASET.md)*
