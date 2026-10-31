# Hosseinghorbani0/ask-ai

⭐ 15 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/Hosseinghorbani0/ask-ai) · [官网](https://hosseinghorbani0.ir) · 个人维护

**一行代码切换 LLM 供应商的极简 Python SDK**

面向开发者的 Python SDK，将 OpenAI、Anthropic、Google Gemini、Groq、Azure、OpenRouter 等多家 LLM 供应商统一到单一的 .ask() 调用接口；API key 自动从环境变量读取，内置限流重试与超时、多供应商降级回退、同步/异步与流式输出、Pydantic 结构化输出、图像与音频生成、视觉多模态输入等能力。明确声明自身不是框架、不是 API 网关、不是 agent 记忆系统。以 PyPI 包 askai-python 分发，要求 Python 3.9+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一行代码切换 OpenAI/Groq/Gemini/Anthropic/Azure/OpenRouter 六家供应商
- 内置限流重试、超时与多供应商降级回退
- 同步/异步/流式调用与 Pydantic 结构化输出
- 图像与音频生成、视觉多模态输入

## 适用场景

- 在脚本或应用中快速调用多家 LLM 而不绑定单一供应商
- 为 LLM 调用增加自动重试与供应商降级
- 用 Pydantic schema 约束模型输出格式

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L15:  A minimal Python SDK to switch between LLM providers in one line.
> L38: - **Multiple providers**: OpenAI, Anthropic, Google Gemini, Groq, Azure, OpenRouter
> L44: > ❌ Not an AI framework

## 星数曲线

```mermaid
xychart-beta
    title "Hosseinghorbani0/ask-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `e1ed2128e0a6` · [字段定义](../../DATASET.md)*
