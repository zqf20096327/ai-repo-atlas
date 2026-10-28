# ElliotJLT/Claude-Skill-Potions

⭐ 62 · Python · MIT · 推送 2026-02-12 · [GitHub](https://github.com/ElliotJLT/Claude-Skill-Potions) · 个人维护

**Claude Code 可复用技能集：以 Markdown 技能优化开发工作流**

面向 Claude Code 用户的技能（Potions）集合：以纯 Markdown 文件定义触发式工作流，覆盖规划风险、上下文管理、调试、质量验证、代码纪律、复盘等 20 余个技能；可链接多个技能组成编排型 Elixir；另含 meta 技能用于生成与改进技能本身。安装方式为 git clone 到 ~/.claude/skills 或项目目录，通过追加到 CLAUDE.md 与可选 hook 提升激活率（宣称约 20% 提升至约 84%）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20+ 个触发式 Markdown 技能，覆盖规划/调试/验证/复盘等环节
- Elixir 编排模式：fan-out/pipeline/map-reduce 链式组合技能
- meta 技能（skill-forge/skill-creator）自动沉淀新技能形成飞轮
- 可选 hook 将技能激活率从约 20% 提升至约 84%

## 适用场景

- 给 Claude Code 装上结构化工作流，避免跳步直接写代码
- 在破坏性操作前强制确认与影响评估
- 把会话中的经验沉淀为可复用技能

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L8: **Skills** teach Claude *how* to do things. Not prompts - actual workflows that trigger automatically.
> L14: Just markdown files. No magic required.
> L29: - battle-plan - Complete planning ritual before significant tasks. Orchestrates rubber-duck (scope) -> pre-mortem (

## 星数曲线

```mermaid
xychart-beta
    title "ElliotJLT/Claude-Skill-Potions 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 60 --> 63
    line [61, 62, 62]
```

2026-10-18 61 → 2026-10-28 62（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `23185cf7c803` · [字段定义](../../DATASET.md)*
