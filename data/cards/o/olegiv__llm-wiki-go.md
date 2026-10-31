# olegiv/llm-wiki-go

⭐ 13 · Go · GPL-3.0 · 推送 2026-10-09 · [GitHub](https://github.com/olegiv/llm-wiki-go) · 个人维护

**Karpathy 式 LLM Wiki 仓库脚手架：raw/ 存原始资料，wiki/ 存编译后知识**

一个围绕『知识工件是编译后的活 wiki』理念组织的仓库结构：raw/ 存放不可变的文档、转录与笔记，wiki/ 是 Obsidian 风格 Markdown 的知识层，每个实质性声明通过 ## Sources 溯源到 raw/。编码代理（如 Claude Code）充任编译器，按 CLAUDE.md/AGENTS.md 规则读取 raw/、写入 wiki/；Go 编写的 wikilint 检查标题、来源节、链接解析、slug 冲突与孤儿页等结构不变量。默认示例绑定 ocms-go.core 项目，多项目用法见 docs/MULTI_PROJECT.md。GPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- raw/ 不可变源料层与 wiki/ 编译知识层的双层数据结构
- wikilint（Go CLI）检查标题、来源节、wikilink 解析、slug 冲突与孤儿页
- 定义 ingest-source / answer-from-wiki / reconcile-conflicts / lint-wiki 四类代理技能工作流
- 冲突记录在 ## Contradictions 节而非静默合并

## 适用场景

- 为代码库或研究资料构建可溯源的代理驱动知识库
- 让 Claude Code 等编码代理按固定规则编译并维护 wiki
- 用 wikilint 在 CI 或本地校验 wiki 结构一致性

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: A [Karpathy-style][karpathy-llm-wiki] "LLM Wiki" — a repo designed around
> L20: Claude Code (and any other coding agent operating in this repo) acts as
> L27: The Go CLI `wikilint` enforces the structural invariants so the wiki

## 星数曲线

```mermaid
xychart-beta
    title "olegiv/llm-wiki-go 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `bd95e901cb22` · [字段定义](../../DATASET.md)*
