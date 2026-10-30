# HolobiomicsLab/asb-skill-collections

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/HolobiomicsLab/asb-skill-collections) · [官网](https://holobiomicslab.cnrs.fr) · 组织维护

**面向科学 AI agent 的证据锚定技能与工具集合（代谢组学 5,859 技能）**

由 ASB（AgenticScienceBuilder）流水线生成的多领域技能集市：当前发布代谢组学合集 v0.2.0，含 5,859 个从 566 篇同行评审论文及代码库提炼的 SKILL.md 技能、909 个 EDAM 标注的工具记录与 21 个组合式工作流超技能，以逐字证据锚定并在发布前做许可/PII 门控。通过 Claude Code 本地 marketplace 或 asbb CLI 安装到 Codex/Copilot/Gemini/Cursor 等运行时，任意 agent 可直接读取 Markdown+JSON 索引；可选基于 Perspicacité 的论文 RAG grounding。Dagstuhl 计算代谢组学研讨会发起的社区项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 5,859 个技能 + 909 工具，源自 566 篇同行评审论文，逐字证据锚定
- EDAM 标注、许可/PII 门控后发布，ASB-Benchmark/ASB-Capsules 待发布
- asbb CLI 支持多运行时安装（Claude Code/Codex/Copilot/Gemini/Cursor/Cline 等）与离线无 key 检索
- 可选 grounding：对照源论文核验参数与声明的 RAG 机制

## 适用场景

- 为 Claude Code 等 agent 运行时安装代谢组学分析技能
- 按 EDAM/工具名/关键词检索经论文验证的分析流程
- 在执行数值参数前对照源论文做 grounding 核验
- 作为科研 agent 的领域 benchmark 与工具索引数据源

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L11: Curated, **evidence-grounded** skill and software-tool collections for scientific
> L24: > `collections/metabolomics/v2` — **5,859 skills**
> L47: `asb-skill-collections` is a **multi-domain** marketplace — it hosts ASB-generated skill

## 星数曲线

```mermaid
xychart-beta
    title "HolobiomicsLab/asb-skill-collections 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `fee44e55892e` · [字段定义](../../DATASET.md)*
