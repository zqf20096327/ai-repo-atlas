# ActiveMemory/ctx

⭐ 79 · HTML · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/ActiveMemory/ctx) · [官网](https://ctx.ist) · 组织维护

**让 AI 编程助手跨会话持久化项目上下文的文件式系统**

以文件目录 .context/ 为载体的上下文持久层，供 AI 编程助手在会话之间保存、结构化并重新加载任务、决策与经验。以单个 Go 二进制分发，可下载预编译版本或从源码构建；不绑定任何模型或厂商，凡能读文件的 AI 工具均可配合使用。要求项目内存在 .git/，否则除少量白名单命令外拒绝运行。另提供面向研究、事件复盘等知识型工作的编辑管线工作流（Phase KB）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任务、决策、经验跨会话持久化并可重新加载
- 不绑定模型或厂商，兼容任何可读文件的 AI 工具
- 单二进制分发，预编译或 Go 源码构建
- 提供知识库工作流（ctx kb topic 编辑管线）

## 适用场景

- 让 AI 编程助手在新会话中记得架构决策与历史教训
- 研究项目、厂商规格分析、事件复盘的知识库沉淀
- 在 Claude Code、Cursor、Aider 等工具间共享项目上下文

## 场景标签

`Agent 记忆` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L7: A lightweight, file-based system that enables AI coding assistants to persist,
> L10: `ctx` works with **any AI tool** that can read files; no model or
> L58: * **Persist**: Tasks, decisions, learnings survive session boundaries

## 星数曲线

```mermaid
xychart-beta
    title "ActiveMemory/ctx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-28 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2ddfe2fef039` · [字段定义](../../DATASET.md)*
