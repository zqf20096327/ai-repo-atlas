# Yang1Bai/nature-paper-hub

⭐ 19 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/Yang1Bai/nature-paper-hub) · 个人维护 · 中文 README

**面向 19 个顶刊投稿的全流程 AI 论文写作 agent 技能集**

以 7 个 agent 技能组成的顶刊论文写作流水线：12 阶段对话路由覆盖选刊、文献调研、起草、图表生成、引用核验、模拟审稿与审稿回复；支持 OpenClaw、Claude Code、Codex 三种平台安装，输出 LaTeX/Overleaf、Word、PPTX。内置 485 篇清洗文献索引，CrossRef 实时核验与 RetractionWatch 撤稿检查，可选 LITREVIEW_API 接入私有文献库，默认无需任何密钥。手动安装需保留完整 clone 并设 CLAUDE_PLUGIN_ROOT。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 阶段全流程：选刊→文献→起草→图表→引用核验→模拟审稿→审稿回复
- 覆盖 19 个顶刊并内置字数/图数/引用限制索引
- CSV/Excel 自动生成 matplotlib/R 投稿级图表
- CrossRef 实时核验 + RetractionWatch 撤稿检查 + BibTeX/Zotero 导出

## 适用场景

- 我要按目标期刊的字数图表限制起草 Nature 系列投稿
- 投稿前让多个专家 agent 模拟审稿并核验引用完整性
- 把我的实验数据 CSV 自动转成投稿级图表
- 根据审稿意见起草 point-by-point 回复

## 场景标签

`科研工具` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L19: `top-journal-paper-hub` 是一套面向顶级期刊投稿的全流程 AI 写作 agent，覆盖从**选刊、文献调研、论文起草、图表生成、引用核验、投稿前模拟审稿、投稿前检查，到审稿意见回复**的完整链路。
> L21: 支持 **OpenClaw、Claude Code、Codex** 三种平台，输出格式支持 **LaTeX（Overleaf）和 Word（.docx）**，并内置 CSV/Excel 自动生图、CrossRef 实时引用核验、个
> L223: |🏠 `nature-paper-hub`|Main hub with 12-stage (0–11) conversational pipeline (incl. integrity check + reviewer sim)

## 星数曲线

```mermaid
xychart-beta
    title "Yang1Bai/nature-paper-hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d70eb8af2da0` · [字段定义](../../DATASET.md)*
