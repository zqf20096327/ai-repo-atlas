# 10/chatgpt-codex-proxy

⭐ 17 · Go · MIT · 推送 2026-10-24 · [GitHub](https://github.com/10/chatgpt-codex-proxy) · 个人维护

**把 ChatGPT Codex 私有接口包装成 OpenAI/Anthropic 兼容 API 的代理**

用 Go 编写的本地代理服务，暴露 OpenAI（Chat Completions、Responses、Images）与 Anthropic Messages 两套 API 端点，将请求翻译为 chatgpt.com/backend-api/codex/* 私有格式，并在多个已登录 Codex 账号间路由（least-used/round-robin/sticky，带冷却与配额感知）。账号通过设备登录 OAuth 流程添加。面向开发者，供任何 OpenAI 或 Anthropic 客户端接入自有 Codex 账号。限制：上游为私有未文档化接口，可能随时变更；面向本地与小规模使用；音频输入被拒绝。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同时提供 OpenAI 与 Anthropic 两套 API 表面，单一 Codex 后端
- 多账号轮换（least-used/round-robin/sticky）与配额/冷却感知
- 设备登录添加账号，无需抓取 cookie 或粘贴 token
- 支持 SSE 流式、Responses 的持久 WebSocket、工具调用与结构化输出

## 适用场景

- 让任意 OpenAI/Anthropic 客户端复用自己的 ChatGPT Codex 账号
- 在多个 Codex 账号间做配额与负载轮换
- 本地或小规模环境统一暴露标准 API 端点

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L17: Exposes OpenAI and Anthropic endpoints, translates each request into the private
> L63: Point any OpenAI client at `http://localhost:8080/v1` using `PROXY_API_KEY` as

## 星数曲线

```mermaid
xychart-beta
    title "10/chatgpt-codex-proxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `75af49822e93` · [字段定义](../../DATASET.md)*
