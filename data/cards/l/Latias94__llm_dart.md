# Latias94/llm_dart

⭐ 25 · Dart · MIT · 推送 2026-05-27 · [GitHub](https://github.com/Latias94/llm_dart) · 个人维护

**Dart/Flutter 的多 LLM 提供商统一接入库**

模块化 Dart 库，为 LLM 提供商提供 provider 中立的模型优先 API、提供商专属类型化选项与 Flutter 聊天会话层。根包 llm_dart 负责消息、聊天运行时与传输契约，各提供商以独立包接入：OpenAI 家族（含 DeepSeek/OpenRouter/Groq/xAI）、Anthropic、Google、Ollama、ElevenLabs（语音/转录）。支持流式输出、结构化 JSON、工具调用、嵌入与 Web 搜索示例。当前处于 0.11.0-alpha.x 预览线，1.0.0 前允许破坏性变更。

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

- 跨 OpenAI/Anthropic/Google/Ollama/ElevenLabs 等提供商的统一 API，仅改工厂与模型 ID 即可切换
- 11 个工作区子包拆分：契约、传输（HTTP/SSE）、纯 Dart 聊天会话、Flutter 适配层
- generateTextCall/streamTextCall 等多层文本调用接口与结构化输出辅助
- 提供 8 个可运行示例：流式、工具调用、结构化输出、嵌入、Flutter 集成等

## 适用场景

- Flutter/Dart 应用统一接入多家 LLM 提供商
- 在 OpenAI、Anthropic、Ollama 等模型间低成本切换
- 为聊天应用构建可持久化的会话层与聊天控制器
- 自研新 LLM 提供商接入（provider_authoring 契约）

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: Modular Dart library for LLM providers with a stable model-first API,
> L15: - `llm_dart` for provider-neutral messages, result helpers, chat runtime, and
> L17: - one provider package for concrete models, such as `llm_dart_openai`,

## 星数曲线

```mermaid
xychart-beta
    title "Latias94/llm_dart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `10159a238781` · [字段定义](../../DATASET.md)*
