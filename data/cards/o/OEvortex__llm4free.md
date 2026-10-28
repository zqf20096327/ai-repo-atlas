# OEvortex/llm4free

⭐ 376 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/OEvortex/llm4free) · [官网](https://pypi.org/project/llm4free/) · 组织维护

**统一 OpenAI 接口聚合 40+ 免费/付费 AI 提供商的 Python 工具包**

原 WebScout 更名而来的 Python 工具包：以与 OpenAI SDK 一致的 chat.completions 接口聚合 40+ 聊天提供商（含 HeckAI、Pollinations 等免 key 免费层与 Groq、DeepInfra 等认证提供商），统一 Client 提供自动故障转移与模型解析。另含多引擎网络搜索（DDG/Bing/Brave 等）、文生图、文生语音、OpenAI 兼容 FastAPI 服务器、CLI 及 Scout 爬虫、GGUF 转换等开发者工具。pip/uv/Docker 安装，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40+ 提供商统一实现 OpenAI 兼容接口，一行切换
- 统一 Client 自动故障转移与模型解析（model="auto"）
- 本地 OpenAI 兼容 FastAPI 服务器（llm4free-server）
- 多引擎搜索、文生图、文生语音与 CLI、开发者工具箱

## 适用场景

- 不改代码在多个免费/付费 LLM 提供商之间切换并自动容灾
- 零 API key 快速接入可用的聊天模型
- 把各种提供商经标准 /v1 端点供官方 OpenAI SDK 调用
- 在同一工具包里做搜索、文生图、文生语音

## 场景标签

`模型网关` `网页抓取` `图像生成` `语音合成` · 领域:Agent 开发

## 证据(README 行号)

> L30: - 🔌 **One interface, 40+ providers.** Every chat provider implements `client.chat.completions.create(...)` — identi
> L35: - 🚀 **OpenAI-compatible server.** Serve any provider through standard `/v1` endpoints — point the official OpenAI S
> L181: All providers use the **OpenAI-compatible interface** (`client.chat.completions.create(...)`).

## 星数曲线

```mermaid
xychart-beta
    title "OEvortex/llm4free 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 374 --> 377
    line [375, 376, 376]
```

2026-10-18 375 → 2026-10-28 376（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `34f6baebbd86` · [字段定义](../../DATASET.md)*
