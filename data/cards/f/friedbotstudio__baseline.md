# friedbotstudio/baseline

⭐ 14 · JavaScript · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/friedbotstudio/baseline) · [官网](http://baseline.friedbotstudio.com/) · 组织维护

**Claude Code 的治理层：钩子拦截工具调用，三道人工同意门**

面向使用 Claude Code 的开发团队的开源治理覆盖层。通过 npx 脚手架向项目写入 27 个钩子（PreToolUse 等边界上以独立 Node 子进程运行，可拒绝违反宪则的工具调用）、59 个技能、1 个子代理、9 条工作流轨道与 3 道必须由用户亲手输入命令的同意门（含 /grant-push），使 Claude 无法自我批准或禁用钩子。层级契约由 seed.md 与 CLAUDE.md 承载。当前为公开 alpha，要求 Node 18.17+ 与 git，PlantUML 依赖 JDK 8+（可用 --no-plantuml 跳过）。Apache 2.0 许可，由 Friedbot Studio 维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 27 个钩子在工具边界以外部子进程运行并拒绝违规调用
- 3 道用户亲手输入的同意门，Claude 无法伪造同意标记
- intake 到 commit 的 11 阶段流水线，由 track_guard 强制顺序
- audit-baseline 在每次构建时核对组件清单，漂移导致 CI 失败

## 适用场景

- 让 AI 编码代理在团队规则约束下工作，禁止自行推送或自我批准
- 为代码库建立从需求 intake 到 commit 的可审计工作流
- 控制 Claude Code 在受保护分支上的 git push 操作

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: An open-source governance layer for Claude Code. Hooks fire at every tool boundary and refuse a call that breaks the
> L33: A repository overlay. It installs **27 hooks** at Claude's tool boundaries, **59 skills**, **1 subagent**, **9 work

## 星数曲线

```mermaid
xychart-beta
    title "friedbotstudio/baseline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `59e5603906ba` · [字段定义](../../DATASET.md)*
