# MyrikLD/memlord

⭐ 29 · Python · AGPL-3.0 · 推送 2026-09-26 · [GitHub](https://github.com/MyrikLD/memlord) · 组织维护

**自托管多用户 MCP 记忆服务器，供个人与团队使用**

基于 PostgreSQL + pgvector 的自托管 MCP memory server，面向个人与团队。提供 11 个 MCP 工具（store/retrieve/recall 等），检索采用 BM25 与向量 KNN 并行、经 RRF 融合的混合搜索；本地 ONNX 嵌入模型（paraphrase-multilingual-MiniLM-L12-v2）随服务分发，无需外部 API。支持多用户隔离、共享工作区、OAuth 2.1、Web UI 全 CRUD 与 JSON 导入导出；含 'dream' 整合流程，由客户端 LLM 驱动合并近似记忆（非破坏性）。限制：需 Python 3.12、PostgreSQL ≥15（pgvector）与 uv；记忆为手动显式存储，非自动抽取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BM25 + 向量 KNN 经 RRF 融合的混合搜索
- 11 个 MCP 工具，含自然语言时间检索与 dream 整合流程
- 多用户隔离 + 邀请制共享工作区 + OAuth 2.1 内置授权服务器
- 本地 ONNX 嵌入零配置，渐进式披露降低 token 用量

## 适用场景

- 为 Claude 等 MCP 客户端提供持久化记忆存储与检索
- 团队共享知识库，按工作区隔离权限
- 通过 Web UI 浏览、编辑、导出记忆数据

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L4:  Self-hosted MCP memory server for personal use and teams
> L24: - 🛠️ **11 MCP tools** — store, retrieve, recall, list, search by tag, get, update, delete, move, list workspaces, d

## 星数曲线

```mermaid
xychart-beta
    title "MyrikLD/memlord 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-31 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7f7e253ede55` · [字段定义](../../DATASET.md)*
