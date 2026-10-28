# castnettech/mnemosyne

⭐ 63 · Python · AGPL-3.0 · 推送 2026-05-30 · [GitHub](https://github.com/castnettech/mnemosyne) · [官网](https://pypi.org/project/mnemosyne-engine/) · 组织维护

**零依赖的本地代码检索与上下文压缩引擎，供 LLM/开发者使用**

将代码库、文档与数据库 schema 索引到本地 SQLite，用 BM25、TF-IDF、符号匹配等 6 信号混合检索排序，并按 token/结果预算做 AST 感知压缩后返回。支持 7 种语言的结构化切块、增量 delta 跟踪、内容去重与守护进程模式。纯 Python 3.11+ 标准库实现，无需 API key 或云端。面向需要在大代码库中做精确检索并向 LLM 提供精简上下文的开发者，另提供 MCP 服务器与 Ollama 桥接两个附加包。采用 AGPL-3.0 与商业许可双许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 信号混合检索（BM25/TF-IDF/符号/使用频率/预取/可选稠密向量）经 RRF 融合
- AST 感知四阶段压缩，保留签名、docstring 与控制流
- 零运行时依赖，纯 Python 3.11+ 标准库，全程本地运行
- 提供 MCP 服务器（Claude Code）与 Ollama 桥接两个附加包

## 适用场景

- 在大代码库中用自然语言查询定位函数级实现
- 给 Claude/GPT/Cursor 等 agent 提供预算内的精简上下文，降低 API 开销
- PR 审查时基于 delta 跟踪拉取变更函数及其调用方与测试
- 迁移或重构前分析旧 API 的全部使用点与调用频率

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5:  Intelligent code retrieval engine -- index, search, and compress any codebase with zero dependencies.
> L14: Mnemosyne indexes your codebase and documents into a local SQLite store, scores every chunk with a 6-signal hybrid 
> L61: **LLM context optimization** -- Feed Claude, GPT, Cursor, or any LLM agent the right tokens from a 100K+ codebase. 

## 星数曲线

```mermaid
xychart-beta
    title "castnettech/mnemosyne 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 61 --> 64
    line [62, 63, 63]
```

2026-10-18 62 → 2026-10-28 63（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4e5d4bf1be00` · [字段定义](../../DATASET.md)*
