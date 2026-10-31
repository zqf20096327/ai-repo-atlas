# henkisdabro/cloudflare-workers-react-boilerplate

⭐ 13 · TypeScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/henkisdabro/cloudflare-workers-react-boilerplate) · [官网](https://henkisdabro.github.io/cloudflare-workers-react-boilerplate/) · 个人维护

**单人/小团队的全栈站点模板：React+API 部署在单个 Cloudflare Worker**

GitHub 模板仓库：将 Vite + React 19 + TypeScript 前端与 `/api/*` Worker 后端合并在单个 Cloudflare Worker 上，面向用 Claude Code 开发的个人或小团队，运行在 Workers 免费计划。内置 CI（lint/类型/测试/构建后部署）、D1 表单存储、KV 会话、密钥隐藏的 AI 调用示例，以及 `/start`、`/add-ai-feature` 等 Claude Code 斜杠命令和 Cloudflare MCP 连接。未内置登录，不适合长驻 Node.js 服务。

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

- 前端与 API 合并部署在单个 Cloudflare Worker，运行于免费计划
- CI 对每个 PR 验证并在 main 通过后自动部署
- AI 调用隐藏密钥、D1 表单、KV 会话的可运行示例
- 面向 Claude Code 的 AGENTS.md、斜杠命令与 Cloudflare MCP 服务器连接

## 适用场景

- 独立开发者快速上线带 AI 功能或表单存储的小型应用
- 需要客户端门户或内部仪表盘的小团队
- 在免费计划内完成 CI 与部署的 Cloudflare 全栈项目起步

## 场景标签

 · 领域:Web 开发/Serverless 模板

## 证据(README 行号)

> L18: a server. This GitHub template gives you one: a React app and its `/api/*` back end on a single
> L34: It is built for one person or a small team shipping an app with Claude Code: a paid AI tool, a

## 星数曲线

```mermaid
xychart-beta
    title "henkisdabro/cloudflare-workers-react-boilerplate 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `dc5d167e3725` · [字段定义](../../DATASET.md)*
