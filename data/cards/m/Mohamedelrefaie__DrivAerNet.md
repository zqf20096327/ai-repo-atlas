# Mohamedelrefaie/DrivAerNet

⭐ 555 · Python · NOASSERTION · 推送 2026-05-14 · [GitHub](https://github.com/Mohamedelrefaie/DrivAerNet) · 组织维护

**8,150 个汽车设计的 CFD 仿真多模态数据集与深度学习基准**

DrivAerNet++ 提供涵盖 fastback、notchback、estateback 等构型的 8,150 个汽车设计的高保真 CFD 仿真数据，每个 3D 几何由 26 个参数描述。模态包括参数化模型、体/表面流场、点云、网格、气动系数（Cd/Cl）、29 类部件标注、渲染图与手绘草图，托管于 Harvard Dataverse，总规模 39 TB，通过 Globus 下载。数据集 CC BY-NC 4.0 许可（禁止商用），代码为 MIT，由 MIT DeCoDE Lab 维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8,150 个汽车设计的高保真 CFD 仿真数据，每个几何由 26 个参数描述
- 多模态内容：流场、点云、网格、气动系数、29 类部件标注、渲染图与草图
- 提供 train/val/test 划分与公开排行榜用于模型对比
- 已集成 NVIDIA Modulus 与 PaddleScience 框架示例

## 适用场景

- 训练预测汽车气动性能的代理模型，避免完整 CFD 仿真
- 气动驱动的汽车设计优化与生成式设计研究
- 3D 点云/网格上的表面场预测与部件分类研究
- 提交模型至排行榜与基线对比验证

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: We present **DrivAerNet++**, comprising **8,150 diverse car designs** modeled with high-fidelity computational flui
> L104: The dataset is hosted on **Harvard Dataverse** (CC BY-NC 4.0).
> L252:  Maintained by the DeCoDE Lab at MIT

## 星数曲线

```mermaid
xychart-beta
    title "Mohamedelrefaie/DrivAerNet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 553 --> 556
    line [554, 555, 555]
```

2026-10-18 554 → 2026-10-27 555（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `717cf19af360` · [字段定义](../../DATASET.md)*
