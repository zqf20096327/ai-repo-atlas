# ayush488-glitch/my-secondbrain

⭐ 15 · Python · MIT · 推送 2026-04-29 · [GitHub](https://github.com/ayush488-glitch/my-secondbrain) · 个人维护

**用 Obsidian+Claude+Codex 搭建 AI 维护个人维基的实践手册与模板**

提供一套构建源引用型个人知识库的完整方案：以 raw/（不可变原始材料）、wiki/（AI 撰写的结构化页面）、schema 文件（CLAUDE.md/AGENTS.md 操作规则）三层结构组织知识。仓库含分步设置手册、起始模板（Claude 命令 /ingest /query /lint）、一键脚手架的 Codex skill（Python 脚本）与示例 vault。使用需自备 Obsidian、Claude Desktop（含文件系统 MCP）与 Codex，核心规则是 wiki 中每条声明须以 [[source-slug]] 引用来源页。

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

- raw/wiki/schema 三层分离的文件夹结构模板
- Codex skill 一条命令脚手架新 vault（create_llmwiki_vault.py，支持 --dry-run 等参数）
- CLAUDE.md/AGENTS.md 作为助手操作宪法，含引用、摄取、矛盾标记规则
- /ingest /query /lint 三个核心 Claude 命令模板

## 适用场景

- 把文章、转录、会议笔记等原始材料沉淀为可溯源的个人维基
- 让 Claude/Codex 代为组织、链接、总结笔记并检测矛盾
- 查询时获得带来源引用的回答而非凭记忆生成

## 场景标签

`知识库管理` `教程课程` · 领域:知识与检索

## 证据(README 行号)

> L18: This project gives you a working pattern for an **AI-maintained personal wiki**:
> L32: |Full playbook|Step-by-step setup for Obsidian, Claude, Codex, MCP, and GitHub|
> L33: |Starter templates|`CLAUDE.md`, `AGENTS.md`, `wiki/index.md`, `wiki/log.md`, and Claude commands|

## 星数曲线

```mermaid
xychart-beta
    title "ayush488-glitch/my-secondbrain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5c790764c24e` · [字段定义](../../DATASET.md)*
