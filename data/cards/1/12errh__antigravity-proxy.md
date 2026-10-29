# 12errh/antigravity-proxy

⭐ 41 · TypeScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/12errh/antigravity-proxy) · 个人维护

**让 Antigravity 2.0 使用任意 AI 提供商的 TypeScript 代理**

面向 Antigravity 2.0 Desktop 用户的本地代理：在 443 端口拦截 Gemini API 调用，将请求转换并路由到 NVIDIA、OpenRouter、OpenAI、Groq、Anthropic、Google Gemini 等云端 API，或自动发现的 Ollama、vLLM、LM Studio、llama.cpp 等 9+ 本地推理方案。提供多提供商故障转移、按模型路由、成本统计与实时仪表盘。以 npm 全局包安装，需 Node.js 20+ 与管理员权限绑定 443 端口。

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

- TLS 拦截 Antigravity 的 Gemini API 调用并转换为目标提供商格式
- 支持 8 个云端 API 与 9+ 自动发现的本地推理方案
- 多提供商故障转移、按模型路由与重试退避
- 实时仪表盘：日志、成本统计（按天/模型/提供商）、配置热加载

## 适用场景

- 让 Antigravity 使用 OpenRouter/NVIDIA 等云端模型替代 Gemini
- 在 Antigravity 中接入 Ollama、vLLM 等本地推理方案
- 跨多个提供商配置故障转移与成本跟踪

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7:  Use any AI provider with Antigravity 2.0 — NVIDIA, OpenRouter, OpenAI, Groq, Anthropic, Google Gemini, OpenCode Zen
> L155: 1. **TLS Intercept** — Receives Gemini API call on port 443
> L161: 7. **Translation** — Converts to target provider's API format

## 星数曲线

```mermaid
xychart-beta
    title "12errh/antigravity-proxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-29 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8cb40cd270d9` · [字段定义](../../DATASET.md)*
