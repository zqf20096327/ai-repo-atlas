# TsinHzl/kiro2cc-proxy

⭐ 365 · Rust · MIT · 推送 2026-11-25 · [GitHub](https://github.com/TsinHzl/kiro2cc-proxy) · 个人维护 · 中文 README

**把 Kiro 账号代理为 Anthropic/OpenAI 兼容 API 供 Claude Code 与 Codex 使用**

用 Rust 编写的代理服务：将 Anthropic Claude API 格式请求转换为 Kiro（AWS 的 AI 编程工具）API 请求，并提供 /v1/chat/completions 与 /v1/responses 端点接入 Codex CLI 及 OpenAI SDK 客户端。功能包括 SSE 流式输出、前缀缓存、Token 自动刷新、多账号故障转移与负载均衡、智能重试、WebSearch 工具转换、extended thinking、function calling，以及可选的 Web 管理面板。提供预编译包、源码构建、Docker Compose、systemd 等部署方式；国内用户需配置本地 HTTP/SOCKS5 代理，否则 Claude 模型请求返回错误。README 声明仅供研究使用，与 AWS/Kiro/Anthropic 官方无关。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Anthropic API 与 OpenAI 兼容端点（/v1/chat/completions、/v1/responses）
- 多账号优先级/均衡负载均衡与自动故障转移、Token 自动刷新
- SSE 流式输出与前缀缓存
- 可选 Web 管理面板：账号管理、余额查询、API Key 创建

## 适用场景

- 用 Claude Code 通过 Kiro 账号调用其支持的模型
- 将 Kiro 账号接入 Codex CLI 或任意 OpenAI SDK 客户端
- 本地或服务器上自托管多账号 API 代理服务

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **将 Anthropic Claude API 请求转换为 Kiro API 请求的 Rust 代理服务**
> L27: |**🔌 Anthropic API 兼容**|完整支持 Anthropic Claude API 格式|
> L44: kiro2cc-proxy 是一个代理服务。它把标准的 Anthropic Claude API 请求转发给 Kiro（AWS 的 AI 编程工具），让你可以用 Claude Code使用Kiro账号的模型。

## 星数曲线

```mermaid
xychart-beta
    title "TsinHzl/kiro2cc-proxy 星数(近 7 点)"
    x-axis ["2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-26"]
    y-axis "stars" 354 --> 366
    line [355, 356, 357, 358, 360, 361, 365]
```

2026-11-18 355 → 2026-11-26 365（+10）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `00bf11fb3d39` · [字段定义](../../DATASET.md)*
