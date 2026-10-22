# SYuan03/Skill-Anything

⭐ 342 · Python · MIT · 推送 2026-09-26 · [GitHub](https://github.com/SYuan03/Skill-Anything) · [官网](https://SYuan03.github.io/Skill-Anything/) · 个人维护

**把任意来源（PDF/视频/网页/音频/文本/仓库）转成学习包与 Agent 技能的 CLI 工具**

面向学习者与开发者的 Python CLI 工具：一条命令把 PDF、视频、网页、音频、文本或代码仓库解析为分章节输入，经 map-reduce LLM 流水线（并发 + 磁盘缓存、双层模型路由）生成 12 节学习包（笔记、词汇表、测验、闪卡、练习、学习路径），并核验每条 LLM 生成项的原文引用。支持导出为 SKILL.md 形式的 agent 技能、离线单文件 HTML 学习站、Anki 卡组。v0.3 起支持长文档分章节配额覆盖；兼容任何 OpenAI 兼容 API，需自配 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多源输入（PDF/视频/网页/音频/文本/仓库）→ 12 节结构化学习包（6 种测验题型）
- map-reduce 流水线：并发执行 + sha256 磁盘缓存 + FAST/SMART 双层模型路由
- 引用验证：每条测验/闪卡/练习须含原文引文，`sa audit --strict` 提供 CI 门禁
- 多格式输出：离线单文件 HTML 站、Anki TSV、SKILL.md agent 技能导出与 lint

## 适用场景

- 把整本书或长 PDF 转成带测验和闪卡的学习包用于主动回忆
- 把代码仓库转成入职学习笔记、术语表和学习路径
- 把学习包导出为 Claude Code/Cursor 可用的 SKILL.md 技能

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L199: **Skill-Anything automates the entire pipeline.** One command. Any source. Structured study pack by default, optio
> L214: 1. **Study Pack (default)**: a structured learning package built from raw source material
> L287: Skill-Anything works with **any OpenAI-compatible API**:

## 星数曲线

```mermaid
xychart-beta
    title "SYuan03/Skill-Anything 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 337 --> 339
    line [338, 338]
```

2026-10-18 338 → 2026-10-21 338（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `920695dc5f6b` · [字段定义](../../DATASET.md)*
