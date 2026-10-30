# Temikus/butter

⭐ 16 · Go · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/Temikus/butter) · [官网](https://butterproxy.org/) · 个人维护

**Go 编写的 AI 代理网关：统一 OpenAI 兼容 API 接入多家供应商**

用 Go 实现的 AI 代理网关，部署在应用与 AI 供应商之间，提供统一的 OpenAI 兼容 API，支持 11 家供应商（OpenAI、Anthropic、AWS Bedrock、Azure OpenAI、Gemini、OpenRouter、Groq、Mistral、Together.ai、Fireworks、Perplexity），并做 Anthropic/Gemini 格式互转。功能包括多供应商路由与优先级/轮询策略、加权密钥轮换、自动故障转移与指数退避重试、响应缓存、配置热重载，以及通过 WASM 沙箱插件机制（Extism/wazero）扩展限流、请求日志、Prometheus 指标、分布式追踪和提示注入防护。通过 GitHub Releases 二进制或源码构建安装，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 家 AI 供应商的统一 OpenAI 兼容 API 与格式互转
- 多供应商路由、加权密钥轮换、自动故障转移与重试
- WASM 沙箱插件系统（Extism/wazero，零 CGo），内置限流/日志/指标/追踪/提示注入防护插件
- 应用密钥体系：按密钥用量追踪、撤销/轮换/过期与作用域限制

## 适用场景

- 在多个 AI 供应商之间做统一接入与故障转移
- 管理多把 API 密钥并按权重轮换与限额
- 通过插件对请求做提示注入防护、限流与审计
- 让现有 OpenAI SDK 客户端换 base URL 即切换后端

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: A blazingly fast AI proxy gateway written in Go. Butter sits between your application and AI providers, offering a u
> L12: Your App ──▶ Butter ──▶ OpenAI / Anthropic / Bedrock / Gemini / Groq / Mistral / ...
> L14:                 ├── Unified OpenAI-compatible API

## 星数曲线

```mermaid
xychart-beta
    title "Temikus/butter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4efe8cdb6065` · [字段定义](../../DATASET.md)*
