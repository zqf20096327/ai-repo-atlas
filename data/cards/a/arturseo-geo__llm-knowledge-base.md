# arturseo-geo/llm-knowledge-base

⭐ 40 · MIT · 推送 2026-04-06 · [GitHub](https://github.com/arturseo-geo/llm-knowledge-base) · [官网](https://thegeolab.net) · 个人维护

**面向个人知识库的 LLM 编译 schema 标准：AGENTS.md 规范+模板+学习层**

一套用于 LLM 编译个人知识库的 schema 与工作流：核心是 AGENTS.md 规范文件，约定目录布局、frontmatter 结构、三个索引文件的维护方式以及编译/查询/lint 工作流。用户将原始资料放入 raw/，由 LLM 按规范自动生成概念文章、摘要、反向链接与闪卡，用户不手动编辑 wiki。附加间隔重复学习层（简化 FSRS 复习队列、gap 追踪、苏格拉底问答），并提供 Obsidian 双 vault 设置防止 agent 生成内容污染个人笔记。以 git clone 模板方式使用，无独立软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AGENTS.md 规范：目录布局、frontmatter、索引维护、编译/查询/lint 工作流，带版本号
- 自动生成闪卡与基于简化 FSRS 的复习队列、gap 追踪
- 两 vault 模型与 sandbox-first 晋升机制，隔离 agent 内容与个人笔记
- 含已填充的示例 wiki（AI alignment 主题）与 finetune 路径文档

## 适用场景

- 让 LLM 把收集的 PDF/网页/markdown 自动编成结构化知识库
- 通过间隔重复闪卡和复习队列掌握知识库内容
- 把反复 lint 后的 wiki 转为微调训练语料

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L10: **A schema and workflow for LLM-compiled personal knowledge bases.**
> L20: |`AGENTS.md`|The schema spec — every LLM agent operating on your wiki reads this first|
> L94: `AGENTS.md` is the contract between you and any LLM operating on your knowledge base. It defines:

## 星数曲线

```mermaid
xychart-beta
    title "arturseo-geo/llm-knowledge-base 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-29 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a988e1b64aea` · [字段定义](../../DATASET.md)*
