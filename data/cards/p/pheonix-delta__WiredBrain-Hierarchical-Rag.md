# pheonix-delta/WiredBrain-Hierarchical-Rag

⭐ 40 · Python · NOASSERTION · 推送 2026-02-11 · [GitHub](https://github.com/pheonix-delta/WiredBrain-Hierarchical-Rag) · 组织维护

**面向低显存消费级硬件的分层 RAG 架构研究原型**

研究原型（AGPLv3，另有商业许可），提出分层 3 地址（Gate/Branch/Topic/Level）RAG 架构：用 SetFit 做意图分类路由，将 693K 知识块的检索空间缩减到约 20 块/查询；融合向量检索（Qdrant HNSW）、图遍历（PostgreSQL，688K 关系）与分层过滤三种方式，并含 Transparent Reasoning Module（TRM）做置信度检查与证据缺口检测。目标硬件为 GTX 1650（4GB VRAM），声明本地部署零云成本。文档以论文、架构说明与 Mermaid 图形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 分层 3 地址路由将 693K 块的检索空间缩减 99.997%（约 20 块/查询）
- 向量+图+分层过滤的混合检索融合
- SetFit 意图分类路由（76.67% 准确率，<50ms）
- TRM 置信度检查与“证据缺口检测”回退机制

## 适用场景

- 在 4GB 显存消费级 GPU 上搭建大规模本地知识检索
- 需要可追溯推理步骤与证据缺口提示的高风险问答场景
- 研究分层路由与混合检索在 RAG 中的效果

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: ### Hierarchical RAG scaling to 693K chunks on consumer hardware
> L54: We present **WiredBrain**, a novel hierarchical RAG architecture that addresses these limitations through intellige
> L291: Query → [Vector Search] → Semantic Similarity (Qdrant HNSW)

## 星数曲线

```mermaid
xychart-beta
    title "pheonix-delta/WiredBrain-Hierarchical-Rag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-26 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d9e753394d23` · [字段定义](../../DATASET.md)*
