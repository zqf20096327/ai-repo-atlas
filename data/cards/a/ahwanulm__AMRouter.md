# ahwanulm/AMRouter

⭐ 15 · JavaScript · MIT · 推送 2026-08-12 · [GitHub](https://github.com/ahwanulm/AMRouter) · 个人维护

**自托管 AI 网关：单一端点代理多家 AI 提供商并自动故障转移**

Express 后端 + Vite/React 前端的自托管 AI 网关，对外暴露 OpenAI 兼容 REST API，将请求代理到 Cloudflare Workers AI、OpenAI、Anthropic、Gemini、Groq 等数十家提供商，支持负载均衡、自动回退与密钥轮换。含暗色仪表盘管理提供商/连接/代理池、OIDC 或密码登录、SQLite 本地存储。另含基于 Playwright + 2Captcha + Ammail 临时邮箱的 Cloudflare Workers AI 账号注册自动化模块，以及供 AI 编码代理使用的 SKILL.md 技能集。需 Node.js 20+，自动化功能另需 Python 3.10+ 与 Chromium。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 REST API，覆盖聊天/图像/语音/嵌入/搜索端点
- 多提供商路由：负载均衡、自动回退、密钥轮换
- Cloudflare Workers AI 账号注册与取 key 自动化（Playwright + 2Captcha + Ammail）
- 面向 Claude/Gemini/Codex 等 AI 编码代理的 SKILL.md 技能

## 适用场景

- 统一多个 AI 提供商为单一 OpenAI 兼容端点供客户端调用
- 在提供商故障或配额耗尽时自动切换保证可用性
- 通过仪表盘集中管理提供商、连接与代理池

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: 9Router v2 is a decoupled rewrite of 9Router with a clean separation between a dedicated **Express backend** and a *
> L15: - **OpenAI-compatible API** — works with any client that supports `/v1/chat/completions`, `/v1/images/generations`,

## 星数曲线

```mermaid
xychart-beta
    title "ahwanulm/AMRouter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `15d3add47c47` · [字段定义](../../DATASET.md)*
