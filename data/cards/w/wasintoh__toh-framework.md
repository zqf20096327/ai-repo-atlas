# wasintoh/toh-framework

⭐ 98 · JavaScript · MIT · 推送 2026-09-02 · [GitHub](https://github.com/wasintoh/toh-framework) · [官网](https://tohframework.dev) · 个人维护 · 中文 README

**向项目安装 AI 多 agent 构建体系的 npm 框架，一次批准自动完成应用**

通过 npx 安装的 AI 编排开发框架：向项目注入 14 个斜杠命令、8 个专职 agent 与 23 个技能，支持 Claude Code、Cursor、Antigravity、Codex、ZCode 五种 IDE/CLI。用户用自然语言下达一句指令并批准一次后，编排器生成 .toh/plan.md 复选框式计划，由各 agent 构建、测试、修复直到检查点验证通过；技术栈固定为 Next.js 16 + React 19 + Supabase + Playwright。面向独立开发者与小团队，提供安装/卸载/更新命令及跨 IDE 的计划恢复。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 个命令、8 个 agent、23 个技能一次安装，覆盖 5 种 IDE/CLI
- 计划以 .toh/plan.md 文件存在，跨会话与跨 IDE 自动恢复
- TOH LOOP：构建-测试-修复循环，检查点以命令退出码验证
- 按角色分层路由模型（haiku 测试 / sonnet 构建 / opus 规划）

## 适用场景

- 独立开发者用一句话从零搭建完整应用
- 在多个 AI IDE 之间切换时延续同一份构建计划
- 自动执行测试与修复循环直到应用验证完成

## 场景标签

`多智能体` `编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: **Toh Framework** installs an AI "build department" into your project: **14 slash commands, 8 specialist agents, an
> L20: **If you do write code:** it's a plan-as-file loop your agent cannot fake its way out of. The backlog lives in `.to
> L63: - 🤖 **AI handles everything** - Breaks down tasks, calls agents, executes until done

## 星数曲线

```mermaid
xychart-beta
    title "wasintoh/toh-framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-26 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3ca64b8b3004` · [字段定义](../../DATASET.md)*
