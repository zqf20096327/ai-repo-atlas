# tatigabru/kaggle-rsna

⭐ 126 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/tatigabru/kaggle-rsna) · [官网](https://arxiv.org/abs/2005.13899) · 个人维护

**胸部 X 光片肺炎病灶检测的深度学习方案**

面向放射科图像的肺炎病灶目标检测研究代码：基于 PyTorch RetinaNet 单阶段检测器与 SE-ResNeXt 系列 backbone（se-resnext101 最优），图像缩放至 512×512 并配合数据增强与 ImageNet 预训练，在 RSNA 肺炎检测挑战数据集（26684 名患者、三类标注）上以 mAP@IoU 为指标训练与预测，训练约 12 轮、P100 上每轮 50 分钟。提供 conda/Docker 环境脚本、数据下载脚本、训练/评分/预测入口脚本及推理流程。代码基于挑战赛第二名的开源方案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RetinaNet + SE-ResNeXt（101/50）backbone 的肺炎病灶检测
- 26684 名患者的 RSNA 挑战 CXR 数据集训练与 mAP 评估实现
- 数据下载、conda/Docker 环境、训练/预测的完整脚本流程
- 支持用已保存 checkpoint 对自有测试图像生成预测

## 适用场景

- 复现 RSNA 肺炎检测挑战实验结果
- 在自己的胸部 X 光数据上训练肺炎病灶检测模型
- 基于该方案开展医学影像检测相关研究并引用论文

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: Pneumonia is the leading cause of death among young children and one of the top mortality causes worldwide. The pneu
> L50: The model is based on RetinaNet implementation on Pytorch with a few modifications. Several different base models' 

## 星数曲线

```mermaid
xychart-beta
    title "tatigabru/kaggle-rsna 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 125 --> 127
    line [126, 126]
```

2026-10-18 126 → 2026-10-27 126（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8daca213f388` · [字段定义](../../DATASET.md)*
