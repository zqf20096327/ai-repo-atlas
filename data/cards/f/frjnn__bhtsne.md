# frjnn/bhtsne

⭐ 95 · Rust · MIT · 推送 2026-08-31 · [GitHub](https://github.com/frjnn/bhtsne) · [官网](https://docs.rs/bhtsne) · 个人维护

**Rust 编写的并行 Barnes-Hut t-SNE 降维库**

以 Rust 实现的 t-SNE 降维算法库，提供三种拟合路径：Barnes-Hut 树加速版本（支持 D=2~7 维嵌入）、精确原始算法版本、以及 FFT 加速的 FIt-SNE 路径（D=1 或 2，每 epoch O(n)）。支持自定义数据类型与自定义距离度量，基于 rayon 并行、按可用 CPU 数使用线程。以 Cargo crate 形式分发（v0.7.12），附带 API 文档与示例；另将 Morton Z-order 线性树抽为独立 crate（barnes-hut-tree）可单独复用。限制：Barnes-Hut 路径仅支持 2~7 维嵌入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Barnes-Hut 树加速、精确算法与 FIt-SNE 三种拟合路径
- 支持自定义数据类型与自定义距离度量（如字符串）
- 基于 rayon 并行，线程数等于可用 CPU 数
- Z-order 线性树抽出为独立 crate（barnes-hut-tree）可复用

## 适用场景

- 高维向量数据降维到 2D/3D 用于可视化
- 大规格数据集（数万点以上）用 FIt-SNE 路径加速嵌入
- 需要在自有力近似问题中复用 Morton Z-order 树结构

## 场景标签

 · 领域:机器学习/降维可视化

## 证据(README 行号)

> L9: Parallel Barnes-Hut and exact implementations of the t-SNE algorithm written in Rust. The tree-accelerated version o
> L42: For larger datasets the crate also provides `fit_sne` and `fit_sne_with_neighbors`, an FFT-accelerated, interpolati

## 星数曲线

```mermaid
xychart-beta
    title "frjnn/bhtsne 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-31 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `704946fab3c7` · [字段定义](../../DATASET.md)*
