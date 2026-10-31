# sfu-mial/QG-SSL

⭐ 14 · Python · MIT · 推送 2026-06-04 · [GitHub](https://github.com/sfu-mial/QG-SSL) · 组织维护

**质量引导的医学图像半监督分割训练方法（MICCAI 2026）**

面向医学图像分割的半监督学习研究代码（PyTorch，Python 3.10）：训练一个基于可变质量掩码的分割质量预测器 g_φ，冻结后通过两种机制（QAR 可微质量感知正则化、PL-QW 基于质量分数的伪标签加权）引导分割网络 f_θ 在无标注数据上的半监督训练，可作为现有半监督框架的即插增强。两阶段 shell 脚本运行，实验覆盖皮肤镜与结肠镜数据集（PH2、SCD、ISIC2020、CVC-ClinicDB 等），需自行下载数据与 Swin-UNet 预训练权重；预训练权重计划上传 HuggingFace（尚未提供）。

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

- 质量预测器 g_φ 从图像-掩码对估计分割质量，无需 ground truth
- QAR 可微正则化与 PL-QW 伪标签加权两种即插式机制
- 两阶段脚本化训练（train_mq.sh / train_SSL_methods.sh）
- 实验覆盖皮肤科与结肠镜多组标注/无标注数据集

## 适用场景

- 在标注稀缺的医学影像上做半监督分割训练
- 为现有半监督分割框架添加质量引导增强
- 复现 MICCAI 论文在皮肤镜/结肠镜数据上的实验

## 场景标签

`目标检测` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L7: A quality-guided approach to semi-supervised medical image segmentation. A dedicated segmentation quality predictor 
> L8: - **QAR**: a differentiable quality-aware regularization that encourages f &theta; to produce masks that g &phi; sco
> L9: - **PL-QW**: quality-based pseudolabel reweighting that uses g &phi; 's score of each pseudolabel as a sample weight

## 星数曲线

```mermaid
xychart-beta
    title "sfu-mial/QG-SSL 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e4674a989113` · [字段定义](../../DATASET.md)*
