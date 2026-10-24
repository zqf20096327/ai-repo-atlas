# hanyeol/model-compose

⭐ 120 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/hanyeol/model-compose) · 个人维护 · 中文 README

**用单个 YAML 声明式编排 AI 管线与应用的开源框架**

面向开发者的声明式 AI 编排工具：在一份 model-compose.yml 中组合模型、agent、工作流、工具与协议组件，以 model-compose up 命令运行，同一文件可在本地、Docker 或生产环境部署。支持混用本地模型（HuggingFace/vLLM/llama.cpp）与云端 API，内置 100+ 组件，覆盖 RAG、媒体处理、流式多模态、MCP 服务器等场景，自动生成 Gradio Web UI，可通过 Redis 队列横向扩展。MIT 许可，经 PyPI 提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式 YAML 定义 chat API、RAG、agent、MCP 服务器，无需编排代码
- 混用本地模型（HuggingFace/vLLM/llama.cpp）与 OpenAI/Anthropic/Google/xAI 云 API
- token/音频块/视频帧流式跨阶段传递，SSE/WebSocket/任务间流为一等公民
- 两行 YAML 生成 Gradio Web UI；Redis 队列支持分布式横向扩展

## 适用场景

- 不写代码快速搭建带 Web UI 的模型服务或 chat API
- 把 RAG 检索、媒体处理、实时 TTS 等多阶段管线组合为一个工作流
- 将既有工作流一键转为 Claude/Cursor/ChatGPT 可调用的 MCP 服务器
- 本地开发与容器化、多机部署使用同一份定义文件

## 场景标签

`工作流自动化` `RAG` `语音合成` `多模态` · 领域:效率与自动化

## 证据(README 行号)

> L15: Build chat APIs, RAG pipelines, autonomous agents, and MCP servers without writing orchestration code — then run th
> L92: Run open-weight models on your own hardware with PyTorch, vLLM, or llama.cpp — same YAML surface as cloud APIs, no 
> L209: - **Any model, anywhere** — HuggingFace, vLLM, llama.cpp locally, or OpenAI/Anthropic/Google/xAI via HTTP

## 星数曲线

```mermaid
xychart-beta
    title "hanyeol/model-compose 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 118 --> 121
    line [119, 120, 120]
```

2026-10-18 119 → 2026-10-24 120（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `be046267cafd` · [字段定义](../../DATASET.md)*
