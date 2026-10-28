# zxcloli666/AI-Worker-Proxy

⭐ 106 · TypeScript · MIT · 推送 2026-09-18 · [GitHub](https://github.com/zxcloli666/AI-Worker-Proxy) · 个人维护

**跑在 Cloudflare Workers 上的 OpenAI 兼容免费 AI 网关**

部署到 Cloudflare Workers（免费层每日 10 万请求）的 AI 代理网关：接收 OpenAI 格式请求，路由到 OpenAI、Anthropic、Google 或 Cloudflare Workers AI 等后端，支持多 API key 轮换、故障自动切换，并原生支持 Anthropic Messages API 格式（含跨格式自动转换）。安装通过 Fork 仓库+GitHub Secrets+Actions 工作流部署，路由逻辑经 GitHub Variables 配置无需改代码，也支持添加任意 OpenAI/Anthropic 兼容的第三方供应商。面向不写代码即可自助部署的开发者/使用者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 与 Anthropic Messages 双 API 格式支持，跨供应商自动格式转换
- 多 key 轮换与故障自动切换
- 路由配置经 GitHub Variables 下发，无需改代码（单变量上限 48 kB，可分段至 9 个）
- 运行于 Cloudflare 免费层，$0 成本

## 适用场景

- 让只支持 OpenAI API 的应用接入 Claude/Gemini 等模型
- 聚合多个 API key 轮换使用，规避速率限制
- 单一入口做多供应商故障切换

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: This is a **Free AI Gateway** that runs on Cloudflare Workers. It acts as a middleman: you send it an OpenAI-style r
> L18: * **One API to Rule Them All:** Talk to Anthropic Claude 3.5, Google Gemini 2.0, and GPT-4o using the exact same co

## 星数曲线

```mermaid
xychart-beta
    title "zxcloli666/AI-Worker-Proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-28 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5fbbd537148a` · [字段定义](../../DATASET.md)*
