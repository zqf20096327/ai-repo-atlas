# alexandephilia/kiro-claude-proxy

⭐ 27 · Go · 推送 2026-03-11 · [GitHub](https://github.com/alexandephilia/kiro-claude-proxy) · 个人维护

**Go 本地代理：用 Kiro/AWS 凭证让 Claude Code 免 Anthropic 计费后端运行**

单文件 Go CLI（kirolink）读取本地 ~/.aws/sso/cache/kiro-auth-token.json 的 Kiro SSO 令牌，在本地 8080 端口暴露 Anthropic 兼容 API（POST /v1/messages、GET /v1/models、GET /health），将请求翻译为 AWS CodeWhisperer 的 generateAssistantResponse 调用并翻译回 Anthropic 风格 JSON/SSE。提供 read/refresh/export/claude/server 五个子命令，export 输出 ANTHROPIC_* 环境变量，claude 命令修改 ~/.claude.json。面向已登录 Kiro 的 Claude Code / OpenClaw 用户。限制：依赖已存在的 Kiro 令牌文件，上游端点与导出地址均硬编码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 读取 Kiro SSO 缓存令牌并在本地暴露 Anthropic 兼容 API
- 请求/响应双向翻译至 AWS CodeWhisperer 后端，支持 SSE 流式与 Tool Use
- 提供 read/refresh/export/claude/server 五个子命令
- export 输出 ANTHROPIC_* 环境变量供客户端直接使用

## 适用场景

- 让 Claude Code 等 Anthropic 兼容客户端走 Kiro/AWS 凭证而非 Anthropic 原生计费
- 为 OpenClaw 添加自定义 Claude provider
- 刷新并管理本地 Kiro 令牌

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L22: `kirolink` is a small Go CLI that reads Kiro auth tokens from your local SSO cache, then exposes an Anthropic-shape
> L24: In practice: your client sends `POST /v1/messages` to this proxy, the proxy translates the request to AWS CodeWhisp
> L156: 4. Send them to `https://codewhisperer.us-east-1.amazonaws.com/generateAssistantResponse`.

## 星数曲线

```mermaid
xychart-beta
    title "alexandephilia/kiro-claude-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `291f7b90bd1f` · [字段定义](../../DATASET.md)*
