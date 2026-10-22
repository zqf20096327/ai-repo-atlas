# aparsoft/yolo-streamlit-detection-tracking

⭐ 430 · Python · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/aparsoft/yolo-streamlit-detection-tracking) · [官网](https://aparsoft.com) · 个人维护

**基于 Streamlit 的视频目标检测/分割/姿态/文本检索与追踪计数应用**

面向需要可视化目标检测与计数用户的免费开源 Streamlit 应用：在图像和视频上运行 YOLO26、RT-DETR、YOLO World v2、YOLOE 等模型，支持检测、实例分割、姿态估计与文本提示检索；视频侧提供 ByteTrack 等 4 种追踪器、可选外观 ReID，并区分当前帧计数与去重后的累计计数（物体需连续出现 5 帧才计入），同时显示 Churn 指标。视频源支持本地文件、浏览器摄像头、RTSP 与 YouTube；多个会话的追踪状态互相隔离。可运行于 CPU，NVIDIA GPU 可加速；通过 git clone 配合 uv 或 pip 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同时显示帧内计数、去重累计计数与 Churn 指标
- 4 种追踪器与可选外观 ReID（含编码器选择与三个可调阈值）
- 支持存储视频、浏览器摄像头、RTSP 流与 YouTube 链接
- 多视频并排运行，追踪 ID 按视频隔离

## 适用场景

- 统计一段时间内经过的不同行人/车辆数量
- 用文本提示（如 red car）在视频中检索特定目标
- 对视频做分割、姿态估计并按 ID 追踪

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L4: A free, open-source Streamlit app built on Ultralytics YOLO26, YOLOE, YOLO World v2 and RT-DETR.
> L48: |**Tasks**|Detection, Segmentation, Pose Estimation, YOLO World v2 (text prompt), YOLOE (text → masks). All of them

## 星数曲线

```mermaid
xychart-beta
    title "aparsoft/yolo-streamlit-detection-tracking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 429 --> 431
    line [430, 430]
```

2026-10-18 430 → 2026-10-22 430（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `bd439f233dfc` · [字段定义](../../DATASET.md)*
