# Sinapsis-AI/sinapsis-chatbots

⭐ 25 · Python · AGPL-3.0 · 推送 2026-08-03 · [GitHub](https://github.com/Sinapsis-AI/sinapsis-chatbots) · [官网](https://sinapsis.tech/) · 组织维护

**面向开发者的 Sinapsis 聊天机器人模板 monorepo，覆盖多种 LLM 后端**

Sinapsis Chatbots 是一个 monorepo，汇集多个聊天机器人工作区包：共享聊天抽象（chatbots-base）、Anthropic Claude 模板、基于 llama-cpp-python 的本地 GGUF 推理、基于 LlamaIndex 的摄取/检索/重排与 PGVector 语义缓存、Mem0 持久记忆、SQL 聊天历史存储，以及 vLLM 批量/流式/多模态补全模板。提供 Gradio 演示 webapp 与 Docker compose 启动方式；限制：Docker 镜像依赖 sinapsis-nvidia:base 基础镜像，vLLM 多模态与本地 llama-cpp 变体可能需要 GPU 调优。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Anthropic、vLLM、llama-cpp、OpenAI 兼容端点等多后端的模板套件
- LlamaIndex 检索模板含 PGVector 语义缓存读写
- Mem0 持久记忆模板（托管与自托管后端）
- Docker compose 一键启动 RAG/多模态/记忆等聊天机器人演示

## 适用场景

- 基于模板组合搭建多后端聊天机器人
- 为 Agent 添加持久记忆与聊天历史存储
- 本地 GGUF/vLLM 推理构建 RAG 聊天演示

## 场景标签

`聊天机器人` `RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L17: The `sinapsis-chatbots` project groups the Sinapsis chatbot packages in one workspace. It covers
> L65: This repository is structured into modular packages, each facilitating the integration of AI-driven chatbots with v

## 星数曲线

```mermaid
xychart-beta
    title "Sinapsis-AI/sinapsis-chatbots 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5dcec25dd30a` · [字段定义](../../DATASET.md)*
