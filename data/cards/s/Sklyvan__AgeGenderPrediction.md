# Sklyvan/AgeGenderPrediction

⭐ 30 · Jupyter Notebook · GPL-3.0 · 推送 2026-07-22 · [GitHub](https://github.com/Sklyvan/AgeGenderPrediction) · 个人维护

**两阶段深度学习管线：人脸检测并预测年龄段与性别**

Deep Learning 2022 课程最终项目，含两阶段管线：先用 YOLOv5（WIDER FACE 微调、1280px、导出 ONNX）定位人脸，再将人脸裁剪送入 CNN 分类器（ResNet-18 或 InceptionResNetV1）输出 9 个年龄段分类与性别。训练用 UTKFace 数据集，损失为年龄头 MSE 加性别头 BCE。以四个 Jupyter notebook 交付，支持图像、视频与实时摄像头推理，仓库附带训练好的权重；开发于 Google Colab，支持本地运行，再训练建议使用 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv5 人脸检测 + CNN 年龄段/性别分类的两阶段管线
- 年龄离散为 9 组（00-10 至 81-90），UTKFace 上性别准确率约 91-93%
- 支持图像、视频文件与实时摄像头三种输入
- 仓库附带训练权重与示例测试图像

## 适用场景

- 对图像或视频中的人脸批量估计年龄段与性别
- 实时摄像头流中做人脸检测与属性预测
- 复现课程实验或在此基础上再训练模型

## 场景标签

`人脸识别` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L14: 1. **Face detection** — a YOLOv5 model locates faces and returns bounding boxes.
> L15: 2. **Age & gender classification** — each detected face is cropped and passed to a
> L18: The final notebook ties both stages together and runs on still images, video files,

## 星数曲线

```mermaid
xychart-beta
    title "Sklyvan/AgeGenderPrediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8b8a60385bcb` · [字段定义](../../DATASET.md)*
