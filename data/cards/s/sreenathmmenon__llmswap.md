# sreenathmmenon/llmswap

⭐ 35 · Python · MIT · 推送 2026-08-03 · [GitHub](https://github.com/sreenathmmenon/llmswap) · [官网](https://llmswap.org) · 个人维护

**统一接口访问 10 家 LLM 的 Python SDK/CLI：问答、对比与综合**

BYOK（自带密钥）的 Python SDK 与 CLI，通过同一接口接入 OpenAI、Anthropic、Gemini、Ollama 等 10 家提供商，支持问答、聊天、函数调用、异步客户端、本地 stdio MCP 服务器与工作区上下文管理。Best Answer 机制生成 2-5 个独立候选回答并由 judge 模型综合，返回一致性、分歧与警示；默认同提供商以保持隐私，跨提供商需显式同意。附带本地浏览器 Arena 对比多模型。需 Python 3.9+，通过 pip 安装。

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

- 统一 API/CLI 接入 10 家 LLM 提供商，自带密钥
- Best Answer 多候选+judge 综合模式，含一致性与分歧标注
- 本地 Arena 浏览器对比多模型的延迟与 token 用量
- 本地 stdio MCP 服务器与 llmswap doctor 安装诊断

## 适用场景

- 在应用中切换 LLM 提供商而不改写周边代码
- 对比多个模型的回答并生成交叉核验的综合答案
- 通过 CLI 与本地 MCP 服务器用自然语言调用工具

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: Ask one model, compare many, or synthesize one cross-checked answer. LLMSwap is
> L10: an open-source Python SDK, CLI, and local Arena for working directly with 10 LLM
> L13: Bring your own provider keys, keep control of routing, and switch models without

## 星数曲线

```mermaid
xychart-beta
    title "sreenathmmenon/llmswap 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-28 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `34a75335895a` · [字段定义](../../DATASET.md)*
