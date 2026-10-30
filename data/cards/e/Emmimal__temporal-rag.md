# Emmimal/temporal-rag

⭐ 53 · Python · MIT · 推送 2026-05-15 · [GitHub](https://github.com/Emmimal/temporal-rag) · 个人维护

**RAG 检索后时间层：过期过滤、时间衰减与混合重排**

嵌入在向量检索与 LLM 之间的 Python 后处理层：先按 valid_until 硬性移除 EXPIRED 文档，再对候选做 STATIC/VERSIONED/EVENT 三类分类、指数时间衰减（0.5^(age/half_life)）、新鲜度评分与相关性门槛，最终混合重排。附带 PAIR 执行、冲突检测、置信分级等八个进阶模式与领域衰减模板。仅依赖 numpy，demo 用确定性 TF-IDF 嵌入无需 API key；已知限制包括无显式过期日期的文档不能自动移除、内存态无跨会话持久化、稠密嵌入需重校准阈值。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检索后管线：有效期过滤 + 文档分类 + 指数衰减 + 混合重排
- 仅依赖 numpy，无 API key，demo 输出确定性可复现
- advanced.py 提供八个生产模式（PAIR 执行、冲突检测、失败审计日志等）
- 按领域预配置的衰减模板与衰减下限（DECAY_PROFILES/DECAY_FLOORS）

## 适用场景

- 知识库频繁更新时避免 LLM 引用已过期或被取代的文档
- 让停机公告等时间窗口型信息优先呈现
- 多版本文档场景下不让 LLM 同时看到冲突版本

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L2: A post-retrieval temporal layer for RAG systems — validity filtering, time decay, and freshness tracking that runs d
> L15: Query → Vector Retriever → Temporal Layer → Re-ranked Context → LLM

## 星数曲线

```mermaid
xychart-beta
    title "Emmimal/temporal-rag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-18 52 → 2026-10-30 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c2e88df143d1` · [字段定义](../../DATASET.md)*
