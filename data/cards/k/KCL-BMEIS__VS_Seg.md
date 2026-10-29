# KCL-BMEIS/VS_Seg

⭐ 49 · Python · Apache-2.0 · 推送 2026-01-06 · [GitHub](https://github.com/KCL-BMEIS/VS_Seg) · 组织维护

**基于 MONAI/PyTorch 的前庭神经鞘瘤 MRI 自动分割脚本集**

提供 3D T1/T2 MRI 影像中前庭神经鞘瘤的深度学习分割训练与推理脚本，基于 MONAI 实现，网络在原论文基础上有残差连接、卷积下采样、dropout 等改动。配套公开 TCIA 数据集（需 DICOM 转 NIFTI 预处理），提供训练/推理 CLI、TensorBoard 进度监控与基于 T1/T2 的已训练模型下载（Zenodo）。运行需 CUDA GPU（≥4GB）、CUDA Toolkit、cuDNN，建议 Python 3.6、PyTorch 1.6、MONAI 0.4，在 Ubuntu 20.04 测试。

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

- 支持 T1 或 T2 3D MRI 的分割训练与推理
- 网络含残差连接、注意力模块与硬度加权损失（可用参数关闭）
- 提供 Zenodo 上的已训练模型与推理结果下载
- 训练进度可用 TensorBoard 监控，输出 Dice 评分

## 适用场景

- 医学影像研究者复现或改进前庭神经鞘瘤分割基线
- 在 TCIA 公开数据集上训练并评估分割模型
- 下载已训练模型对 T1/T2 测试集重跑推理

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository provides scripts for the segmentation of vestibular schwannoma on 3D T1 or T2 images,
> L34: The implementation is based on MONAI and the network has a couple of differences

## 星数曲线

```mermaid
xychart-beta
    title "KCL-BMEIS/VS_Seg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-29 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `63abc039bb13` · [字段定义](../../DATASET.md)*
