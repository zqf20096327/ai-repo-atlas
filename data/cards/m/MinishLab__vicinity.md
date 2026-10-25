# MinishLab/vicinity

⭐ 352 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/MinishLab/vicinity) · [官网](https://minish.ai/packages/vicinity/introduction) · 组织维护

**轻量向量检索库：统一接口适配多种近邻搜索后端**

低依赖的 Python 向量存储与最近邻检索库，为 BASIC、HNSW（hnswlib）、Usearch、Annoy、PyNNDescent、FAISS（8 种索引类型）和 Voyager 提供统一接口，支持多种距离度量与后端参数配置。向量库可序列化保存/加载，并可推送到 Hugging Face Hub。内置评测功能，可测量各后端的每秒查询数与召回率。限制：ANN 后端不支持动态删除（需重建索引），仅 FAISS/HNSW/Usearch 支持插入。面向需要实验比较不同索引方案的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 类后端的统一检索接口，含 FAISS 8 种索引类型
- 内置评测：测量各后端每秒查询数与召回率
- 向量库可保存/加载并推送至 Hugging Face Hub
- 低依赖、MIT 许可

## 适用场景

- 统一接口下实验比较不同 ANN 索引方案
- 保存向量库并托管到 Hugging Face Hub 供复用
- 评估各后端在我的数据上的召回率与速度

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L24: Vicinity is a light-weight, low-dependency vector store. It provides a simple and intuitive interface for nearest n
> L28: This is where Vicinity comes in. Instead of learning a new interface for each new package or backend, Vicinity prov

## 星数曲线

```mermaid
xychart-beta
    title "MinishLab/vicinity 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 350 --> 353
    line [351, 352, 352]
```

2026-10-18 351 → 2026-10-25 352（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `73cf482334de` · [字段定义](../../DATASET.md)*
