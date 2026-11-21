# 7ZoneSystems/NativeLab

⭐ 11 · Python · AGPL-3.0 · 推送 2026-11-16 · [GitHub](https://github.com/7ZoneSystems/NativeLab) · [官网](https://7zonesystems.github.io/NativeLab/) · 个人维护

**全本地 LLM 桌面/终端客户端，封装 llama.cpp 运行模型**

NativeLab 提供桌面 PyQt6 GUI 与终端 CLI 两种形态，在本机运行大语言模型：封装 llama.cpp，可接入运行中的 Ollama 模型、可选 Hugging Face Transformers 模型及 OpenAI/Anthropic 兼容 API 后端。功能涵盖多模型管线（20+ 节点可视化构建器）、@file 文档引用、长文摘要、技能管理、MCP、Labs 实验层，以及将任意 GGUF 转为 OpenAI/Anthropic 兼容 API 的本地服务器。配套 Android 客户端 PhonoLab 经 JNI 在端侧运行 llama.cpp，提供 RAG、视觉模型与局域网 API 服务。要求 Python 3.10+ 与 llama.cpp 二进制（可在应用内下载）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 桌面 GUI + Claude-Code 风格终端 CLI 双形态，统一管理聊天/模型/管线
- 本地 GGUF、Ollama、HF Transformers、OpenAI/Anthropic API 混合作为后端
- 20+ 节点的可视化管线构建器与 Labs 实验层（共享 endpoint API）
- 本地服务器可将任意 GGUF 转为 OpenAI/Anthropic 兼容 API

## 适用场景

- 在本地机器上运行 GGUF 模型聊天与长文摘要
- 用可视化管线把多个本地/API 模型串联执行
- 把本地 GGUF 模型暴露成 OpenAI 兼容 API 供其他工具调用
- 在 Android 手机端侧运行小模型并做文档 RAG

## 场景标签

`AI 助手` `工作流自动化` `RAG` `推理引擎` · 领域:效率与自动化

## 证据(README 行号)

> L21: NativeLab is a desktop and terminal client for running large language models entirely on your machine. It wraps lla
> L108: - 🌐 **Backend mixing** - Local GGUF, running Ollama models, optional Hugging Face Transformers models, OpenAI-comp
> L114: - 🖧 **Local server app** - `python -m nativelab.server` turns any GGUF model into an OpenAI/Anthropic compatible A

## 星数曲线

```mermaid
xychart-beta
    title "7ZoneSystems/NativeLab 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-22", "2026-11-21"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-10-19 10 → 2026-11-21 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `b03b0a2b942c` · [字段定义](../../DATASET.md)*
