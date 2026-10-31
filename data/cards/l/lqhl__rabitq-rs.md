# lqhl/rabitq-rs

⭐ 19 · Rust · Apache-2.0 · 推送 2026-02-26 · [GitHub](https://github.com/lqhl/rabitq-rs) · [官网](https://crates.io/crates/rabitq-rs) · 个人维护

**RaBitQ 量化与 IVF/MSTG 向量索引的纯 Rust 实现**

面向开发者的 Rust 向量量化与近似最近邻搜索库：实现 RaBitQ 二值量化（结合 IVF 倒排索引）与 MSTG 多尺度树图索引（层级聚类 + HNSW 图导航），宣称最高 32 倍内存压缩。提供内置 k-means 训练、FAISS 兼容的预聚类导入、索引持久化（带 CRC32 校验）、SIMD 加速与 faster_config 快速构建模式；另含 Python 绑定（maturin 构建）、CLI 基准测试工具与 ann-benchmarks 封装。限制：ARM64 平台存在距离计算错误，README 不推荐在该平台生产使用。

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

- RaBitQ 量化 + IVF 与 MSTG 两种索引结构
- 支持 FAISS 预聚类质心导入与内置 k-means 训练
- 提供 Python 绑定与 ann-benchmarks 标准评测封装
- faster_config 模式加速索引构建，索引保存带 CRC32 校验

## 适用场景

- 在大规模向量集合上构建低内存占用的 ANN 索引
- 复用 FAISS 已有聚类结果进行 RaBitQ 量化索引训练
- 在 ann-benchmarks 上评测 MSTG 索引的召回与 QPS

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L9: Pure Rust implementation of advanced vector quantization and search algorithms:
> L48: ### When to Use MSTG vs IVF+RaBitQ
> L244: RaBitQ-RS provides Python bindings for the MSTG (Multi-Scale Tree Graph) index, enabling seamless integration with

## 星数曲线

```mermaid
xychart-beta
    title "lqhl/rabitq-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `0ea7a3165d53` · [字段定义](../../DATASET.md)*
