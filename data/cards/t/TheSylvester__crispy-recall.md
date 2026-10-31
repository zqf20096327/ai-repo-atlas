# TheSylvester/crispy-recall

⭐ 15 · TypeScript · MIT · 推送 2026-09-11 · [GitHub](https://github.com/TheSylvester/crispy-recall) · [官网](https://recall.thesylvester.ca) · 个人维护

**为 Claude Code/Codex 提供本地会话记录检索记忆**

索引 Claude Code 与 Codex 生成的 JSONL 会话日志到本地 SQLite，用 SQLite FTS5 做关键词检索、Nomic Embed Text v1.5（经 llama.cpp 本地运行）生成向量做语义检索，rank fusion 合并结果，构成对历史会话的本地 RAG。通过生命周期钩子在会话结束时自动索引，安装时回填磁盘上已有会话。附带技能教 agent 何时检索，支持按 commit/blame 从代码行回溯到产生它的对话，及实验性的多机 hub/satellite 共享模式。自身不做 LLM 调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- FTS5 关键词 + 本地向量嵌入的混合检索与 rank fusion
- recall --commit / --blame 从提交或代码行回溯到会话对话
- 自动钩子索引 + 安装时回填历史会话，索引保留于原始 transcript 删除之后
- 实验性多机模式：satellite 上传 transcript 到 hub 集中检索

## 适用场景

- 新会话中让 agent 检索之前会话的决策与上下文，省去手写交接
- 通过 commit 或某行代码找回当时的讨论理由与被否方案
- 多台机器共享同一份编码对话历史

## 场景标签

`Agent 记忆` `RAG` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L9: Under the hood, Recall indexes the JSONL conversation logs that Claude Code and Codex already generate in a local SQ
> L215: 4. A small skill teaches your agent to search first when prior work is likely to matter.
> L218: On a single machine there's no resident daemon (the optional hub daemon runs only in satellite mode), and recall m

## 星数曲线

```mermaid
xychart-beta
    title "TheSylvester/crispy-recall 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c149f08809d5` · [字段定义](../../DATASET.md)*
