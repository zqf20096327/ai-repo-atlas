# VectorDB-NTU/RaBitQ-Library

⭐ 291 · C++ · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/VectorDB-NTU/RaBitQ-Library) · [官网](https://vectordb-ntu.github.io/RaBitQ-Library/) · 组织维护

**RaBitQ 向量量化与近邻搜索的官方轻量 C++/Python 库**

RaBitQ 论文算法的官方实现库，提供向量量化与近似最近邻搜索：内置 IVF、HNSW、SymphonyQG 三种索引，支持 L2 与内积（向量归一化后可做余弦），并提供可嵌入自建搜索引擎的量化组件（core 与 FastScan）。面向构建向量检索系统的开发与研究人员，C++17 组件加 Python 绑定，pip 即装。限制：SymphonyQG 更新需重建索引，量化结果为近似值。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种内置索引：IVF / HNSW / SymphonyQG，各具 QPS–召回权衡
- 可独立嵌入自有引擎的量化组件（core 编码与距离估计、FastScan 批量打分）
- 支持 1–9-bit 量化码，CPython 3.11–3.14 多平台 wheel
- Apache 2.0 许可，含论文支撑

## 适用场景

- 在应用中构建和查询量化向量索引
- 把 RaBitQ 量化集成进自己的存储与搜索引擎
- 对比 IVF/HNSW/SymphonyQG 的存储与 QPS–召回权衡

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L20: RaBitQ-Library is a research-backed library for vector quantization and
> L96: Integrate encoding and distance estimation into your own storage and search

## 星数曲线

```mermaid
xychart-beta
    title "VectorDB-NTU/RaBitQ-Library 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 290 --> 292
    line [291, 291]
```

2026-10-18 291 → 2026-10-25 291（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `83cefca67b38` · [字段定义](../../DATASET.md)*
