# schalkneethling/skills-autoresearch-flue

⭐ 15 · TypeScript · MIT · 推送 2026-09-19 · [GitHub](https://github.com/schalkneethling/skills-autoresearch-flue) · 个人维护

**基于 Flue 的 agent 技能自动研究评测框架（alpha）**

构建于 Flue 之上的技能自动研究 harness：将种子技能在项目 fixture 上评测，交由研究员模型改进，再对候选技能重跑评测。模型评测路径分三个角色：Researcher（claude-sonnet-4-6）改进技能、Producer（claude-haiku-4-5）运行技能产出评测文件、Judge（claude-sonnet-4-6）仅对产出打分，以避免自我评分。支持无凭据的确定性报告路径（--response-file）、append-only 运行日志与 smoke/research/determinize 命令，自带 release-notes alpha fixture。项目自述为 alpha 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Researcher/Producer/Judge 三角色分离，按职责分配不同大小的模型
- determinize report 支持凭据无关的确定性运行（--response-file）
- append-only 运行日志记录事件、结果与错误
- 自带 release-notes-alpha fixture（种子技能、评测用例、基线工作区）

## 适用场景

- 对自有 agent 技能跑自动化评测与迭代改进
- 在固定 fixture 上对比候选技能与基线的表现
- 以确定性回放方式检查研究报告

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: An alpha skills autoresearch harness built on Flue.
> L5: The harness evaluates a seed skill against project fixtures, asks a researcher model to improve the skill, then reru
> L19: 1. **Researcher** (`claude-sonnet-4-6`): improves the candidate skill.

## 星数曲线

```mermaid
xychart-beta
    title "schalkneethling/skills-autoresearch-flue 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b6312ad86927` · [字段定义](../../DATASET.md)*
