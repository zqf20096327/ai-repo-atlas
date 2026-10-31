# YusephAlvandi/FacialLandmarks_Pro

⭐ 15 · Python · 推送 2026-06-29 · [GitHub](https://github.com/YusephAlvandi/FacialLandmarks_Pro) · 个人维护

**离线图像人脸 478 点网格标注的桌面应用**

基于 MediaPipe Face Landmarker 模型的面部关键点检测应用：读取本地图像，识别其中人脸并映射 478 个关键点（眼、眉、鼻、唇、轮廓），以绿点叠加展示，结果可另存为新图像。全程本地离线运行，图像不上传。依赖 Python 库（mediapipe/opencv-python/pillow/customtkinter），需一次性下载 3.6 MB 的 face_landmarker.task 模型文件放入脚本目录，运行 facial_landmarks.py 启动 GUI 后打开图像即可自动检测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 MediaPipe 深度学习模型输出 478 点面部网格
- 完全离线本地运行，图像不离开本机
- GUI 操作：打开图像、自动标注、保存结果

## 适用场景

- 给本地图片做人脸关键点标注并保存结果
- 离线处理人脸图像，避免隐私外泄

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: A deep learning-based application for detecting 478-point facial mesh in images. Uses MediaPipe's Face Landmarker mo
> L7: This application identifies human faces in images and maps 478 precise landmarks onto each face; including eyes, eye

## 星数曲线

```mermaid
xychart-beta
    title "YusephAlvandi/FacialLandmarks_Pro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9c3b6ac195ed` · [字段定义](../../DATASET.md)*
