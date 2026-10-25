# meydeey/obsidian-god-mode-claude-code

⭐ 41 · MIT · 推送 2026-04-20 · [GitHub](https://github.com/meydeey/obsidian-god-mode-claude-code) · 个人维护

**让 Claude Code 自动生成 Obsidian 知识库的提示词集**

仓库提供两个 Markdown 文件：PROMPT-PILOT.md 是带 3 次人工检查点的试点提示词，用户替换 5 个变量（主题、集群、描述、vault 路径、目标页数）后交给 Claude Code 执行，1-2 小时生成 30-50 页带 wikilinks、集群结构和 WebSearch 事实核查的 Obsidian 知识库；GUIDE.md 讲解逐步使用与领域适配方法。生产级多 agent 提示词由试点运行结束时的校准报告生成。面向 Obsidian 与 Claude Code 用户，由个人创作者 LE LABO IA 维护。

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

- 试点提示词在 3 个节点暂停等待人工验证（页面规划/8 页后/运行结束）
- 生成含 wikilinks、集群与导航图谱的 Obsidian vault，核查记录可查
- 适配任意领域的 5 变量模板，试点后可扩展至 500+ 页

## 适用场景

- 用 Claude Code 批量构建某个主题的 Obsidian 知识库
- 用结构化 wiki 替代一次性 RAG 查询的工作流
- 从 30-50 页试点起步，再扩展到 500+ 页知识库

## 场景标签

`提示工程` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L7: > Transforme Claude Code en générateur autonome de knowledge vault Obsidian. Tu donnes un sujet, il construit pour t
> L15: 1. **`PROMPT-PILOT.md`** : version pilote avec checkpoints humains. Tu lances sur **1 seul cluster de 30-50 pages**

## 星数曲线

```mermaid
xychart-beta
    title "meydeey/obsidian-god-mode-claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ec896994527a` · [字段定义](../../DATASET.md)*
