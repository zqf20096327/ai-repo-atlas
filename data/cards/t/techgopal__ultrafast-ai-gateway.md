# techgopal/ultrafast-ai-gateway

⭐ 21 · Rust · MIT · 推送 2026-10-24 · [GitHub](https://github.com/techgopal/ultrafast-ai-gateway) · 个人维护

**自托管 LLM API 网关：单 Rust 二进制提供路由、限额与控制台**

用单个 Rust 二进制实现的 LLM 网关，位于应用与模型提供商之间：兼容 OpenAI 与 Anthropic API 格式，支持 Gemini、Azure OpenAI 及任意 OpenAI 兼容后端（Groq/Mistral/OpenRouter/Ollama 等）。提供加权路由与故障转移、重试、熔断、请求/令牌/并发限流、预算与告警、虚拟密钥与团队权限、护栏（关键词/正则/PII）、MCP 网关及内置 Web 控制台，存储用 SQLite（可切 PostgreSQL）。面向自托管的小团队，通过 Docker 或预编译二进制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 兼容 OpenAI/Anthropic API，跨格式翻译工具调用与编码代理请求
- 加权路由、有序故障转移、熔断、单飞缓存与响应缓存
- 虚拟密钥、团队/用户/密钥级限流与预算，凭据静态加密
- 内置控制台、Prometheus 指标、OpenTelemetry 追踪与 MCP 网关

## 适用场景

- 小团队统一接入多家模型提供商并做密钥管理
- 按团队和密钥控制模型用量、花费与权限
- 为 Claude Code / Codex 等编码代理提供带故障转移的代理入口

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: Ultrafast is one small Rust binary that sits between your apps and your LLM
> L10: providers. It speaks the OpenAI and Anthropic APIs, adds an admin API, and
> L42: - **Providers.** OpenAI, Anthropic, Gemini, Azure OpenAI, and any

## 星数曲线

```mermaid
xychart-beta
    title "techgopal/ultrafast-ai-gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ee02c548a5fb` · [字段定义](../../DATASET.md)*
