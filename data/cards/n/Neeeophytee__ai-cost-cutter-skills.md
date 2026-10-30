# Neeeophytee/ai-cost-cutter-skills

⭐ 19 · JavaScript · NOASSERTION · 推送 2026-07-13 · [GitHub](https://github.com/Neeeophytee/ai-cost-cutter-skills) · [官网](https://flowstacks.xyz/) · 个人维护

**10 个为编码 agent 降 AI 开销的可安装技能，带 CI 验证**

面向 Claude Code、Codex、Cursor 等 SKILL.md 格式 agent 的技能集合，把 10 种降成本模式（路由切换、顾问调用预算、上下文瘦身、免费额度批量规划等）转化为 agent 可执行的过程，每个技能附 runnable proof block，由仓库 CI 在每次推送和每周定时执行验证。技能源自 FlowStacks 语料库，其中确定性部分（配置/模式/算术）由 CI 复查，模型质量部分明确标注需自测。提供 npx skills CLI、Claude Code 插件市场与手动复制三种安装方式，另有单文件 CLAUDE.md/AGENTS.md 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个技能覆盖路由、token、免费额度、证据对比等降本维度
- 每个技能附 proof block，CI 每次推送与每周定时执行
- 兼容 agentskills.io SKILL.md 格式，适配多款编码 agent
- 提供单文件 CLAUDE.md/AGENTS.md 被动指导版本

## 适用场景

- 给编码 agent 安装降本技能以压缩 AI 账单
- 先用 token-receipts-audit 弄清账单构成再选策略
- 对比便宜模型与昂贵模型在自己任务上的表现

## 场景标签

 · 领域:AI 成本优化/agent 技能

## 证据(README 行号)

> L5: **10 installable skills that cut your AI bill with proof instead of vibes. Free, MIT.**
> L11: Works in Claude Code, OpenAI Codex, Cursor, and any agent that reads the agentskills.io SKILL.md format.

## 星数曲线

```mermaid
xychart-beta
    title "Neeeophytee/ai-cost-cutter-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `fb99a1d8484b` · [字段定义](../../DATASET.md)*
