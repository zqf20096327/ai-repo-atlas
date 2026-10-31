# phelps-sg/claude-code-obsidian-skills

⭐ 14 · 推送 2026-03-02 · [GitHub](https://github.com/phelps-sg/claude-code-obsidian-skills) · 个人维护

**把 Obsidian 库变为人/AI 共享知识库的 Claude Code 技能集**

一组 Claude Code 技能（SKILL.md 格式），将 Obsidian 库用作软件开发项目中人与 AI 共享的知识库。包含四个技能：Vault Manager 定义库约定并指导 agent 在发现架构时写笔记；Vault Auditor 定期检查矛盾、断链与潜在交叉洞察；External Sync 将 Notion/Confluence 等外部知识源桥接入库（含去重与人工确认）；WIP Dashboard 从库、GitHub 与外部工具生成看板。安装方式为复制技能目录到 .claude/skills/ 并手动配置路径与标签体系，是博客文章的配套材料，需按自身技术栈定制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个技能：库读写管理、定期审计、外部源同步、看板生成
- Vault Auditor 检查矛盾、断链并挖掘图结构隐含洞察
- 通过 CLAUDE.md 指令引导 agent 优先查库而非直接搜代码
- 需定制库路径、标签体系与外部工具引用

## 适用场景

- 让 Claude Code 在开发中沉淀和复用项目知识到 Obsidian
- 审计共享库中的矛盾与断链
- 把 Notion/Confluence 中的知识同步进 Obsidian 库
- 生成跨工具的进行中工作看板

## 场景标签

`Agent 记忆` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L3: A set of Claude Code skills that turn an Obsidian vault into a shared knowledge base for human and AI collaboration 
> L11: |**Vault Manager**|`/pkm`|Core read/write skill. Defines vault conventions and instructs the agent to write notes w

## 星数曲线

```mermaid
xychart-beta
    title "phelps-sg/claude-code-obsidian-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b62eacf4a732` · [字段定义](../../DATASET.md)*
