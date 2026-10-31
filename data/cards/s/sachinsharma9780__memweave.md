# sachinsharma9780/memweave

⭐ 54 · Python · MIT · 推送 2026-05-10 · [GitHub](https://github.com/sachinsharma9780/memweave) · 个人维护

**给 AI agent 的持久化可检索记忆库，Markdown 文件存储**

异步优先的 Python 库，为 AI agent 提供长期记忆：记忆以纯 Markdown 文件为数据源，SQLite（FTS5 + sqlite-vec）作为可重建的派生索引。搜索采用混合检索（0.7×向量 + 0.3×BM25），支持分数阈值、时间衰减（默认半衰期 30 天，evergreen 文件豁免）、MMR 去重重排及自定义后处理器。核心读写与检索操作不调用 LLM，嵌入按内容哈希缓存，无嵌入 API 时退化为纯关键词检索，可完全离线运行。支持 agent 命名空间隔离与来源标签过滤。以 pip 包形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Markdown 为数据源、SQLite 为派生索引，支持 git diff 审计记忆变化
- BM25 + 向量混合检索，权重可调
- 核心操作零 LLM 调用，嵌入按内容哈希缓存，可离线降级为关键词检索
- 时间衰减、MMR 重排与自定义后处理器均以插件机制接入

## 适用场景

- 为多 agent 系统提供隔离命名空间的长期记忆
- 希望用 git 版本化管理 agent 记忆并可直接编辑 Markdown
- 在无向量数据库、无云服务的环境下为 agent 检索历史上下文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L14: memweave is a zero-infrastructure, async-first Python library that gives AI agents persistent, searchable memory — 
> L55: - 🔍 **Hybrid search out of the box.** Combines BM25 keyword ranking (FTS5) with semantic vector search (sqlite-vec)
> L59: - 🔌 **Pluggable at every layer.** Swap in a custom search strategy, add a post-processing step, or bring your own e

## 星数曲线

```mermaid
xychart-beta
    title "sachinsharma9780/memweave 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-31 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e5a2029876dd` · [字段定义](../../DATASET.md)*
