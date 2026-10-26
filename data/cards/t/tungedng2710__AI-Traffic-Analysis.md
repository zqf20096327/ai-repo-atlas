# tungedng2710/AI-Traffic-Analysis

⭐ 37 · Python · 推送 2026-07-26 · [GitHub](https://github.com/tungedng2710/AI-Traffic-Analysis) · 个人维护

**交通监控与车牌识别系统：YOLO 检测 + PaddleOCR 识别**

TrafficCam 是一套车牌识别（ALPR）与交通监控系统，由 FastAPI REST 服务、共享处理核心和 Web 可视化应用（beta）组成。使用 Ultralytics YOLO（YOLOv8/11/12）做多类车辆与车牌检测，PaddleOCR v4/v5 做文字识别，SORT/DeepSORT 做目标跟踪；支持 PyTorch 与 ONNX 模型及 TensorRT 加速推理。提供 Docker Compose 一键部署、训练脚本与模型库（含 mAP 指标）。面向 Ubuntu 环境，生产环境推荐 NVIDIA GPU 与 CUDA，模型权重约占 2GB 空间。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLO 车辆/车牌检测 + PaddleOCR v4/v5 文字识别 + SORT/DeepSORT 跟踪
- FastAPI JSON REST API（/predict/image、/predict/frame 等端点）
- 支持 .pt/.onnx 模型与 TensorRT 加速推理
- Docker Compose 一键部署分析与 WebApp 两个服务

## 适用场景

- 通过 REST API 对图片或视频帧做车牌检测与识别
- 接入 RTSP/WebRTC 摄像头做实时交通监控可视化
- 用自带脚本训练并导出自己的 YOLO 车牌检测模型

## 场景标签

`目标检测` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L14: TrafficCam is a comprehensive traffic surveillance and license plate recognition system built on modern deep learni
> L32: - **OCR Recognition**: PaddleOCR v4/v5 for text recognition
> L30: - **Vehicle Detection**: YOLO-based multi-class vehicle detection (cars, trucks, buses, motorcycles, bicycles)

## 星数曲线

```mermaid
xychart-beta
    title "tungedng2710/AI-Traffic-Analysis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4872d6031979` · [字段定义](../../DATASET.md)*
