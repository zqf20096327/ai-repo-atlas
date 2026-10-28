# KashifKhn/gemini-proxy

⭐ 51 · TypeScript · MIT · 推送 2026-03-09 · [GitHub](https://github.com/KashifKhn/gemini-proxy) · 个人维护

**自托管 OpenAI 兼容代理：用个人 Google 账号免费调用 Gemini**

用 Bun + Hono + TypeScript 实现的自托管 HTTP 代理：把 OpenAI 格式的 /v1/chat/completions 请求透明转发到 Google Cloud Code Assist 内部端点，认证采用 OAuth 2.0 + PKCE 浏览器登录（复用 Gemini CLI 公开凭据），无需付费 API key。支持 SSE 流式、function calling、多模态图像输入、自动令牌刷新与免费层 GCP 项目自动开通；PROXY_API_KEY 提供静态 Bearer 保护。README 明确声明使用内部端点存在违反 ToS 与账号被限制的风险，仅供个人与内部开发使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI wire 兼容，任何 OpenAI SDK/工具可直连 base_url 使用
- OAuth 2.0 + PKCE 浏览器登录，复用 Gemini CLI 凭据，无需付费 API key
- 支持 SSE 流式、function calling、base64 图像输入
- 首次登录自动开通免费层 GCP 托管项目，令牌自动刷新

## 适用场景

- 让仅支持 OpenAI API 的工具（如 Continue）调用 Gemini 模型
- 个人开发中不购买 API key 使用 Gemini 免费额度
- 本地统一入口管理 Gemini 调用并加 Bearer 鉴权

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A self-hosted, OpenAI-compatible HTTP proxy for Google Gemini AI — authenticated via **OAuth 2.0 + PKCE** using the 
> L5: Point any OpenAI SDK or tool at `http://localhost:3000` and it will transparently route requests through Google's Cl

## 星数曲线

```mermaid
xychart-beta
    title "KashifKhn/gemini-proxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-28 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6a7b67cd1d49` · [字段定义](../../DATASET.md)*
