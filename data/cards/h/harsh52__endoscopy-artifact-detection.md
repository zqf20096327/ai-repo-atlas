# harsh52/endoscopy-artifact-detection

⭐ 21 · Jupyter Notebook · MIT · 推送 2026-04-15 · [GitHub](https://github.com/harsh52/endoscopy-artifact-detection) · 个人维护

**YOLOv2 检测内窥镜图像中 7 类伪影的实习项目**

基于 EAD2019 挑战赛数据集的内窥镜伪影检测项目：使用 Darknet 框架实现的 YOLOv2 对内窥镜帧进行实时目标检测，识别 specularity、saturation、artifact、contrast、blur、bubbles、instruments 共 7 类伪影。作者比较了 YOLO、Fast R-CNN、R-CNN 多种架构后采用 YOLOv2（IoU 与 mAP 分数最高）。运行方式为跟随 Jupyter notebook，数据集需从 Google Drive 下载（2,147 帧标注图像）。技术栈为 Python、Darknet (C)、OpenCV。

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

- 检测 7 类内窥镜伪影（高光、气泡、器械等）
- 基于 Darknet 框架的 YOLOv2 实时目标检测
- 对比过 YOLO、Fast R-CNN、R-CNN 架构后选定 YOLOv2
- 提供 Jupyter notebook 形式的研究代码

## 适用场景

- 研究内窥镜图像伪影检测的深度学习方法
- 复现 EAD2019 挑战赛相关工作
- 学习 YOLOv2/Darknet 在医学影像上的应用

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: Detects 7 types of artifacts in endoscopy frames: specularity, saturation, artifact, contrast, blur, bubbles, and in
> L3: Detecting artifacts in endoscopy images using YOLOv2 — built during a summer internship based on the EAD2019 challen

## 星数曲线

```mermaid
xychart-beta
    title "harsh52/endoscopy-artifact-detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c68f537a7d4b` · [字段定义](../../DATASET.md)*
