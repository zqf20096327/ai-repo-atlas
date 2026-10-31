# rajkripal/cashew

⭐ 27 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/rajkripal/cashew) · 个人维护

**AI agent 持久记忆库：单文件思维图存储与召回**

面向 AI agent 的持久记忆系统：将决策、模式、关系等知识提取进单一 SQLite 思维图，通过本地嵌入（all-MiniLM-L6-v2）+ sqlite-vec 种子检索 + 递归 BFS 图游走召回上下文，召回成本与图规模无关。节点设有有机衰减机制，低访问节点逐渐退出检索。提供 CLI、Python API 与可视化 dashboard，内置 Obsidian、markdown 目录、会话日志等摄入器，支持 Claude Code / OpenClaw / Hermes Agent 集成。提取与思考周期需 LLM API key，仅检索可离线。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 SQLite 文件存储，无外部服务
- 本地嵌入 + sqlite-vec 种子 + 递归 BFS 图检索，上下文成本恒定
- 节点有机衰减：低使用知识自动淡出检索
- 内置 Obsidian/markdown/会话日志/Claude 导出等摄入器，支持 --no-llm 离线模式

## 适用场景

- 让 Claude Code 等 agent 跨会话保留决策与项目上下文
- 把 Obsidian 库或 markdown 笔记转为可检索的知识图
- 通过 dashboard 浏览与调试记忆图的检索路径

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Persistent thought-graph memory for AI agents.**
> L135: - **LLM for intelligence.** Extraction and think cycles need an LLM (Claude, GPT, etc). Retrieval and storage don'

## 星数曲线

```mermaid
xychart-beta
    title "rajkripal/cashew 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-31 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `754151a95008` · [字段定义](../../DATASET.md)*
