# abhineet123/animal_detection

⭐ 44 · Python · 推送 2026-05-19 · [GitHub](https://github.com/abhineet123/animal_detection) · [官网](https://ieeexplore.ieee.org/document/9093504) · 个人维护

**论文配套代码：深度学习检测人造环境中的动物**

随 arXiv 论文《Animal Detection in Man-made Environments》发布的实验代码仓库，包含修改版的开源检测器实现：YOLOv3、TensorFlow Object Detection API 下的多种检测器与 Mask RCNN（含 RetinaNet）、SiamFC/SiamMask 相关实验，另附评测工具（mAP）与图像标注工具。各模型的运行命令放在对应文件夹的 .md 文件中，按实验类别分层组织。数据托管在 Hugging Face 仓库，命令假定数据位于 /data/acamp/acamp20k。代码与数据以 CC BY 许可发布，供研究与商业使用，但被修改的各上游仓库可能有各自更严格的许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 包含 YOLOv3、RetinaNet、Mask RCNN 等多种检测器的修改版实现
- 提供 mAP 评测工具与图像标注工具
- 各模型运行命令按实验类别组织于对应文件夹的 .md 文件
- 配套数据发布于 Hugging Face 仓库

## 适用场景

- 复现论文中的人造环境动物检测实验
- 对比不同检测器（YOLOv3/RetinaNet/Mask RCNN）在该任务上的表现
- 利用标注工具制作动物检测数据集

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository provides python code for all experiments reported in this paper:
> L5: Animal Detection in Man-made Environments
> L9: These are the reported models and their corresponding folders:

## 星数曲线

```mermaid
xychart-beta
    title "abhineet123/animal_detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-27 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `4149f14f0b37` · [字段定义](../../DATASET.md)*
