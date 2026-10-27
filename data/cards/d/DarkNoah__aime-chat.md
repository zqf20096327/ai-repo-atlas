# DarkNoah/aime-chat

⭐ 46 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/DarkNoah/aime-chat) · [官网](https://darknoah.github.io/aime-chat/) · 个人维护 · 中文 README

**跨平台 AI 桌面协作应用：多模型对话、RAG 知识库与 MCP 工具**

基于 Electron + React + Mastra 构建的跨平台桌面 AI Cowork 应用。围绕模型提供完整 Agent Harness：编排循环、文件/代码执行/网页/视觉等工具、子 Agent、守护栏与可观测性。支持 10+ 家 AI 提供商（OpenAI、DeepSeek、智谱、Ollama、LMStudio 等，云端与本地均可）。内置本地知识库（语义+BM25 混合检索）、定时 Cultivation 记忆 Agent、MCP 客户端、语音/视频/3D 生成、技能市场与微信/Telegram 渠道接入。数据本地存储优先；从源码用 pnpm 构建打包，macOS 未签名需 xattr 处理。

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

- 接入 10+ 家云端与本地 AI 提供商，各提供商独立配置
- 本地知识库：语义+BM25 混合检索、可选重排、原文溯源
- Mastra Agent 运行时：流式输出、多步工具调用、子 Agent 与定时任务
- MCP 协议客户端、技能市场与后台 Bash 会话管理

## 适用场景

- 在桌面端用多个云/本地模型完成对话与项目协作
- 搭建本地知识库并让 Agent 检索回答
- 通过定时任务和记忆 Agent 维护长期项目上下文
- 把 AI 能力接入微信/Telegram 渠道

## 场景标签

`AI 助手` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L17: - 🤝 **Open CoWork Capability** - AI is not just for chatting: it can edit project files in an integrated workspace,
> L15: - 💬 **Intelligent Conversations** - Powerful AI Agent system based on Mastra framework, supporting streaming respon

## 星数曲线

```mermaid
xychart-beta
    title "DarkNoah/aime-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-27 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4b88d9492906` · [字段定义](../../DATASET.md)*
