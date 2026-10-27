# fredotran/traffic-sign-detector-yolov4

⭐ 32 · Jupyter Notebook · 推送 2025-11-11 · [GitHub](https://github.com/fredotran/traffic-sign-detector-yolov4) · 个人维护

**用 YOLOv4 与 OpenCV DNN 检测 4 类交通标志的项目**

个人训练项目：基于 877 张图、4 类（红绿灯、限速、人行横道、停车标志）的数据集训练 YOLOv4 自定义检测模型，通过 OpenCV DNN（GPU 后端）运行检测；提供预训练权重下载、数据集自动下载/划分脚本、训练与测试命令，以及图像和视频测试用的 Jupyter Notebook。环境要求 Windows、OpenCV 4.0+、CUDA 11+、cuDNN 7+，需自行编译 darknet；Google Colab 云端路径已标注弃用。作者报告 mAP@0.5 为 95.13%（约 2000 次迭代）。

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

- 4 类交通标志的自定义 YOLOv4 训练与检测，报告 mAP@0.5 95.13%
- 提供预训练权重自动下载脚本（download_weights.py）
- 数据集自动下载与训练/验证/测试集划分脚本
- 附带图像与视频测试的 Jupyter Notebook

## 适用场景

- 用预训练权重直接对图像/视频做交通标志检测
- 在 Windows + CUDA 环境下复现或继续训练自定义模型
- 学习 YOLOv4 自定义数据集训练与 OpenCV DNN 部署流程

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L5: This repository contains my upgraded version of using YoloV3 with OpenCV DNN to detect objects by training a YoloV4 
> L85: Using the weights provided in this repository, the model achieved an **accuracy mAp @0.5 of 95.13%** (*it tooks ~ 2

## 星数曲线

```mermaid
xychart-beta
    title "fredotran/traffic-sign-detector-yolov4 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0cce892debb2` · [字段定义](../../DATASET.md)*
