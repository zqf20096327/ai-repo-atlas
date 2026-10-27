# BuildingTechAlternatives/OpenThorn

⭐ 26 · TypeScript · 推送 2026-08-31 · [GitHub](https://github.com/BuildingTechAlternatives/OpenThorn) · [官网](https://www.openthorn.app) · 个人维护

**浏览器端 BYOK AI 建站工具：自带 API key 生成并部署网站**

免费开源的 BYOK（自带密钥）AI 应用构建平台：用户用自然语言描述需求，AI agent 生成完整代码，在浏览器内用 esbuild-wasm 实时预览，并一键部署到 Cloudflare Pages。平台本身免费，用户直接向 12 家 AI 提供商（OpenAI、Anthropic、Gemini、Ollama 等）按 token 付费，无订阅。API 密钥以 AES-256-GCM 加密存储，支持多提供商自动降级切换、实时协作与完整代码导出。自托管需 Node.js 20+、Supabase、Cloudflare 与 Vercel 账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BYOK 模式：接入 12 家 AI 提供商，用户直接向提供商付费
- 浏览器内 esbuild-wasm 实时预览，无服务器往返
- 一键部署 Cloudflare Pages，用户无需自有 Cloudflare 账号
- 提供商限流时 agent 自动切换并继续运行

## 适用场景

- 用自然语言生成并部署完整网站，不想付平台订阅费
- 已有 OpenAI/Anthropic 等 API key，按 token 直接付费建站
- 配合 Gemini/Groq 免费额度或本地 Ollama 以 $0 成本构建

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L8: OpenThorn is a BYOK (bring-your-own-key) AI app builder. Describe what you want in plain language; the AI agent writ
> L24: - **12 AI providers** — OpenAI, Anthropic, Google Gemini, DeepSeek, Mistral, Groq, xAI, Perplexity, OpenRouter, Oll

## 星数曲线

```mermaid
xychart-beta
    title "BuildingTechAlternatives/OpenThorn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a9daf8169c31` · [字段定义](../../DATASET.md)*
