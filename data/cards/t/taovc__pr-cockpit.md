# taovc/pr-cockpit

⭐ 485 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/taovc/pr-cockpit) · 个人维护 · 中文 README

**本地 AI PR 审查工作台：用 Claude/Codex 批量审 PR，人工把关后发布**

面向开发者的桌面应用（Electron 打包 Nuxt 4）：通过 gh CLI 拉取仓库 PR 队列，让本地登录的 Claude 或 Codex 在只读隔离 git worktree 中执行审查，产出含严重级别、path:line、修复建议的结构化 findings；另有修复聊天、功能开发助手与技能生成。所有 GitHub 评论需逐条勾选确认才发布，写操作默认不提交推送。需 gh auth 登录与 Claude/Codex 登录；提供 macOS/Windows/Linux 桌面构建（nightly，未签名）或 Node≥22 + pnpm 9 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI 在隔离只读 git worktree 中审查，产出结构化 findings（严重级别/path:line/修复指引）
- 人工把关门控：逐条勾选才发布 GitHub 评论，预发布预览支持干跑
- 审查代理只读：工具级阻断 git 写、文件编辑、网络与危险命令
- 每项目独立选择 Claude 或 Codex 提供方、模型与审查方法论

## 适用场景

- 在本地批量审查整个仓库的 PR 队列而不逐个开终端
- 让 AI 修复 PR 问题并人工确认 diff 后再提交推送
- 在隔离分支里让项目助手开发新功能并创建 PR

## 场景标签

`代码审查` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3:  Review a repo's whole PR queue with Claude or Codex — locally.
> L8:  Providers: Claude and Codex
> L88: Nuxt 4 + @nuxt/ui (Tailwind v4) · better-sqlite3 + drizzle · `@anthropic-ai/claude-agent-sdk` · `@openai/codex-sdk`

## 星数曲线

```mermaid
xychart-beta
    title "taovc/pr-cockpit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 484 --> 490
    line [489, 485, 485]
```

2026-10-18 489 → 2026-10-28 485（-4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `45e8d77f7c5c` · [字段定义](../../DATASET.md)*
