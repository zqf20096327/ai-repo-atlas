# EmmanuelleB985/UK_BOB

⭐ 52 · Python · MIT · 推送 2026-03-29 · [GitHub](https://github.com/EmmanuelleB985/UK_BOB) · [官网](https://emmanuelleb985.github.io/ukbob/) · 组织维护

**3D MRI 分割数据集与 Swin-BOB 基础模型（ICCV 2025）**

面向医学影像研究者的 3D MRI 分割工作：提供含 51,761 样本、13.7 亿分割掩码、72 个解剖结构的 UKBOB 数据集，以及基于 Swin-UNetr 的基础模型 Swin-BOB（约 62M 参数），支持单/多 GPU 分布式训练与梯度检查点。含 SOLF 器官标签自动质检过滤管线与基于熵的测试时自适应（ETTA）推理，评估覆盖 Dice、HD95 等指标。运行需 Python 3.8+、CUDA 11.8+，训练要求 32GB+ 显存、128GB+ 内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 51,761 个 3D MRI 样本与 13.7 亿分割掩码、72 个解剖结构
- Swin-UNetr 架构的 Swin-BOB 模型，约 62M 参数
- SOLF 器官标签过滤管线做训练数据质检
- ETTA 基于熵的测试时自适应推理

## 适用场景

- 在 BRATS/BTCV 等基准上训练与评测 3D 医学影像分割模型
- 获取大规模多器官标注 MRI 数据用于研究
- 在新领域数据上做测试时自适应分割推理

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L15: UKBOB represents a breakthrough in medical image segmentation, introducing the largest-scale 3D MRI dataset to date
> L39: Input (96×96×96) → Swin-UNetr Encoder → Bottleneck → Decoder → Output (72 channels)

## 星数曲线

```mermaid
xychart-beta
    title "EmmanuelleB985/UK_BOB 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-24 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1f682839d64a` · [字段定义](../../DATASET.md)*
