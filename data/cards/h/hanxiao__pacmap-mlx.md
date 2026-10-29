# hanxiao/pacmap-mlx

⭐ 21 · Python · MIT · 推送 2026-03-05 · [GitHub](https://github.com/hanxiao/pacmap-mlx) · 个人维护

**Apple Silicon 上纯 MLX 实现的 PaCMAP 降维库**

PaCMAP（Pairwise Controlled Manifold Approximation）的纯 MLX 实现，面向 Apple Silicon 用户：仅依赖 MLX 与 numpy，不使用 scipy/numba/annoy，KNN 与梯度优化均在 Metal GPU 上运行，KNN 采用精确暴力配对距离。README 给出参数表、三阶段权重调度原理说明与 API 用法。注意：仓库已合并入 mlx-vis，README 声明不再单独维护，建议改装 mlx-vis。安装经 uv pip 从 git 仓库或源码进行。

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

- 纯 MLX + numpy 实现，无 scipy/numba/annoy 依赖
- KNN 与优化在 Metal GPU 上运行（精确暴力配对距离）
- 支持 n_neighbors、MN_ratio、FP_ratio、三阶段迭代等参数
- 输入超 100 维时自动 PCA 降至 100 维

## 适用场景

- 在 Mac 上对高维数据做快速降维可视化
- 需要保留全局结构的流形学习嵌入生成
- 已有 numpy 数组输入的 sklearn 风格 fit_transform 工作流

## 场景标签

 · 领域:机器学习/降维可视化

## 证据(README 行号)

> L6: Pure MLX implementation of PaCMAP (Pairwise Controlled Manifold Approximation) for Apple Silicon GPU.
> L8: No scipy, no numba, no annoy. Just MLX + numpy.

## 星数曲线

```mermaid
xychart-beta
    title "hanxiao/pacmap-mlx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2c355a4a565b` · [字段定义](../../DATASET.md)*
