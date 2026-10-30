# Some1Uknow/chatgpt-cloned

⭐ 38 · TypeScript · NOASSERTION · 推送 2025-11-16 · [GitHub](https://github.com/Some1Uknow/chatgpt-cloned) · [官网](https://chat-gpt0.vercel.app) · 个人维护

**复刻 ChatGPT 的全栈 AI 对话应用：流式回复+长期记忆**

基于 Next.js 14、TypeScript 与 Vercel AI SDK 构建的全栈 ChatGPT 克隆应用：接入 OpenAI GPT-4 提供逐 token 流式对话，支持文本/图像/PDF 多模态输入与文件上传文本提取，通过 mem0.ai 与 MongoDB 实现跨会话持久记忆，Clerk 提供用户认证，Uploadcare 提供文件存储。面向希望学习现代全栈开发与 AI 集成模式的开发者，定位为教学/参考项目，运行需自备 OpenAI、Clerk、Uploadcare、mem0.ai 等 API key 与 MongoDB。

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

- Vercel AI SDK 驱动的逐 token 流式回复
- 文本/图像/PDF/DOCX 多模态输入与文本提取
- mem0.ai + MongoDB 的跨会话长期记忆
- Clerk 认证与 RESTful API 路由（chat/upload/memory）

## 适用场景

- 学习 Next.js 14 + AI SDK 的流式对话集成模式
- 参考带认证、数据库与文件处理的全栈 AI 应用架构
- 作为自部署对话应用的基础进行二次开发

## 场景标签

`聊天机器人` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L1: # ChatGPT Clone - Full-Stack AI Chat Application | Next.js 14, AISDK, mem0, OpenAI
> L29: - **Real-Time Streaming Responses** - Token-by-token AI responses using Vercel AI SDK
> L31: - **Long-Term Memory** - Persistent conversation context with mem0.ai

## 星数曲线

```mermaid
xychart-beta
    title "Some1Uknow/chatgpt-cloned 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7afef6549eb3` · [字段定义](../../DATASET.md)*
