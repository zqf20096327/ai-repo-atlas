# kamalesh404/crowd_detection

⭐ 15 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/kamalesh404/crowd_detection) · 个人维护

**实时人群监控与踩踏预警系统：检测、追踪并预测危险**

基于 YOLOv8 与 PyTorch 的人群监控系统：从摄像头、RTSP 流或录像中检测行人并持续追踪，统计人数与分区密度，叠加密度/运动热力图；通过速度骤增、人群压缩、逃逸模式等签名检测踩踏前兆，并用 LSTM 网络基于前 60 秒指标预测未来 30-120 秒风险。提供告警升级（视觉/音频/TTS/SMS/邮件/Firebase 推送）、走失儿童检测、运营仪表盘与自动事件时间线报告。支持在笔记本、Jetson、树莓派 5 等边缘设备离线运行，模型量化为 ONNX INT8。面向车站、寺庙、体育场馆、商场等高人流场所的管理方与安保人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv8 行人检测与 ByteTrack 持续追踪，30+ FPS
- LSTM 预测引擎输出未来 30/60/120 秒风险预报
- 踩踏签名检测（速度骤增、人群压缩、逃逸模式、压力波）
- 边缘离线运行，模型量化 ONNX INT8，支持 Jetson/树莓派 5

## 适用场景

- 在车站或场馆实时监控人群密度并提前收到踩踏风险预警
- 通过短信/邮件/推送通知安保人员并广播语音告警
- 事件结束后自动生成含时间线的详细事件报告
- 在网络受限的户外活动现场离线运行监控

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L11: An AI-powered real-time crowd monitoring system that detects people, tracks movement, measures density, predicts da
> L39: - **YOLOv8 Engine:** Detects people frame by frame at 30+ FPS.
> L63: ### 🔮 Predictive Risk Engine (LSTM)

## 星数曲线

```mermaid
xychart-beta
    title "kamalesh404/crowd_detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `954031c20615` · [字段定义](../../DATASET.md)*
