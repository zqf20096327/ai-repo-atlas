# ariya/chat-llm

⭐ 19 · JavaScript · MIT · 推送 2026-07-15 · [GitHub](https://github.com/ariya/chat-llm) · 个人维护

**零依赖的终端/Web LLM 聊天工具，支持云端与本地模型**

以 Node.js 单脚本形式提供的 LLM 对话客户端，通过 LLM_API_BASE_URL 环境变量接入云端服务（OpenAI、Groq、DeepSeek、OpenRouter 等 13 家）或本地推理服务（llama.cpp、Ollama、Jan、LocalAI、LM Studio、Msty）。支持终端交互、管道快速提问、极简 Web 界面（HTTP_PORT 启动）与多语言对话；可读取问答文本文件，用正则验证多轮回答作为评测。运行需 Node.js v18+，配置通过环境变量完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零依赖 Node.js 脚本，终端与 Web 双界面
- 接入 13 家云端 LLM 服务与 6 种本地 LLM 服务
- 管道方式单次提问与文件驱动的多轮问答评测
- 多语言对话与查询间语言切换

## 适用场景

- 在终端快速向云端或本地 LLM 提问并获取回答
- 通过浏览器界面与自托管 LLM 对话
- 用文本文件批量提问并以正则核验答案

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: **Chat LLM** is a simple, zero-dependency tool to chat with an LLM (large language model). It works seamlessly with 
> L5: Chat LLM is accessible via the terminal or through its minimalist web interface.

## 星数曲线

```mermaid
xychart-beta
    title "ariya/chat-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `9b3b3c28d958` · [字段定义](../../DATASET.md)*
