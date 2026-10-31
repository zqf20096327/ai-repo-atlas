# PRABHUSIDDARTH/sidd-ai

⭐ 19 · Java · NOASSERTION · 推送 2026-10-11 · [GitHub](https://github.com/PRABHUSIDDARTH/sidd-ai) · [官网](https://www.producthunt.com/products/sidd-ai?launch=sidd-ai) · 个人维护

**Java 开发者的多 LLM 统一调用 SDK（8 家提供商）**

面向 Java 开发者的轻量 LLM 客户端库：通过单一 AiClient 接口调用 OpenAI、Gemini、Claude、Grok、Groq、Kimi、NVIDIA NIM 与本地 Ollama 共 8 家提供商。核心机制为按模型名前缀自动路由的 ModelRouter，也可显式指定提供商；凭据从 builder、环境变量或 .env 依序读取。无 Spring/依赖注入/YAML 依赖，仅 Jackson 一个运行时依赖，基于 JDK HttpClient。要求 Java 17+，经 Maven Central 或 fat jar 分发。README 中含与 Spring AI、LangChain4j 的能力对比表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 AiClient 接口接入 8 家提供商，切换模型只需改字符串
- ModelRouter 按模型名前缀自动路由，支持显式指定提供商
- 统一异常层级与含 token 用量的 ChatResponse 元数据
- 零配置凭据：环境变量或 .env 自动加载

## 适用场景

- 在纯 Java 环境中不引入 Spring 即可调用多家 LLM
- 通过改模型名字符串在不同提供商间切换
- 用同一套代码访问云端模型与本地 Ollama

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L23: `sidd-ai` is a minimal Java library that gives you a single, consistent interface to multiple AI providers. It requ
> L29: If you know LiteLLM from Python, `sidd-ai` aims to fill the same role for Java.
> L33: - **Unified API**: one `AiClient` for eight providers, so switching models means changing a string.

## 星数曲线

```mermaid
xychart-beta
    title "PRABHUSIDDARTH/sidd-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e2f8e743f73b` · [字段定义](../../DATASET.md)*
