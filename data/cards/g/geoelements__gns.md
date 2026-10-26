# geoelements/gns

⭐ 240 · Python · NOASSERTION · 推送 2026-03-27 · [GitHub](https://github.com/geoelements/gns) · [官网](https://www.geoelements.org/gns/) · 组织维护

**GNN 代理模拟器：模拟颗粒与流体系统替代数值方法**

UT Austin 团队维护的基于图神经网络（GNN）的机器学习代理模拟器，包含 GNS（颗粒/流体领域，可作为物质点法、光滑粒子流体动力学、CFD 等数值方法的替代）与 MeshNet（面向有限元、CFD、有限差分等网格模型）。提供训练、rollout 预测与渲染命令行流程，使用 numpy .npz 格式数据，支持分布式数据并行的多 GPU/多节点训练，可处理复杂边界条件与多材料交互。通过 conda/pip 安装，依赖 PyTorch Geometric，数据集托管于 DesignSafe。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GNS 覆盖颗粒/流体领域，MeshNet 覆盖 FEA/CFD/FDM 网格模型
- 分布式数据并行的多 GPU 与多节点训练
- rollout 预测输出可渲染为 gif/.vtu（ParaView 可视化）
- 提供 WaterDropSample/Sand/SandRamps 等训练数据集（DesignSafe）

## 适用场景

- 用 GNN 代理模拟替代 MPM/SPH/CFD 数值仿真
- 训练并预测颗粒介质（砂土等）或流体流动的演化
- 在多 GPU 集群上并行训练模拟器

## 场景标签

 · 领域:科学计算/物理仿真

## 证据(README 行号)

> L12: Graph Network-based Simulator (GNS) is a generalizable, efficient, and accurate machine learning (ML)-based surroga
> L14: MeshNet is a scalable surrogate simulator for any mesh-based models like Finite Element Analysis (FEA), Computation

## 星数曲线

```mermaid
xychart-beta
    title "geoelements/gns 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 239 --> 241
    line [240, 240]
```

2026-10-18 240 → 2026-10-26 240（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6c7a5a78cbbe` · [字段定义](../../DATASET.md)*
