# seaavey/SRouter

⭐ 23 · Rust · MIT · 推送 2026-10-25 · [GitHub](https://github.com/seaavey/SRouter) · [官网](https://srouter.web.id) · 个人维护

**Rust 自托管 LLM 网关：一个端点聚合多供应商 OAuth 账号**

用 Rust/Axum 编写的自托管 LLM 网关，同时提供 OpenAI 与 Anthropic 兼容端点，供 Claude Code、Cursor、Cline、OpenAI SDK 等客户端指向单一 base URL。内置九个驱动覆盖 OpenCode Zen、Qoder、Cline、Grok Web、Codex、CodeBuddy、Antigravity、Claude Code，各自维护 OAuth 流程与 token 刷新。网关密钥带独立限流、配额与模型白名单；每条请求记录到 SQLite（不含正文）并在 React 仪表盘展示。单二进制 + SQLite，Docker Compose 一条命令安装；PostgreSQL 被拒绝，SQLite 是唯一后端。

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

- 同时暴露 /v1/chat/completions（OpenAI）与 /v1/messages（Anthropic）两套协议
- 九个供应商驱动，各自管理 OAuth 登录与 token 刷新
- 网关密钥独立于供应商凭据，支持限流窗口、token 配额、额度与模型白名单
- 请求日志（供应商/模型/token/延迟/成本）存 SQLite，仪表盘经 SSE 实时图表展示

## 适用场景

- 让 Claude Code、Cursor、Cline 等多个客户端共用一个网关端点
- 聚合已订阅的多个 LLM 账号做配额池与故障转移
- 通过仪表盘查看用量、配额与各模型花费

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **One self-hosted endpoint for the LLM accounts you already pay for.** SRouter is an LLM gateway that speaks both th
> L19: - **One endpoint, two protocols.** `/v1/chat/completions` for OpenAI-shaped clients and `/v1/messages` for Anthropi
> L20: - **The accounts you already have.** Nine drivers cover OpenCode Zen (free tier), Qoder, Cline, Grok Web, OpenAI Co

## 星数曲线

```mermaid
xychart-beta
    title "seaavey/SRouter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `15585af6d7b6` · [字段定义](../../DATASET.md)*
