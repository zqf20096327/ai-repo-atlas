# PSkinnerTech/brainlift-writer-skill

⭐ 10 · MIT · 推送 2026-06-30 · [GitHub](https://github.com/PSkinnerTech/brainlift-writer-skill) · 个人维护

**面向 AI 使用者的 BrainLift 写作技能包：把研究笔记整理成结构化上下文文档**

一个与具体 AI 工具无关的技能（skill），内容为可移植的 agent 指令，用于将研究、笔记与粗略想法整理成 BrainLift 文档——按 purpose/scope、DOK 2 知识树、DOK 3 洞察、DOK 4 观点的层次组织的上下文文档。提供从零起草、改进既有文档、审计结构三种用途。安装方式是把技能文件夹复制到 Codex 技能目录，或在其他工具中把 SKILL.md 与模板文件作为指令/参考资料粘贴使用。限制：不含可执行程序，产出依赖所用模型，要求标注缺口而非编造证据。

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

- 可移植 SKILL.md 指令，可在 Codex/Claude/ChatGPT/Cursor/Gemini 中使用
- 按 DOK 层级（知识树/洞察/观点）结构化研究材料
- 支持起草、改进、审计三种 BrainLift 操作
- 要求保留不确定性与来源出处，标注缺口而非编造

## 适用场景

- 把零散笔记或研究材料整理成结构化上下文文档
- 为已有 BrainLift 做结构与论证完整性审计
- 在多个 AI 工具间复用同一套写作指令

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: BrainLift Writer is an AI-agnostic skill for turning research, notes, and rough thinking into a structured BrainLift
> L44: This skill is intentionally portable. For Claude Projects, ChatGPT custom GPTs, Cursor rules, or other agents:

## 星数曲线

```mermaid
xychart-beta
    title "PSkinnerTech/brainlift-writer-skill 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-10 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `6d1eeac748d1` · [字段定义](../../DATASET.md)*
