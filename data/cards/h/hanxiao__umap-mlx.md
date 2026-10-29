# hanxiao/umap-mlx

⭐ 46 · Python · MIT · 推送 2026-03-05 · [GitHub](https://github.com/hanxiao/umap-mlx) · 个人维护

**Apple Silicon 上纯 MLX 实现的 UMAP 降维库**

用 MLX 在 Apple Silicon 的 Metal GPU 上完整实现 UMAP 降维算法：精确 k-NN、逐点 sigma 二分搜索、谱初始化与编译 SGD 均在 GPU 上运行，依赖仅 mlx 与 numpy，不含 scipy/PyTorch。README 给出参数列表、性能数据（M3 Ultra 上 Fashion-MNIST 70K 约 3.4 秒，自称较 umap-learn 快 30-46 倍）及未来方向讨论。注意：仓库已并入 mlx-vis，README 声明不再单独维护，改用 pip install mlx-vis。

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

- UMAP 全流程在 Metal GPU 上运行的纯 MLX 实现
- 依赖仅 mlx 与 numpy，不含 scipy/PyTorch
- 提供 n_components/n_neighbors/min_dist 等参数与可复现随机种子
- 仓库已合并入 mlx-vis，单独仓库停止维护

## 适用场景

- 在 Mac 上对高维数据做快速 UMAP 降维与可视化
- 需要避免 scipy/PyTorch 依赖的 Apple Silicon 环境下做嵌入可视化
- 对比 UMAP/t-SNE/PaCMAP 的降维效果

## 场景标签

 · 领域:机器学习/降维可视化

## 证据(README 行号)

> L6: UMAP in pure MLX for Apple Silicon. Entire pipeline runs on Metal GPU.
> L8: 30-46x faster than umap-learn. Fashion-MNIST 70K in 3.4 seconds for 500 epochs.

## 星数曲线

```mermaid
xychart-beta
    title "hanxiao/umap-mlx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-29 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8e13a7ebbda5` · [字段定义](../../DATASET.md)*
