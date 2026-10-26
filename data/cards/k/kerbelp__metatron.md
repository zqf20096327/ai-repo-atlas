# kerbelp/metatron

⭐ 27 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/kerbelp/metatron) · [官网](https://getmetatron.com/) · 个人维护

**为 AI 编程 agent 提供 git 内团队决策上下文层的工具**

Metatron 把代码库的实现决策（模式、被否决的做法、边界情况、内部约定）记录为结构化 markdown 决策文件，随代码在 git 中版本化，编程 agent 写码前读取，并通过 PR 评审人工晋升为正式决策。默认 files-first 模式无需服务器；可选自托管 MCP server 模式（SQLite 存储、相关性排序、agent 反馈闭环），两种模式无损互通。LLM 抽取步骤（ingest 等）需 Anthropic API key，serve/ui/candidates 完全本地。面向使用 AI 编程 agent 的开发团队，为私有代码库自托管部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每条约定一个 markdown 决策文件，git 版本化、PR 人工评审晋升
- 可选 SQLite + MCP server 服务层，与 files-first 模式无损往返
- 决策文件为 OKF v0.1 标准捆绑包，可在任意编辑器/GitHub 阅读
- agent 通过 submit_feedback 上报知识缺口并生成新候选，闭环人工策展

## 适用场景

- 让编程 agent 写码前了解团队约定，减少违反规范
- 把团队工程决策沉淀为可审计、可 PR 评审的知识库
- 私有代码库上自托管 MCP 服务，向 agent 提供排序后的上下文

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L19: Metatron captures a codebase's real implementation decisions — preferred
> L32: For teams that want a serving layer on top, Metatron also runs as a self-hosted

## 星数曲线

```mermaid
xychart-beta
    title "kerbelp/metatron 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-26 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f9bdc9183ca9` · [字段定义](../../DATASET.md)*
