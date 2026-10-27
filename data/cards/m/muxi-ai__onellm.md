# muxi-ai/onellm

⭐ 52 · Python · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/muxi-ai/onellm) · [官网](https://muxi.org) · 组织维护

**统一接口接入多家 LLM 提供商的 Python 客户端库**

OneLLM 是一个 provider 无关的 Python 库，遵循 OpenAI 客户端 API 设计，提供 ChatCompletion、Completion、Embedding 等接口，通过统一接口访问 22 个提供商的约 300+ 模型，覆盖 Anthropic、Bedrock、Gemini、Mistral 等。特性包括语义缓存、自动回退与重试、连接池、流式与多模态支持。本地侧支持 Ollama、llama.cpp 运行 GGUF 模型，以及进程内 HuggingFace 嵌入（ONNX Runtime 优先、PyTorch 回退），内置 CLI 从 HuggingFace 下载 GGUF 模型。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 22 个提供商、300+ 模型的统一 OpenAI 兼容接口
- 语义缓存、自动回退与重试机制
- 内置 onellm download CLI 下载 HuggingFace GGUF 模型
- local/ 进程内嵌入：ONNX Runtime 优先，支持 CUDA/CoreML 执行后端

## 适用场景

- 用现有 OpenAI 代码最小改动接入多家模型提供商
- 在应用中加入模型回退与语义缓存以提升可靠性
- 本地运行 GGUF 模型或生成 HuggingFace 嵌入

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L33: **OneLLM** is a lightweight, provider-agnostic Python library that offers a unified interface for interacting with 
> L37: With support for 22 implemented providers (and more planned), OneLLM gives you access to approximately 300+ unique 

## 星数曲线

```mermaid
xychart-beta
    title "muxi-ai/onellm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-27 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a9aced26a9fb` · [字段定义](../../DATASET.md)*
