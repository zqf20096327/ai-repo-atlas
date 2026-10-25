# ZombaSY/FSG-Net-pytorch

⭐ 39 · Python · 推送 2026-01-06 · [GitHub](https://github.com/ZombaSY/FSG-Net-pytorch) · 组织维护

**视网膜血管分割网络 FSG-Net 的官方 PyTorch 实现**

论文 "Full-scale Representation Guided Network for Retinal Vessel Segmentation" 的官方实现：提供在 DRIVE、STARE、CHASE_DB1、HRF 四个数据集上的训练与推理流程，通过 configs/train.yml 与 inference.yml 配置路径和超参数，以 bash_train.sh 和 bash_inference.sh 运行；Releases 页面提供各数据集预训练模型。要求输入与标签文件按文件名排序且一一对应，测试环境为 Ubuntu 22.04、RTX 4090、CUDA 12.4、PyTorch 2.4.1。面向复现论文或做视网膜血管分割的科研人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 DRIVE/STARE/CHASE_DB1/HRF 四个数据集的训练与推理流程
- Releases 提供各数据集官方预训练模型
- 支持可选 WandB 训练监控
- 报告各数据集的 mIoU/F1/AUC 等指标

## 适用场景

- 复现论文中的视网膜血管分割结果
- 用预训练模型对自己的眼底图像做血管分割推理
- 在自己的视网膜数据集上训练分割模型

## 场景标签

`目标检测` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L1: # 🩺 FSG-Net: Full-scale Representation Guided Network for Retinal Vessel Segmentation
> L25: Comprehensive evaluation across multiple retinal vessel segmentation datasets:
> L75: bash bash_train.sh

## 星数曲线

```mermaid
xychart-beta
    title "ZombaSY/FSG-Net-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `eddeedba99f7` · [字段定义](../../DATASET.md)*
