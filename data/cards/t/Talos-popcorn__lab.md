# Talos-popcorn/lab

⭐ 15 · TypeScript · AGPL-3.0 · 推送 2026-09-06 · [GitHub](https://github.com/Talos-popcorn/lab) · [官网](https://labstudio.tech) · 个人维护 · 中文 README

**本地优先的无后端 LLM 聊天前端，可接入多种模型端点**

纯静态、运行于浏览器的 LLM 对话界面，定位为 Open WebUI / Google AI Studio 的替代：无需后端与服务器数据库，API 密钥、设置与聊天记录全部存储在浏览器 IndexedDB。支持连接 Ollama、OpenAI、Groq、OpenRouter 及任意 OpenAI 兼容端点并可同时接入切换。功能含实时 token 追踪与消息固定、滑动窗口裁剪、Monaco 代码编辑器、LaTeX 渲染、语音输入输出、ToolHub 工具调用代理编排；GraphMem 知识图谱集成尚未公开发布。基于 Bun 构建，需自行 build 部署；AGPL-3.0 并另设商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 无后端纯静态架构，数据存于浏览器 IndexedDB，可完全离线运行
- 多供应商接入：Ollama、OpenAI、Groq、OpenRouter 及任意 OpenAI 兼容端点，可同时连接
- 实时 token 追踪、消息固定、滑动窗口自动裁剪与代码块压缩的上下文管理
- Monaco 代码编辑器、LaTeX 公式渲染、STT/TTS 语音引擎与 ToolHub 代理工具调用

## 适用场景

- 在本地或气隙环境配合本地 LLM 使用，数据不出浏览器
- 同时接入多家模型供应商并快速切换与搜索对比
- 对长对话做 token 级上下文裁剪与成本控制

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: Minimalist, ultra-fast, and completely **serverless** alternative to heavy AI web interfaces like Open WebUI.
> L33: * **Zero Backend / Client-Full:** Everything runs strictly client-side. Your API keys and data live securely in you
> L34: * **Multi-Provider & Fast Search:** Connect and switch between Ollama, OpenAI, Groq, OpenRouter, or any OpenAI-comp

## 星数曲线

```mermaid
xychart-beta
    title "Talos-popcorn/lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `081d9e55323e` · [字段定义](../../DATASET.md)*
