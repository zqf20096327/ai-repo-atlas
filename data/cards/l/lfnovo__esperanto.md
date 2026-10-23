# lfnovo/esperanto

⭐ 221 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/lfnovo/esperanto) · 个人维护 · 中文 README

**统一多种 AI 模型服务商接口的轻量 Python 库**

面向开发者的 Python 库，通过直接 HTTP 调用（httpx，不依赖厂商 SDK）为 20+ 家 AI 提供商提供统一接口，覆盖 LLM 对话、Embedding、重排序、语音转文字与文字转语音五类能力。提供 AIFactory 创建实例与模型发现、标准化响应对象、同步/异步 API、流式输出、JSON 结构化输出及 LangChain 转换方法。可选安装 transformers extras 支持本地模型。

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

- 统一接口接入 20+ 提供商（OpenAI/Anthropic/Google/Ollama 等），切换不改代码
- 直接 HTTP 通信，不依赖各厂商 SDK
- 五类能力矩阵：LLM/Embedding/重排序/STT/TTS
- 任务感知 Embedding（8 种通用任务类型）与模型发现（结果缓存 1 小时）

## 适用场景

- 在应用中用同一套代码切换不同 LLM 提供商
- 接入本地 Ollama/vLLM/LM Studio 等 OpenAI 兼容端点
- 统一管理 Embedding、重排序与语音能力的多提供商调用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: Esperanto is a powerful Python library that provides a unified interface for interacting with various Large Language
> L32: - **Unified Interface**: Work with multiple LLM providers using a consistent API
> L63: - **Structured Output**: JSON mode + schema-driven outputs across all LLM providers (OpenAI, Azure, OpenAI-compatib

## 星数曲线

```mermaid
xychart-beta
    title "lfnovo/esperanto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 220 --> 222
    line [221, 221]
```

2026-10-18 221 → 2026-10-23 221（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `47c140f416c3` · [字段定义](../../DATASET.md)*
