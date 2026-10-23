# Mirrowel/LLM-API-Key-Proxy

⭐ 558 · Python · NOASSERTION · 推送 2026-09-23 · [GitHub](https://github.com/Mirrowel/LLM-API-Key-Proxy) · 个人维护

**自托管通用 LLM 代理：统一 OpenAI/Anthropic 兼容端点与密钥轮换**

由 FastAPI 实现的自托管代理，提供 OpenAI（/v1/chat/completions）与 Anthropic（/v1/messages）兼容端点，将请求路由到 Gemini、OpenAI、Anthropic、OpenRouter 等已配置的 provider，模型以 provider/model_name 格式指定。内置密钥轮换、错误自动切换、按模型的递增冷却（10s→120s）与每 provider 并发控制，配套可复用的 Python 韧性库（rotator_library）、交互式 TUI 与凭据管理工具。面向希望让 Claude Code、Cursor、SillyTavern 等客户端零代码接入多 provider 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI/Anthropic 双格式兼容端点，客户端零代码接入
- API 密钥自动轮换、故障切换与递增冷却机制
- 通过 LiteLLM 支持多 provider，含 Gemini CLI OAuth 等专属 provider
- 可独立复用的密钥管理 Python 库 rotator_library

## 适用场景

- 让 Claude Code 等只支持 Anthropic API 的工具改用 Gemini/OpenAI 模型
- 多个 API key 聚合为一个端点并做负载均衡与故障切换
- 自建 LLM 网关统一管理凭据、用量与并发限额

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: A self-hosted proxy that provides OpenAI and Anthropic compatible API endpoints for all your LLM providers. Works wi
> L11: 1. **The API Proxy** — A FastAPI application providing universal `/v1/chat/completions` (OpenAI) and `/v1/messages`
> L17: - **One Endpoint, Many Providers** — Configure Gemini, OpenAI, Anthropic, and any LiteLLM-supported provider once. 

## 星数曲线

```mermaid
xychart-beta
    title "Mirrowel/LLM-API-Key-Proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 557 --> 559
    line [558, 558]
```

2026-10-18 558 → 2026-10-23 558（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `f5b2afac9525` · [字段定义](../../DATASET.md)*
