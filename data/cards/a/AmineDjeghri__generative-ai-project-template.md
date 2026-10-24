# AmineDjeghri/generative-ai-project-template

⭐ 118 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/AmineDjeghri/generative-ai-project-template) · [官网](http://aminedjeghri.com/generative-ai-project-template/) · 个人维护

**生成式 AI 项目脚手架模板：快速搭建带 LLM、RAG 与评测的工程**

面向开发者的生成式 AI 项目起始模板：前后端 monorepo（NiceGUI 前端 + FastAPI 后端），用 uv 管理工作区依赖。内置 LLM 接入通道——本地通过 Ollama、云端通过 LiteLLM 兼容任意提供商（OpenAI、Anthropic、Azure 等），并提供信息抽取、文档问答、聊天与 RAG 功能。集成 Promptfoo 与 Ragas 作为评测和红队框架，附带 Docker 容器化、Make 命令、GitHub Actions CI/CD、pre-commit 与 MkDocs 文档。支持 CPU 与 NVIDIA CUDA 两种安装路径。作为模板使用，需 git clone 后配置 .env。

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

- 本地 Ollama 与云端 LiteLLM 双通道 LLM 接入，含专属 Make 命令
- NiceGUI 前端 + FastAPI 后端的 uv 工作区 monorepo
- Promptfoo 与 Ragas 作为评测/红队框架
- Docker Compose（CPU/CUDA）与 GitHub Actions CI/CD 流水线

## 适用场景

- 新起生成式 AI 项目时复用完整工程脚手架
- 搭建本地或云端 LLM 的原型应用（聊天、RAG、信息抽取）
- 在 CI 中持续测试 AI 系统与本地模型

## 场景标签

`RAG` `文档问答` `模型评测` `MLOps` · 领域:评测与运维

## 证据(README 行号)

> L20: Template for a new AI Cloud project.
> L24: This project is a generative ai template. It contains the following features: LLMs, information extraction, chat, r
> L43: - [x] LLM running locally with Ollama or in the cloud with any LLM provider (LiteLLM)

## 星数曲线

```mermaid
xychart-beta
    title "AmineDjeghri/generative-ai-project-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 117 --> 119
    line [118, 118]
```

2026-10-18 118 → 2026-10-24 118（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b6e0ce6ecba8` · [字段定义](../../DATASET.md)*
