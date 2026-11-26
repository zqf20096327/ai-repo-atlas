# TsinHzl/kiro2cc-proxy

⭐ 365 · Rust · MIT · 推送 2026-11-25 · [GitHub](https://github.com/TsinHzl/kiro2cc-proxy) · 个人维护 · 中文 README

**把 Kiro 账号代理为 Claude API 供 Claude Code/Codex 使用的服务**

Rust 编写的代理服务，将 Anthropic Claude API 请求转换为 Kiro API 请求，使 Kiro 账号中的模型可在 Claude Code 或 Codex CLI 中调用，而非仅限 Kiro IDE/CLI 使用。提供 Anthropic API 兼容端点与 OpenAI 兼容端点、SSE 流式输出、prefix cache、Token 自动刷新、多账号故障转移与负载均衡、Admin Web 管理面板。部署方式包括预编译包、macOS/Windows 本地构建、Docker Compose 预构建镜像、systemd。国内使用需配置本地 HTTP/SOCKS5 代理。

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

- Anthropic API 与 OpenAI API 兼容端点，可接入 Claude Code 与 Codex CLI
- 多账号优先级故障转移与 balanced 负载均衡，Token 自动刷新
- 支持 SSE 流式输出、prefix cache、extended thinking 与 function calling
- 提供 Admin Web 面板管理账号、余额查询与 API Key

## 适用场景

- 用 Claude Code 调用 Kiro 账号中的模型
- 通过 OpenAI 兼容端点把 Kiro 模型接入任意 SDK 客户端
- 多账号场景下做负载均衡与自动故障转移
- 在服务器上用 Docker 部署代理并统一管理账号

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **将 Anthropic Claude API 请求转换为 Kiro API 请求的 Rust 代理服务**
> L44: kiro2cc-proxy 是一个代理服务。它把标准的 Anthropic Claude API 请求转发给 Kiro（AWS 的 AI 编程工具），让你可以用 Claude Code使用Kiro账号的模型。
> L27: |**🔌 Anthropic API 兼容**|完整支持 Anthropic Claude API 格式|

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
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `ce8f10ba9800` · [字段定义](../../DATASET.md)*
