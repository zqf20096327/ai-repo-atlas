# whtsky/copilot2api

⭐ 36 · Go · MIT · 推送 2026-08-21 · [GitHub](https://github.com/whtsky/copilot2api) · 个人维护

**把 GitHub Copilot 代理为 OpenAI/Anthropic/Gemini 兼容 API 的 Go 代理**

用 Go 编写的本地代理：通过 GitHub Device Flow OAuth 认证并自动刷新 Copilot API token，将 GitHub Copilot 暴露为 OpenAI、Anthropic、Gemini 与 AmpCode 兼容的 API 端点，支持 SSE 流式输出、embeddings、模型缓存与配额查询（/usage）。提供 Docker、docker compose 与多平台预编译二进制安装；README 声明仅面向本地开发，不实现 API key 校验，公开暴露会消耗 Copilot 配额。附带 Claude Code、Codex、Gemini CLI、AmpCode 等客户端接入示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI/Anthropic/Gemini/AmpCode 四种兼容 API 端点，含流式与 embeddings
- GitHub Device Flow OAuth 认证与 token 自动刷新
- 内置 /usage 配额查询与 5 分钟模型列表缓存
- 可配置的精确匹配模型路由（默认 codex-auto-review → gpt-5.6-luna）

## 适用场景

- 用 Claude Code/Codex/Gemini CLI 等客户端接入自己的 Copilot 订阅
- 让仅支持 OpenAI/Anthropic SDK 的工具复用 Copilot 额度
- 本地查看 Copilot 使用量与配额

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: A lightweight Go proxy that exposes GitHub Copilot as OpenAI-compatible, Anthropic-compatible, Gemini-compatible, an
> L224: 4. Proxies OpenAI-format requests directly to Copilot API

## 星数曲线

```mermaid
xychart-beta
    title "whtsky/copilot2api 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 34 --> 38
    line [35, 37, 36]
```

2026-10-18 35 → 2026-10-28 36（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6a1e9df1bc32` · [字段定义](../../DATASET.md)*
