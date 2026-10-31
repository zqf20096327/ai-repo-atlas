# AnthonyTlei/langchain-codex-oauth

⭐ 14 · Python · MIT · 推送 2026-08-13 · [GitHub](https://github.com/AnthonyTlei/langchain-codex-oauth) · [官网](https://pypi.org/project/langchain-codex-oauth/1.0.0/) · 个人维护

**用 ChatGPT 订阅的 Codex 模型接入 LangChain/LangGraph 的适配器**

Python 适配器库，将 ChatGPT Plus/Pro 订阅包含的 Codex 模型包装为 LangChain 风格的聊天模型（ChatCodexOAuth）：通过本地 OpenAI OAuth 登录认证（无需 API key，凭据存于 ~/.langchain-codex-oauth/），支持流式输出、异步调用、工具绑定（可配 LangGraph agent）、结构化输出等。面向已持有 ChatGPT 订阅的开发者。项目标注为 Legacy，明确不用于生产或多用户托管；上游为消费级端点，可能随时变更导致兼容性破坏。

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

- 本地 OAuth 登录，无需 OPENAI_API_KEY
- 支持流式/异步调用与工具绑定（LangGraph agent 可用）
- 兼容部分 ChatOpenAI 参数（timeout/temperature/max_tokens/stop 等）
- 提供 RAG 示例（Chroma + 本地嵌入的 A/B 测试脚本）

## 适用场景

- 已有 ChatGPT 订阅的开发者在 LangChain/LangGraph 中调用 Codex 模型
- 为 LangGraph agent 绑定工具调用 Codex
- 配合本地嵌入模型搭建 RAG 原型

## 场景标签

 · 领域:LLM 基础设施/框架适配

## 证据(README 行号)

> L3: Use the Codex models included with a **ChatGPT Plus/Pro** subscription inside **LangChain/LangGraph**.
> L8: - A dev-friendly adapter that makes Codex feel like a native-ish LangChain chat model.

## 星数曲线

```mermaid
xychart-beta
    title "AnthonyTlei/langchain-codex-oauth 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `99fafa366e11` · [字段定义](../../DATASET.md)*
