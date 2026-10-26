# EllisMorrow/Caelune

⭐ 45 · Python · MIT · 推送 2026-08-08 · [GitHub](https://github.com/EllisMorrow/Caelune) · [官网](https://ellismorrow.github.io/Caelune/) · 个人维护 · 中文 README

**本地优先的私人知识检索 Windows 桌面应用与只读 MCP 服务器**

面向个人用户的 Windows 桌面应用，为本地 Markdown（含 Logseq）、PDF 及 Tika 支持的文档构建可搜索索引：混合 SQLite FTS5 精确检索、结构化评分与 LanceDB 向量搜索（BAAI/bge-m3，可选 reranker），支持事件驱动的实时监视与增量更新，检索结果带来源标签可直接核验。另提供只读 MCP 服务器包（stdio/Registry），AI 客户端可查询但不能构建或修改数据。CPU 执行可用，NVIDIA CUDA 为可选；首次需联网下载 Runtime、模型与 Java/Tika 组件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- FTS5+结构评分+LanceDB 向量搜索+可选 reranker 的混合检索
- Markdown/Logseq 感知，PDF 与 Tika 扩展索引（目录含 1,290 种格式）
- 事件驱动 live watch 与可配置静默期的增量更新
- 只读 MCP 服务器（omniclip.status / omniclip.search 两个工具）

## 适用场景

- 在本地检索自己的 Markdown 笔记与 PDF 文档并核验来源
- 通过 MCP 把私有知识库接入 AI 客户端做问答
- 笔记编辑后自动增量更新索引

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: **A local-first Windows desktop app and read-only MCP server for searching private Markdown, PDF, and Tika-backed kn
> L22: Caelune builds searchable indexes from knowledge you already keep on your own computer. It combines exact-text retr
> L72: - **Hybrid retrieval** — combines SQLite FTS5, structure-aware scoring, LanceDB vector search, `BAAI/bge-m3`, and o

## 星数曲线

```mermaid
xychart-beta
    title "EllisMorrow/Caelune 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-26 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0887fc048d8d` · [字段定义](../../DATASET.md)*
