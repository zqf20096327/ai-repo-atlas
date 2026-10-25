# mydisha/keirouter

⭐ 154 · Go · MIT · 推送 2026-10-20 · [GitHub](https://github.com/mydisha/keirouter) · [官网](https://keirouter.app) · 个人维护

**面向 AI 编码工具的自托管 AI 网关：统一接入、路由与成本管控**

用 Go 编写的自托管 AI 网关，供使用 Claude Code、Codex、Cursor 等编码工具的开发者将各类工具指向一个本地端点。功能包括多协议翻译（OpenAI Chat/Responses、Anthropic Messages、原生 Gemini）、带优先级/轮询/延迟/成本排序的故障转移链、响应缓存、提示压缩等五类 token 节省、按 key 的预算与限流、安全护栏（PII/注入/毒性检测）、审计日志与 Prometheus 指标。原生支持 AWS Bedrock、Azure、watsonx 等企业云。提供 Homebrew、Shell/PowerShell 脚本、Docker Compose 安装及预编译单二进制，自带 Web 仪表盘。README 标注项目处于活跃开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单端点翻译 OpenAI/Anthropic/Gemini 协议并按策略路由与故障转移
- 五类 token 节省、按 key 预算硬上限与 RPM/TPM/并发限流
- 护栏（PII/注入/毒性等）与哈希链审计日志、OpenTelemetry 导出
- 原生接入 AWS Bedrock、SageMaker、Azure AI Foundry 等企业云并处理其认证

## 适用场景

- 把多个 AI 编码工具的 API key 收敛到一个本地网关统一管理
- 上游服务商限流或宕机时自动故障转移，保持编码不中断
- 按 key 设预算与限流，控制团队 token 支出
- 在 VPS 上自部署网关并接入企业云模型

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L18: **KeiRouter is the smart middleman that makes all of that someone else's problem.** Point your tools at one local e
> L38: - 🔀 **One endpoint, every provider** — Your apps speak OpenAI Chat, the OpenAI Responses API, Anthropic Messages, o
> L40: - 🏢 **Enterprise clouds, natively** — AWS Bedrock, SageMaker, Azure AI Foundry, IBM watsonx.ai, Oracle Cloud, SAP G

## 星数曲线

```mermaid
xychart-beta
    title "mydisha/keirouter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 150 --> 155
    line [151, 153, 154]
```

2026-10-18 151 → 2026-10-25 154（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `3cb9ad54802d` · [字段定义](../../DATASET.md)*
