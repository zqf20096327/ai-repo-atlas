# lean-explore/lean-explore

⭐ 82 · Python · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/lean-explore/lean-explore) · [官网](https://www.leanexplore.com/) · 个人维护

**Lean 4 声明的语义搜索引擎，含 MCP 服务与插件**

面向 Lean 4 生态的声明搜索引擎：索引 Mathlib、Batteries、FLT 等 9 个项目，支持远程 API 与本地后端两种运行方式。本地后端采用 BM25 + FAISS 混合检索并加载端上嵌入与重排模型。以 Python 包（pip）安装提供 CLI 与 MCP Server，可接入 Claude Code、Codex、Cursor 等 MCP 客户端；托管端点限制每客户端 IP 每 60 秒 30 次 POST 请求。有 arXiv 论文与文档站。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 索引 9 个 Lean 项目（Mathlib/Lean/Batteries 等）的声明
- 本地后端采用 BM25 + FAISS 混合检索与端上嵌入/重排模型
- 提供 MCP Server 与 Claude Code/Codex 插件
- MCP 工具均为只读，不修改 Lean 包

## 适用场景

- 在 Mathlib 等项目中查找特定的 Lean 4 声明
- 让 Claude/Codex 等 agent 通过 MCP 检索 Lean 定理
- 离线环境下运行本地语义搜索后端

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3:  A search engine for Lean 4 declarations
> L40: To run the **local** search backend (which uses on-device embedding and reranking models), install the extra ML dep
> L97: |Local Search Backend|How hybrid BM25 + FAISS + reranking works.|

## 星数曲线

```mermaid
xychart-beta
    title "lean-explore/lean-explore 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 80 --> 83
    line [81, 82, 82]
```

2026-10-18 81 → 2026-10-26 82（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c280661b02e2` · [字段定义](../../DATASET.md)*
