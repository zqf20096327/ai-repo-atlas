# mimfort/rag_for_git

⭐ 20 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/mimfort/rag_for_git) · 个人维护 · 中文 README

**面向 Claude Code/Codex 的 RAG 代码评审 MCP 服务器**

以 MCP 服务器加技能集形式接入 AI 客户端（Claude Code、Codex），为 PR 评审提供全仓上下文：PostgreSQL/ParadeDB 上 pgvector ANN 与 BM25 混合检索、Voyage 嵌入与重排、Neo4j 代码图（SCIP 或 tree-sitter 的 CALLS/IMPLEMENTS），产出锚定变更行的内联评论。工作流包括 review-pr、solve-task、ask、pr-walkthrough、性能/可维护性专项评审与任务板操作。要求 Python 3.11–3.13、Docker 运行存储栈、Voyage 与 VCS 凭据；无基础索引时仅剩 diff 加临时 overlay 上下文。通过 uv/PyPI 安装，支持共享主机团队部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pgvector ANN + BM25 混合检索 + Voyage 嵌入/重排的分支级 base index
- Neo4j 代码图（node_id = path#fqn），SCIP 不可用时回退 tree-sitter
- 发布前 grounding 验证：发现必须引用真实变更代码，隐藏指纹防重复发布
- 通过 reviewer install 接入 Claude Code/Codex，MCP 服务器承担存储/图/VCS/任务板操作

## 适用场景

- 让 AI 客户端基于全仓上下文评审 PR 并发布锚定行的内联评论
- 团队在共享主机上部署，各客户端连接同一存储栈
- 新成员通过 ask 技能做带 path:line 引用的代码库问答

## 场景标签

`代码审查` `RAG` · 领域:编码与开发

## 证据(README 行号)

> L5: AI-assisted pull-request reviews grounded in whole-repository context: hybrid search, a code
> L92: service account. Each client launches its own `reviewer-mcp` stdio process; those processes share
> L203: RAG means retrieval-augmented generation: the model receives code selected by hybrid semantic and

## 星数曲线

```mermaid
xychart-beta
    title "mimfort/rag_for_git 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `1217cfe2c8db` · [字段定义](../../DATASET.md)*
