# Mattbusel/Every-Other-Token

⭐ 26 · Rust · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Mattbusel/Every-Other-Token) · [官网](https://mattbusel.github.io/Every-Other-Token/) · 个人维护

**LLM token 流拦截查看器：逐 token 置信度与在线改写**

Rust 编写、CLI 与 Web UI 双形态的 LLM token 流查看/拦截工具：自行打开模型的 SSE 流式连接，从 logprobs 计算每个 token 的置信度与困惑度，并在生成途中按规则（每隔一个/低置信度词）做反转、大写、噪声等变换，观察模型置信度如何位移。支持 OpenAI、Anthropic、Gemini、OpenRouter 及本地 Ollama、llama.cpp、vLLM、LM Studio，内置免 key 的 mock provider；可选 local 特性在 CPU 上跑 SmolLM2-135M 并做遮挡归因。面向可解释性研究、红队与提示工程人员，输出 JSON/CSV/HTML 热图。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 logprobs 计算逐 token 置信度 exp(logprob) 与困惑度
- 生成途中在线变换 token（reverse/uppercase/noise/delete/synonym 等）
- 单二进制分发，含 1,165 个测试；内置免 API key 的 mock provider
- 可选 local 特性：candle 在 CPU 跑 SmolLM2-135M，含遮挡归因

## 适用场景

- LLM 可解释性研究中观察模型逐词置信度
- 红队与提示工程时定位生成过程中的脆弱 token
- 对比不同 provider 或 A/B 系统提示下的 token 流差异
- 无 API key 离线复现固定 logprobs 的示例输出

## 场景标签

 · 领域:LLM 工具/可解释性

## 证据(README 行号)

> L27: `every-other-token` is a free LLM token stream viewer and interceptor for the command line and the browser. It sits
> L29: **Who it's for:** anyone curious how language models pick their words, plus people doing LLM interpretability resea

## 星数曲线

```mermaid
xychart-beta
    title "Mattbusel/Every-Other-Token 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b2c6fd98a7ec` · [字段定义](../../DATASET.md)*
