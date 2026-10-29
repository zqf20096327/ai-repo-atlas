# venkatasivanaga/FuelDeep3D

⭐ 22 · R · NOASSERTION · 推送 2026-03-04 · [GitHub](https://github.com/venkatasivanaga/FuelDeep3D) · 组织维护

**R 包：TLS 激光雷达点云深度学习推理的森林可燃物制图**

面向林火可燃物评估的 R 包，处理地面激光扫描（TLS）3D 森林点云：构建训练数据集、计算高度衍生特征（HAG）、切片与预处理大场景，通过 reticulate 调用 Python（pointnext conda 环境、PyTorch 后端）对 LAS/LAZ 逐点分类并写回燃料类别。支持用户自有标注数据训练模型、预测结果可视化、SOR 去噪，以及精度/混淆矩阵/F1 等评估输出。以 CRAN install.packages 或源码方式安装，需 Conda/Miniconda 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从原始 .las 到分类燃料层的完整工作流
- 通过 reticulate + conda（pointnext 环境）运行 PyTorch 深度学习模型
- 支持自有标注数据训练与预测写回 LAS/LAZ
- 提供混淆矩阵、Precision/Recall/F1 评估与 3D 可视化

## 适用场景

- 用 TLS 点云生成逐点燃料分类图层用于野火行为建模
- 在自己标注的森林点云上训练定制分割模型
- 对预测燃料类别做可视化、质控与精度评估

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L14: `FuelDeep3D` provides tools for processing, feature extraction, and classification of 3D forest point clouds for fu
> L27: - Enable users to train their own deep learning models on custom labeled datasets

## 星数曲线

```mermaid
xychart-beta
    title "venkatasivanaga/FuelDeep3D 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `75f3e5f482e1` · [字段定义](../../DATASET.md)*
