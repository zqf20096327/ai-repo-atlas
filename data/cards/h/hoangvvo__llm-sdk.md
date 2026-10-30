# hoangvvo/llm-sdk

⭐ 23 · Rust · MIT · 推送 2026-09-24 · [GitHub](https://github.com/hoangvvo/llm-sdk) · [官网](https://llm-sdk.hoangvvo.com/) · 个人维护

**多语言统一 LLM 客户端 SDK 与极简 agent 库（JS/Rust/Go）**

提供两个库：LLM SDK 以单一 LanguageModel 接口接入 OpenAI、Anthropic、Google、Cohere、Mistral 等提供商及 OpenAI 兼容 API，支持文本/图像/音频多模态、流式、函数调用、引用（RAG）与 token 用量/成本统计，并在 JS、Rust、Go 间保持一致的序列化格式；LLM Agent 是围绕 SDK 的轻量 for-loop agent 运行时，无隐藏提示模板，核心约 500 行代码。两个库均处于 v0，Agent API 可能变化。附 Console 演示应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一接口接入多家提供商（含 OpenAI 兼容 API）
- 文本/图像/音频多模态与流式、函数调用、引用支持
- JS/Rust/Go 三语言统一序列化，跨语言服务可互操作
- 极简 agent 运行时（核心约 500 行），无隐藏提示模板

## 适用场景

- 用一套代码切换或接入多家 LLM 提供商
- 在多语言微服务间共享一致的模型请求/响应格式
- 基于透明可控的 agent 运行时构建工具调用应用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: - **LLM SDK** – cross-language clients (JavaScript, Rust, Go) that talk to multiple LLM providers through one `Langu
> L6: - **LLM Agent** – a minimal, transparent agent library that orchestrates model generations and tool executions using

## 星数曲线

```mermaid
xychart-beta
    title "hoangvvo/llm-sdk 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-30 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6ae3a4581f3d` · [字段定义](../../DATASET.md)*
