# ranajahanzaib/plasma-flux-explorer

⭐ 3 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/ranajahanzaib/plasma-flux-explorer) · 个人维护

**面向聚变研究人员的托卡马克平衡数据本地可视化工作站**

本地优先的科学工作站，用于探索 Sophelio Fusion Equilibrium Challenge 发布的托卡马克平衡记录（DIII-D、MAST）。提供 2D 极向场交互可视化、3D 轴对称磁面重建、跨装置对比（形状参数差与 Hausdorff 距离）、边界几何参数提取（拉长比、三角性等 18 项 SI 参数），以及对导入的 JSON 模型预测做残差验证，并严格执行数据集划分与实验数据溯源。基于 Next.js 与 Python 模块，完全离线运行，无外部 API key，可选部署到 Cloudflare Workers。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 交互式 2D 极向磁场查看器：marching-squares 等值线、磁面/LCFS/X点图层切换
- 3D 轴对称磁面重建与跨装置共享物理尺度对比（含 Hausdorff 距离）
- 模型预测实验室：会话内 JSON 导入、结构校验与 |Δψ| 残差可视化
- 零云架构：本地 Parquet 归档 + JSON 目录缓存，完全离线可用

## 适用场景

- 离线浏览与校验托卡马克放电记录的 EFIT 重建通量数据
- 对比 DIII-D 与 MAST 的等离子体边界几何形状参数
- 在不执行代码的情况下核验外部模型预测与实验重建的差异
- 为 ML 基准评测保留溯源、避免对隐去标签的划分计算指标

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L5: Plasma Flux Explorer is a local-first scientific workstation for exploring released tokamak equilibrium records from
> L27: - **Model Prediction Laboratory:** Session-only JSON prediction import with structural validation (grid dimensions,
> L28: - **Zero-Cloud Architecture:** Works completely offline using local Parquet archives and JSON catalog caches, with 

## 星数曲线

```mermaid
xychart-beta
    title "ranajahanzaib/plasma-flux-explorer 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `c083b2e52ff3` · [字段定义](../../DATASET.md)*
