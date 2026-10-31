# YusephAlvandi/FaceMeshVideo

⭐ 15 · Python · 推送 2026-07-06 · [GitHub](https://github.com/YusephAlvandi/FaceMeshVideo) · 个人维护

**离线视频人脸检测与 478 点面部网格标注工具**

基于 Python/OpenCV/MediaPipe/CustomTkinter 的桌面 GUI 应用：读取视频文件，用 YOLOv8n-face 检测人脸、MediaPipe Face Landmarker（478 点）生成面部网格，输出带标注的视频并借助 ffmpeg 保留原声。用户可调节关键点大小与 YOLO 置信度。完全离线运行，无需上传数据到外部服务器。安装依赖若干 Python 库与 ffmpeg，模型文件首次运行自动下载或手动放置。

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

- YOLOv8n-face 人脸检测 + MediaPipe 478 点面部网格两个模型组合
- 完全离线运行，数据不上传外部服务器
- GUI 操作，可调节关键点大小与 YOLO 置信度
- ffmpeg 保留原视频音轨

## 适用场景

- 为开发人脸识别软件做面部关键点标注的前置处理
- 离线批量给视频添加人脸网格可视化输出

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: This application is used for detecting faces in a video and meshing them with facial landmarks. This can be used as 
> L5: Two deep learning models were used: YOLOv8n-face (a CNN for face detection) and MediaPipe Face Landmarker (a DNN for

## 星数曲线

```mermaid
xychart-beta
    title "YusephAlvandi/FaceMeshVideo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4cf0c9f96652` · [字段定义](../../DATASET.md)*
