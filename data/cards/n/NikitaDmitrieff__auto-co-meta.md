# NikitaDmitrieff/auto-co-meta

⭐ 51 · TypeScript · MIT · 推送 2026-06-14 · [GitHub](https://github.com/NikitaDmitrieff/auto-co-meta) · [官网](https://runautoco.com) · 个人维护

**终端运行的自主 AI 公司：bash 循环驱动 14 个 agent 全天候开发部署软件**

以约 50 行核心 bash 循环每 2 分钟调用一次 Claude Code，组成 14 个角色 agent（CEO、CTO、工程师、QA 等）的公司化协作流程，从选品、写码到部署 24/7 自主循环运行。状态存于 markdown 文件与 git，无数据库和服务端，唯一依赖为 Claude Code。提供 npx 脚手架与三类项目模板（saas/docs-site/api-backend），通过 Makefile 启动与监控，含 Telegram 升级通知与不可覆盖的安全硬限制。成本约 $1.80/循环（Opus）。

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

- bash 循环驱动 Claude Code，状态存 markdown 文件，重启可恢复
- 14 个角色 agent 定义于 .claude/agents/ 可编辑
- npx create-auto-co 脚手架 + saas/docs-site/api-backend 模板
- 不可覆盖的安全硬限制（禁止删库、未经批准支出等）

## 适用场景

- 让 AI agent 团队自主从想法迭代到部署 MVP
- 独立开发者低成本运行自动化软件开发循环
- 观察/调整 agent 角色定义定制协作行为

## 场景标签

`Agent 框架` `多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L14: A bash loop that calls Claude Code every 2 minutes. 14 AI agents (CEO, CTO, Engineer, Designer, QA, Marketing...) d
> L16: It's not a chatbot. It's not a framework. It's **~50 lines of bash** that turn Claude Code into a self-running comp
> L22: State lives in markdown files. Everything survives restarts. The only dependency is Claude Code.

## 星数曲线

```mermaid
xychart-beta
    title "NikitaDmitrieff/auto-co-meta 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-28 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4c95b8d3da16` · [字段定义](../../DATASET.md)*
