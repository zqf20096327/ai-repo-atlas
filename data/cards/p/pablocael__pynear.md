# pablocael/pynear

⭐ 45 · C++ · MIT · 推送 2026-10-08 · [GitHub](https://github.com/pablocael/pynear) · 个人维护

**度量空间近邻搜索 Python 库：二进制/精确/量化 ANN 索引**

以 C++ 为核心、NumPy 单一 API 的最近邻搜索库，提供三类索引：二进制描述符的 Multi-Index Hashing（MIH，半径内候选完备保证）及 MIH-seeded HNSW，支持 HNSW 浮点与 int8 量化（SQ8）ANN，以及 VP-tree 精确搜索（约 256 维内，支持 L2/L1/Chebyshev/cosine/Hamming），另有 BK-tree 阈值查询与 scikit-learn 适配器。面向 CPU 工作负载，SIMD 支持 x86(AVX2) 与 ARM(NEON)，除 NumPy 外无原生依赖，pip 预编译 wheel 安装。README 含与 Faiss 的逐项基准对比（双方各有胜出的场景）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MIH 二进制近重复检索，半径内候选完备保证
- VP-tree 精确 k-NN（L2/L1/Chebyshev/cosine/Hamming）
- HNSW int8(SQ8) 量化，向量内存为 float32 的四分之一
- scikit-learn 适配器（fit/predict/kneighbors）可直接替换

## 适用场景

- 图像/视频去重与抄袭检测（感知哈希、ORB/BRIEF）
- RAG 语义检索的向量索引
- 需要精确近邻的 CV 特征匹配与 ANN ground truth
- 把现有 sklearn KNN 分类器换成本地索引后端

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L29: Search, recommendation, deduplication, and retrieval-augmented generation all
> L55: - **Semantic & RAG retrieval**: text/image embeddings + `IVFFlatCosineIndex`.

## 星数曲线

```mermaid
xychart-beta
    title "pablocael/pynear 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-29 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ddfa79f61806` · [字段定义](../../DATASET.md)*
