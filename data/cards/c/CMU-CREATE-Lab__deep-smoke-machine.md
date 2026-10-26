# CMU-CREATE-Lab/deep-smoke-machine

⭐ 125 · Python · BSD-3-Clause · 推送 2026-03-23 · [GitHub](https://github.com/CMU-CREATE-Lab/deep-smoke-machine) · [官网](http://smoke.createlab.org) · 组织维护

**识别工业烟尘排放的深度学习模型与视频数据集**

Project RISE 的代码与数据集发布仓库：基于 I3D（Two-Stream Inflated 3D ConvNet）和 SVM 等方法，对工厂烟囱视频进行烟尘排放识别训练与测试，支持 Grad-CAM 可视化模型关注区域与混淆矩阵摘要视频生成。数据集为 2020-02-24 快照的标注视频（高/低不透明度烟、蒸汽、蒸汽带烟），代码 BSD 3-clause、数据集 CC0 许可。假设 Ubuntu 22.04 服务器环境，安装涉及 NVIDIA 驱动、CUDA 11.8、cuDNN、conda 环境与 PyTorch。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- I3D 双流模型对视频进行烟尘排放识别训练与测试
- 公开标注视频数据集（CC0），含 train/validation/test 划分脚本
- Grad-CAM 可视化与混淆矩阵摘要视频生成
- 论文发表于 AAAI 2021，代码中修正了论文 non-local block 实现错误

## 适用场景

- 训练和评估工业烟尘排放识别模型
- 获取带标注的烟囱排放视频数据集做计算机视觉研究
- 用 Grad-CAM 分析模型在视频中的识别依据

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L1: # deep-smoke-machine
> L11: The following figures show how the I3D model recognizes industrial smoke. The heatmaps (red and yellow areas on top

## 星数曲线

```mermaid
xychart-beta
    title "CMU-CREATE-Lab/deep-smoke-machine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 124 --> 126
    line [125, 125]
```

2026-10-18 125 → 2026-10-26 125（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `07d057dd8459` · [字段定义](../../DATASET.md)*
