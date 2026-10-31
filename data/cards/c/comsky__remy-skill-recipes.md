# comsky/remy-skill-recipes

⭐ 13 · Python · MIT · 推送 2026-07-14 · [GitHub](https://github.com/comsky/remy-skill-recipes) · [官网](https://skills.sh/comsky/remy-skill-recipes) · 个人维护

**面向软件工程的 SKILL.md 技能配方集：12 个结构化 LLM 工作流**

遵循 SKILL.md 开放标准的可复用技能合集，收录 12 个面向软件工程任务的结构化提示词工作流，覆盖代码审查、变更复审、架构文档生成、竞品功能对比、文档定稿提交、GitHub PR 自动化、Notion 格式化等。分为单次运行的 Execution Skill 与持久化/自动化导向的 System Skill 两类，每个技能含输入要求、输出格式、流程、护栏与失败模式章节，并标注 Draft/Stable/Production 成熟度。兼容 Cursor、Claude Code、VS Code + Copilot、Codex、Gemini CLI 等 agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 个 SKILL.md 格式技能，分 Execution 与 System 两类
- 每技能含 Purpose/Inputs/Guardrails/Failure Patterns 结构化章节
- 通过 npx skills add 一键安装，或手动复制单个技能
- 技能声明模型无关，要求推理型 LLM 与结构化输入

## 适用场景

- 给 Cursor/Claude Code 等 agent 添加代码审查与变更复审工作流
- 生成带风险分级的架构文档
- 自动化推送分支、注册 PR、处理 review 意见并合并

## 场景标签

`提示工程` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L5: This repository is a curated collection of reusable, structured prompt workflows
> L9: Each skill follows the SKILL.md open standard —

## 星数曲线

```mermaid
xychart-beta
    title "comsky/remy-skill-recipes 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `6e400350ba6c` · [字段定义](../../DATASET.md)*
