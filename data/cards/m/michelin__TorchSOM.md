# michelin/TorchSOM

⭐ 42 · Python · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/michelin/TorchSOM) · [官网](https://opensource.michelin.io/TorchSOM/) · 组织维护

**Michelin 维护的 PyTorch 自组织映射库，GPU 加速训练与聚类可视化**

由米其林团队维护、发表于 JMLR 2026 的自组织映射（SOM）Python 库：基于 PyTorch CUDA 后端做 GPU 加速训练，提供 scikit-learn 风格 API、矩形/六边形拓扑可视化（U-Matrix、Hit Map 等）、在 SOM 潜空间上的聚类（K-Means/GMM/HDBSCAN）以及用于监督回归分类的 Just-In-Time Learning。README 给出与 MiniSom、somoclu 等的基准对比数据；PBC/层级变体标注为进行中。面向研究与工业场景，配有教程 notebook 与文档站。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch CUDA 后端的 GPU 加速 SOM 训练
- SOM 潜空间上的 K-Means/GMM/HDBSCAN 聚类
- 矩形与六进制拓扑的可视化工具集
- Just-In-Time Learning 支持监督回归与分类

## 适用场景

- 高维数据的降维、聚类与可视化分析
- 在 GPU 上训练 SOM 并对结果做聚类评估
- 基于 SOM 拓扑的在线查询局部监督学习（JITL）

## 场景标签

 · 领域:机器学习/聚类与降维

## 证据(README 行号)

> L33: - **GPU-accelerated training** via PyTorch CUDA backend
> L34: - **Advanced clustering** (K-Means, GMM, HDBSCAN) on the SOM latent space
> L39: This library accompanies the paper *torchsom: The Reference PyTorch Library for Self-Organizing Maps* (Berthier et 

## 星数曲线

```mermaid
xychart-beta
    title "michelin/TorchSOM 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-19 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f77bfceb4221` · [字段定义](../../DATASET.md)*
