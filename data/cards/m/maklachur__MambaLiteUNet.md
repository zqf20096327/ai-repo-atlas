# maklachur/MambaLiteUNet

⭐ 42 · Python · 推送 2026-08-11 · [GitHub](https://github.com/maklachur/MambaLiteUNet) · [官网](https://openaccess.thecvf.com/content/CVPR2026/html/Rahman_MambaLiteUNet_Cross-Gated_Adaptive_Feature_Fusion_for_Robust_Skin_Lesion_Segmentation_CVPR_2026_paper.html) · 组织维护

**CVPR 2026 论文官方代码：皮肤病变分割模型 MambaLiteUNet**

论文 'MambaLiteUNet: Cross-Gated Adaptive Feature Fusion for Robust Skin Lesion Segmentation' 的官方仓库，作者来自德州农工相关团队。基于 Mamba/状态空间模型的轻量级 U 形分割网络，提供环境搭建、依赖安装、数据集准备（ISIC2017/2018、HAM10000、PH2 及自定义数据）、训练与测试脚本。需 Python 3.9 Conda 环境、PyTorch 2.6.0+cu118 与 CUDA 11.8，部分旧依赖需另建 Python 3.7 环境处理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Mamba（SSM）的皮肤病变分割网络官方实现
- 提供 ISIC2017/2018、HAM10000、PH2 数据准备脚本
- 训练脚本默认在 epoch 末自动运行测试，输出至 ./results/
- 支持自定义数据集的组织与划分

## 适用场景

- 复现论文的皮肤病变分割训练与测试流程
- 在自有医学影像数据上训练轻量级分割模型
- 对比 Mamba 架构在医学分割任务中的用法

## 场景标签

 · 领域:医学影像/计算机视觉

## 证据(README 行号)

> L3: This is the official repository for **MambaLiteUNet: Cross-Gated Adaptive Feature Fusion for Robust Skin Lesion Segm
> L6:  MambaLiteUNet CVPR 2026 Poster

## 星数曲线

```mermaid
xychart-beta
    title "maklachur/MambaLiteUNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-30 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `5acd1d270e11` · [字段定义](../../DATASET.md)*
