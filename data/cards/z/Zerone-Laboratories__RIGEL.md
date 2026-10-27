# Zerone-Laboratories/RIGEL

⭐ 30 · Python · AGPL-3.0 · 推送 2026-06-01 · [GitHub](https://github.com/Zerone-Laboratories/RIGEL) · [官网](https://rigel.verisimilitude-lk.online) · 组织维护

**开源多智能体 AI 引擎与虚拟助手框架，统一多 LLM 后端**

面向构建 AI 应用、聊天机器人与智能体系统的多 LLM 引擎：通过统一接口接入 Ollama（本地）与 Groq（云端）推理，LLAMA.cpp 与 Transformers 后端在状态表中标注为未完成。提供 D-Bus 服务器（Linux 系统级 AI 助手）与 HTTP REST API 服务器两种运行模式，内置 MCP 工具（文件管理、系统命令）、基于 ChromaDB 的 RAG、Whisper/Piper 本地语音识别与合成、图像分析端点、浏览器自动化工作流录制与回放。安装方式为 git clone、PyPI（rigel-engine-core）或 Docker Compose；D-Bus 功能需 Linux 系统依赖（python3-gi 等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一接口多后端：Ollama 本地推理与 Groq 云端推理已支持
- D-Bus 服务器与 HTTP REST API（含 OpenAPI 文档与 API key 多租户管理）
- MCP 工具：文件管理、系统命令、外部 MCP 服务器集成
- 本地语音能力：Whisper 语音识别、Piper 语音合成、语音克隆端点

## 适用场景

- 在 Linux 桌面通过 D-Bus 获得系统级 AI 助手
- 作为中心 AI 服务器为多个智能体客户端与 AI 应用提供推理
- 录制一次浏览器自动化流程后无限次免 AI 回放

## 场景标签

`Agent 框架` `多智能体` `AI 助手` `浏览器自动化` · 领域:Agent 开发

## 证据(README 行号)

> L22: RIGEL is a powerful **open-source multi-agentic AI engine** and **virtual assistant framework** that provides a uni
> L39: Aims to act as a central AI server for multiple agentic-based clients and AI-powered applications.

## 星数曲线

```mermaid
xychart-beta
    title "Zerone-Laboratories/RIGEL 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-27 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2836f8d64b94` · [字段定义](../../DATASET.md)*
