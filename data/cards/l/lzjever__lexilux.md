# lzjever/lexilux

⭐ 16 · Python · Apache-2.0 · 推送 2026-02-13 · [GitHub](https://github.com/lzjever/lexilux) · [官网](https://lexilux.readthedocs.io) · 组织维护 · 中文 README

**给 Python 开发者的统一 LLM API 客户端库**

Lexilux 是一个 Python 统一 LLM API 客户端库，以函数式调用方式封装 Chat、Embedding、Rerank 和 Tokenizer 四类 API，通过 OpenAI 兼容接口接入 OpenAI、DeepSeek、GLM、Kimi、Minimax、Qwen、Groq 等服务商，切换仅需修改 base_url 与 api_key。内置流式输出、统一 usage 统计、指数退避自动重试、连接池、速率限制、SSL 配置、函数调用、多模态视觉输入与完整 async API。需要 Python 3.9+，通过 pip 安装，tokenizer 支持为可选附加项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 函数式调用 API：chat()/embed() 等，统一封装 Chat/Embedding/Rerank/Tokenizer
- OpenAI 兼容，切换服务商只需改 base_url 与 api_key
- 内置流式、统一 usage 统计、自动重试、连接池、速率限制
- 函数调用、多模态视觉输入与完整 async/await API

## 适用场景

- 在多个 OpenAI 兼容 LLM 服务商之间用同一套代码切换调用
- 在应用中同时处理对话、嵌入、重排与 token 统计
- 需要限流、重试与连接池控制的 LLM API 调用场景

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10: **Lexilux** is a unified LLM API client library that makes calling Chat, Embedding, Rerank, and Tokenizer APIs as s
> L31: Lexilux is designed to work seamlessly with all major LLM providers through their OpenAI-compatible APIs:

## 星数曲线

```mermaid
xychart-beta
    title "lzjever/lexilux 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `eaaa07aedc16` · [字段定义](../../DATASET.md)*
