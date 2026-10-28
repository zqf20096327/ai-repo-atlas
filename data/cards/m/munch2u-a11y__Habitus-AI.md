# munch2u-a11y/Habitus-AI

⭐ 19 · Python · Apache-2.0 · 推送 2026-09-06 · [GitHub](https://github.com/munch2u-a11y/Habitus-AI) · 个人维护

**面向 AI Agent 的记忆与认知引擎：纯 Python + SQLite 的结构化记忆系统**

一个零外部运行时依赖的 Python 引擎，为 Agent 提供长期记忆与证据保留式 RAG。机制上采用沙漏双锥拓扑组织记忆，以 Y 轴行程时间密码替代纯余弦相似度检索；边权重全局守恒（和为 1.0）；设双通道事实安全轨（SQLite 不可变记录直接检索 + 图遍历 Dense+BM25 重排）；动作分类为 SPEAK/LOOK/DO 三干；仅在收到经验证的外部执行回执（ActionReceipt）后才强化学习。内置工具套件与命令行/Web 启动器，可自动探测本地 Ollama 模型，支持 ChromaDB/Pinecone/pgvector 可选向量适配器。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Python 标准库 + SQLite 运行，无外部数据库依赖
- Y 轴行程时间密码与守恒流体边权重（∑=1.0）驱动的图检索
- 回执门控学习：仅 ActionReceipt 验证后强化边权重
- 内置 read_file/execute_python/web_search 等工具绑定至 LOOK/DO/SPEAK 干路

## 适用场景

- 为自主 Agent 构建跨进程重启持久的身份与证据记忆
- 需要事实安全轨防止关键数字/名称被检索驱逐的 RAG 场景
- 通过重复执行与回执验证让 Agent 自然形成可复用技能

## 场景标签

`Agent 记忆` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L8: **Habitus AI** (`habitus-ai`) is a lightweight, zero-external-runtime-dependency Python engine for dual-cipher, cons
> L55: - 🛠️ **Built-in Operational Tool Suite & Trunk Binding**: Includes standard tools (`read_file`, `write_file`, `insp

## 星数曲线

```mermaid
xychart-beta
    title "munch2u-a11y/Habitus-AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-28 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `4fe275df413b` · [字段定义](../../DATASET.md)*
