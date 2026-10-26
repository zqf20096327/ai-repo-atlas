# GewoonJaap/gemini-cli-openai

⭐ 895 · TypeScript · 推送 2026-09-03 · [GitHub](https://github.com/GewoonJaap/gemini-cli-openai) · 个人维护

**将 Gemini CLI 接口转为 OpenAI 兼容 API 的 Cloudflare Worker**

部署在 Cloudflare Workers 上的代理服务：用 Gemini CLI 的 OAuth2 凭据（Google 账号登录，无需 API key）访问 Gemini 2.5 Pro/Flash/Flash-Lite 模型，并以 OpenAI 兼容端点形式对外提供，支持官方 OpenAI SDK、图像输入、函数调用、流式输出与 thinking 模式（含 reasoning_effort 控制）。配套 KV 命名空间做 token 缓存，提供与 Cline、Open WebUI、LiteLLM 等客户端的接入示例。限制：需自建 Google OAuth2 凭据与 Cloudflare 账号，未设置 OPENAI_API_KEY 时 API 公开可访问。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OAuth2 认证访问 Gemini，无需 API key，走 Code Assist 免费额度
- OpenAI 兼容端点，支持官方 OpenAI SDK 与 Open WebUI 等客户端
- 支持视觉、工具调用、流式输出与 thinking 预算/reasoning_effort 控制
- 限流时自动从 Pro 回退到 Flash 模型

## 适用场景

- 让 Cline、Open WebUI 等 OpenAI 兼容客户端直接调用 Gemini 模型
- 用已有 Google 账号 OAuth2 凭据替代付费 API key 访问 Gemini
- 在 Cloudflare 边缘节点自部署一个 OpenAI 格式的模型网关

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Transform Google's Gemini models into OpenAI-compatible endpoints using Cloudflare Workers. Access Google's most adv
> L10: - 🎯 **OpenAI-Compatible API** - Drop-in replacement for OpenAI endpoints
> L11: - 📚 **OpenAI SDK Support** - Works with official OpenAI SDKs and libraries

## 星数曲线

```mermaid
xychart-beta
    title "GewoonJaap/gemini-cli-openai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 894 --> 896
    line [895, 895]
```

2026-10-18 895 → 2026-10-26 895（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `65e0e087d1e8` · [字段定义](../../DATASET.md)*
