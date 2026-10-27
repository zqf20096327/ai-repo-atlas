# hanlulong/econ-paper-review-skill

⭐ 32 · Python · NOASSERTION · 推送 2026-09-01 · [GitHub](https://github.com/hanlulong/econ-paper-review-skill) · [官网](https://openecon.ai) · 个人维护 · 中文 README

**经济学论文的 AI 预审稿技能：在真实审稿人之前生成审稿报告与修改计划**

面向 Claude Code 与 Codex 的 Agent Skill（econ-review）：读取经济学论文（PDF 及 LaTeX/Markdown 源），先重构论文的论证与证据结构，再逐项核查识别策略、表格、证明、数字、参考文献与写作，输出排版好的审稿报告 PDF、Markdown 报告与可交给 agent 执行的修改计划；评论经来源比对与自我反驳筛选，最多保留 100 条实质评论与 30 条编辑评论。也适用于金融、会计、政治经济学等社会科学论文。需要 Python 3.10+，PDF 摄取需 Poppler；PolyForm Noncommercial 许可，非商业用途免费。完整审稿常需 30 分钟以上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 生成审稿报告 PDF + 逐条评论 + 面向 agent 的优先级修改计划（最多 100+30 条）
- 评论经来源核对与自我反驳筛选，无法核查之处明确说明
- 支持 quick/full 两种模式，覆盖实证、理论、结构、宏观等各类论文
- 可选本地 Review Desk 网页端逐条裁决评论，多轮审稿-修改-复查

## 适用场景

- 投稿前让 AI 模拟期刊审稿人找出论文问题
- 把修改计划交给自己的 agent 逐项执行修订
- 金融、会计等实证社会科学论文的提交前自查

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L19: `econ-review` is an Agent Skill for Claude Code and Codex. It reads your paper the way a careful journal referee wo
> L21: *Built for economics. Also works well for finance, accounting, political economy, and other social science papers t

## 星数曲线

```mermaid
xychart-beta
    title "hanlulong/econ-paper-review-skill 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24", "2026-10-27"]
    y-axis "stars" 27 --> 33
    line [28, 29, 31, 32]
```

2026-10-18 28 → 2026-10-27 32（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5a94674b8398` · [字段定义](../../DATASET.md)*
