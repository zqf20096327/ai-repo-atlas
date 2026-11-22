# AkaCoder404/tenniscourt-detector

⭐ 10 · Jupyter Notebook · 推送 2026-04-19 · [GitHub](https://github.com/AkaCoder404/tenniscourt-detector) · 个人维护

**用 YOLOv8-pose 检测网球场 14 个关键点的训练项目**

基于 Ultralytics YOLOv8-pose 的实验项目：在含 14 个标注关键点的网球场图像数据集上训练模型，输出球场线与透视映射。流程覆盖数据准备脚本（zip 解压并转 YOLO 格式）、train.py 训练（以 yolov8s-pose.pt 为基座）、evaluate.ipynb 评估（输出 mAP 指标与预测可视化）和 inference_video.py 的视频推理，将检测结果叠加回原视频。含作者在 RTX 2070 SUPER 上的训练指标结果。

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

- 网球场 14 关键点检测（YOLOv8-pose）训练全流程脚本
- 数据集 zip 一键转 YOLO 格式的准备脚本
- Jupyter 评估：mAP 指标与预测-真值可视化、球场透视映射
- 视频推理脚本将线条与关键点叠加到比赛录像

## 适用场景

- 检测网球场视频中的场地线与关键点
- 复现 YOLOv8-pose 在球场关键点数据上的指标
- 将球场透视映射到 2D 俯视参考图

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: The goal of this project is to see the performance of YOLOv8 at detecting the 14 keypoints of a tennis court to map 
> L28: To train the YOLOv8-pose model on the tennis court dataset:

## 星数曲线

```mermaid
xychart-beta
    title "AkaCoder404/tenniscourt-detector 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `9d1f6866ec74` · [字段定义](../../DATASET.md)*
