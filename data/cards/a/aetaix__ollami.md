# aetaix/ollami

⭐ 67 · Svelte · MIT · 推送 2025-12-03 · [GitHub](https://github.com/aetaix/ollami) · 个人维护

**本地 Ollama 模型的 Web 聊天前端**

Ollami 是与本地 Ollama 服务交互的前端应用，供用户在浏览器（localhost:5050）中与本地模型进行文本生成、推理和对话。内置可用模型库供浏览下载；默认无需配置环境变量，直接连接本地 11434 端口的 Ollama 服务。安装途径：Docker Compose，或开发者模式 npm 运行（git clone 后 npm install / npm run dev），需先自行安装 Ollama 并拉取模型。README 同时给出模型参数与内存需求对照表。

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

- 连接本地 Ollama 服务进行文本生成、推理与对话
- 内置可下载运行的模型库（Llama 3、Mistral、Phi-3、Gemma 等）
- Docker Compose 一键部署，或 npm 开发模式运行
- 默认无需 .env 配置，自动连接 127.0.0.1:11434

## 适用场景

- 给本机 Ollama 服务配一个图形界面进行聊天
- 在真实应用界面中测试和评估本地模型表现
- 浏览并下载本地可运行的模型

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L6: Ollami is a frontend application designed to interact with local Ollama models for text generation, reasoning, chat 
> L16: Get up and running with large language models locally: Ollama Website.

## 星数曲线

```mermaid
xychart-beta
    title "aetaix/ollami 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-28 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `395ad796db9a` · [字段定义](../../DATASET.md)*
