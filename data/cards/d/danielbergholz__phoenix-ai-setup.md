# danielbergholz/phoenix-ai-setup

⭐ 15 · Elixir · MIT · 推送 2026-09-29 · [GitHub](https://github.com/danielbergholz/phoenix-ai-setup) · 个人维护

**六步教程：让新 Phoenix 应用适配 AI 编程 agent 的工程约定**

一份面向 Elixir/Phoenix 开发者的设置指南（附 PROMPT.md 单提示词版与 templates/ 起始文件）：固定 Elixir/OTP 工具链版本、把 mix precommit 改造成含 Credo/Sobelow/技能镜像校验的验证门、将生成的 AGENTS.md 拆分为 .claude/skills 下按需加载的技能并镜像到 .agents/skills、为 Claude Code 配置 worktree 会话启动钩子与 autoPort。明确声明这是设置约定而非 agent 行为保证，文档审阅日期 2026-09-29。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 mix precommit 扩展为含 compile/credo/sobelow/test/skills.check 的验证门
- AGENTS.md 拆分为 5 个按需加载技能并留存根指针
- 符号链接镜像 .claude/skills 与 .agents/skills，precommit 校验镜像一致性
- 提供 PROMPT.md 整体粘贴给编程 agent 执行设置并报告验证证据

## 适用场景

- 新建 Phoenix 项目后让 AI 编程 agent 按约定可靠工作
- 为 Claude Code/Codex 等多 harness 共享同一套 agent 指令与技能
- 用 precommit 门禁防止 agent 指令与技能镜像漂移

## 场景标签

`教程课程` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: `mix phx.new` gives you a working Phoenix app and an `AGENTS.md` with framework guidance. Keep the useful rules, but
> L81: This is the step that actually changes how agents behave.

## 星数曲线

```mermaid
xychart-beta
    title "danielbergholz/phoenix-ai-setup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `22b07a9f80bb` · [字段定义](../../DATASET.md)*
