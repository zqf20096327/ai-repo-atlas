# microsoft/Swin3D

⭐ 299 · Cuda · MIT · 推送 2026-08-25 · [GitHub](https://github.com/microsoft/Swin3D) · 组织维护

**3D 室内场景理解的预训练 Transformer 骨干网络**

微软研究团队发布的 3D Swin Transformer 骨干网络：针对稀疏体素设计线性内存复杂度的自注意力机制，通过广义上下文相对位置编码（cRSE）捕捉点云信号的不规则性。在合成数据集 Structured3D 上预训练，提供 Swin3D-S/L 两种规模模型，可在 ScanNet、S3DIS 的语义分割与 3D 检测任务上微调，检测任务与 FCAF3D、CAGroup3D 框架结合。以 Python 包源码安装方式提供，需自行准备数据集。

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

- 3D Swin transformer 在稀疏体素上实现线性内存复杂度自注意力
- 在 Structured3D（约为 ScanNet 10 倍规模）上预训练的 Swin3D-S/L 模型
- 支持 ScanNet/S3DIS 语义分割与 3D 检测下游任务微调
- 提供不同 cRSE 配置（XYZ,RGB / XYZ,RGB,NORM）的预训练权重

## 适用场景

- 在 ScanNet 或 S3DIS 上微调做 3D 语义分割
- 结合 FCAF3D/CAGroup3D 做 3D 目标检测
- 作为 3D 点云理解任务的预训练骨干网络

## 场景标签

`目标检测` `微调` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L20: We present a pretrained 3D backbone, named Swin3D, that first-time outperforms all state-of-the-art methods on down
> L15: 1. Pretrained models on Structured3D are provided.

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Swin3D 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 298 --> 300
    line [299, 299]
```

2026-10-18 299 → 2026-10-23 299（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c3a03353d789` · [字段定义](../../DATASET.md)*
