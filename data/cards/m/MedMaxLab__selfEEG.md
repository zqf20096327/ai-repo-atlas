# MedMaxLab/selfEEG

⭐ 75 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/MedMaxLab/selfEEG) · [官网](https://selfeeg.readthedocs.io/en/latest/) · 组织维护

**面向 EEG 数据自监督学习实验的 PyTorch 库**

基于 PyTorch 的 Python 库，用于在脑电（EEG）数据上开展自监督学习实验：提供 dataloading、GPU 数据增强、EEG 常用深度模型（EEGNet、DeepConvNet、STNet 等）、SSL 算法（SimCLR、SimSiam、MoCo、BYOL 等）与损失函数模块，覆盖从数据加载到预训练与微调的流程；多数功能也可用于其他信号类型。不提供 EEG 预处理（如 IC 剔除、ASR），仅含滤波、重采样等简单操作。通过 pip 或 conda 安装，配有示例 notebook 与官方文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 SimCLR/SimSiam/MoCo/BYOL 等自监督算法与可定制 fit 方法
- 收录 EEG 分析常用模型（EEGNet、DeepConvNet、ResNet、TinySleepNet、STNet 等）
- 数据增强全量支持 GPU 执行
- 附带早停与微调工具函数

## 适用场景

- 在 EEG 数据集上做自监督预训练再微调下游任务
- 复用 EEG 深度模型与 GPU 数据增强搭建训练管线
- 将 SSL 流程扩展到其他生理信号分析

## 场景标签

`微调` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L9: selfEEG is a pytorch-based library designed to facilitate self-supervised learning
> L23: 7. **ssl** - collection of self-supervised algorithms with a highly customizable

## 星数曲线

```mermaid
xychart-beta
    title "MedMaxLab/selfEEG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-25 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0af9c76a6c60` · [字段定义](../../DATASET.md)*
