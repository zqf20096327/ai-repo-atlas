# aetox-skills/senior-architect-agent

⭐ 23 · Python · MIT · 推送 2026-07-20 · [GitHub](https://github.com/aetox-skills/senior-architect-agent) · 个人维护

**让 AI agent 执行既有系统架构勘察的技能（skill）**

面向 Claude Code、Codex、Antigravity 等 agent 的认知框架技能：强制 agent 先勘察现有代码库，按 Intake→Inspect→Map→Assess→Document→Validate→Report 流程产出架构总览、模块图、数据流、Mermaid 图、债务清单与交接文档。提供 Scan/Focus/Full 三档 smallest safe pass，可选知识图谱辅助依赖分析（file reading 优先于冲突的 graph 数据）。要求模型具备 128K+ 长上下文（Scan 模式 32K），随附 7 个规则文件、11 个模板与示例输出，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三档模式（Scan/Focus/Full），默认最小安全勘察
- 每项 finding 须含 evidence、impact、severity、confidence 与最小安全修正
- 可选 knowledge-graph 辅助依赖映射与影响半径分析
- 输出架构总览、模块图、数据流、Mermaid 图、债务/风险清单与 ai-agent 交接笔记

## 适用场景

- 让 agent 接手前先摸清现有系统架构并产出文档
- 架构变更评审前生成债务与风险评估
- 团队交接时生成模块图与 handoff notes

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: > Cognitive framework ที่เปลี่ยน AI agents ให้เป็น senior architects — evidence-first system understanding, honest u
> L7: Skill นี้บังคับให้ agent inspect, map, assess, document, validate, และรายงานระบบที่มีอยู่จริง ก่อนเสนอการเปลี่ยนแปลง
> L103: ดู INSTALL.md สำหรับ Codex, Claude Code, Antigravity, AGENTS.md, และ manual

## 星数曲线

```mermaid
xychart-beta
    title "aetox-skills/senior-architect-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `1e8a9254326d` · [字段定义](../../DATASET.md)*
