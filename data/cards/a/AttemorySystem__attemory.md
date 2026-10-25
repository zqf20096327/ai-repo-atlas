# AttemorySystem/attemory

⭐ 55 · C++ · MIT · 推送 2026-08-13 · [GitHub](https://github.com/AttemorySystem/attemory) · [官网](https://attemorysystem.github.io/) · 个人维护

**面向 AI agent 的注意力式语义检索引擎：长记忆与代码检索**

本地运行的检索服务，把原始语料（记忆、文档、代码块）索引为可复用的 KV 状态，再由本地 Qwen3.5 检索模型通过注意力机制在索引记忆上执行查询，返回记忆 id、文本片段或文件与行号范围。不依赖向量数据库、嵌入相似度或 BM25 作为核心检索器。提供 Python/HTTP API 与 `atcode` 代码搜索 CLI 两层用法，含 Claude Code 插件；支持 Linux/macOS、CUDA/Metal/CPU 后端，KV 缓存可持久化到磁盘。README 附带可复现的基准结果与脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 索引为 KV 状态、由本地模型注意力检索的机制，非向量/BM25 检索
- `atcode` CLI 索引仓库并返回文件与行号范围证据
- 提供 Claude Code 插件（attemory-code）
- 支持 kv_persist 将分段 KV 缓存持久化到磁盘

## 适用场景

- 为编码 agent 提供仓库级语义搜索，减少探索性 token 消耗
- 为长对话 agent 构建可检索的长期记忆
- 作为通用文档/自定义语料的检索引擎嵌入应用

## 场景标签

`Agent 记忆` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L8: It indexes raw corpora into reusable KV state, then retrieves evidence by
> L41: |**Retrieval engine**|long memory, documents, custom apps, benchmark adapters|Python API / HTTP API|

## 星数曲线

```mermaid
xychart-beta
    title "AttemorySystem/attemory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-25 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a3b8ab58fa19` · [字段定义](../../DATASET.md)*
