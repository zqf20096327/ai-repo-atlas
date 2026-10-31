# dieharders/obrew-studio-server

⭐ 17 · Python · MIT · 推送 2026-05-16 · [GitHub](https://github.com/dieharders/obrew-studio-server) · [官网](https://www.openbrew.ai) · 个人维护

**自托管的本地 AI 引擎：推理/RAG/向量库/Agent 一体化桌面服务**

开源桌面应用兼无头服务器，将本地 AI 的基础组件打包为一套服务：基于 llama.cpp 的开源模型（GGUF）推理、文件/网站生成向量嵌入、以 LlamaIndex + ChromaDB 构建的知识库检索、Agent 与工作流构建。后端为 FastAPI Web 服务器，提供 WebUI 与 API 访问方式，可被第三方应用或自定义技术栈接入。目前提供 Windows/macOS 安装包，Linux 安装包与观测性、语音、视频模态等仍在路线图中，README 标注项目处于活跃开发阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地运行 GGUF 开源模型的推理与嵌入生成
- LlamaIndex + ChromaDB 向量知识库检索
- Agent 与工作流构建，支持自定义工具
- GUI 桌面应用与 headless API 双模式运行

## 适用场景

- 在本地免费搭建带私有数据的 AI 应用引擎
- 通过 API 将本地推理与 RAG 能力接入自己的技术栈
- 构建可调度的私有 Agent 与工作流

## 场景标签

`推理引擎` `RAG` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: The goal of this project is to be an all-in-one solution for running local Ai that is easy to install, setup and use
> L19: This backend runs a web server that acts as the main gateway to the suite of tools. A WebUI is provided called Open
> L81: - Inference: llama-cpp for LLM inference.

## 星数曲线

```mermaid
xychart-beta
    title "dieharders/obrew-studio-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `63008f9871a2` · [字段定义](../../DATASET.md)*
