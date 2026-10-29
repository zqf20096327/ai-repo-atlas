# ariso-ai/ivan

⭐ 52 · TypeScript · 推送 2026-10-09 · [GitHub](https://github.com/ariso-ai/ivan) · 组织维护

**自主 AI 编码 agent：一句话任务变成已评审的 GitHub PR**

构建于 Claude Code 之上的命令行自主编码 agent：将自然语言任务拆解为 PR 规模的子任务，建分支、实现代码、生成规范化提交与 PR 描述并自动开 PR。Expert 模式下以架构师↔实现者双角色多轮评审设计稿与 diff。提供 institutional memory（ivan learn）从历史 PR 与本地 Claude Code 会话蒸馏经验存为 JSONL，并支持自动处理 PR 评审评论与失败 CI、通过 GitHub Actions 由 issue 触发。执行器可选 Claude SDK/Claude CLI/Codex CLI，需自备 API key 或订阅。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任务拆解→实现→提交→开 PR 的全自动工作流
- Expert 模式：只读架构师角色与实现者多轮设计/diff 评审
- ivan learn 将团队 PR 与会话蒸馏为可提交的经验库
- 自动处理 PR 评审评论与失败 CI，issue 评论可触发构建

## 适用场景

- 把一句话需求直接变成可评审的 pull request
- 让 agent 自动回复并修复 PR 上的评审意见
- 沉淀团队的评审经验并注入后续编码任务
- 通过 GitHub Actions 在 issue 上评论触发无人值守构建

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: Ivan is an open-source **autonomous AI coding agent** built on Claude Code that turns a plain-English task into a re
> L7: Give Ivan a sentence. Ivan breaks it into PR-sized tasks, **debates its own design with a principal-engineer persona
> L47: 1. 🗺️ **Break down** your request into manageable, PR-ready tasks

## 星数曲线

```mermaid
xychart-beta
    title "ariso-ai/ivan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-29 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2a62fe221ff2` · [字段定义](../../DATASET.md)*
