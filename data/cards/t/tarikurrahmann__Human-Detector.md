# tarikurrahmann/Human-Detector

⭐ 18 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/tarikurrahmann/Human-Detector) · 个人维护

**基于 YOLOv8 的实时人体检测系统，输出 CSV 与标注视频**

以 YOLOv8 为检测模型的 Python 人体检测项目：读取视频文件、摄像头或 IP 摄像流（RTSP），逐帧检测与追踪人员，输出含时间戳、置信度、边界框坐标的 CSV 遥测日志，并导出带标注框与 FPS 叠加的 MP4 视频。支持 nano 到 xlarge 多档模型自动回退、批量处理与自定义训练。面向安防监控、人群统计、占用分析与研究场景的用户，安装方式为 git clone 后 pip 安装依赖运行脚本；CPU 可运行但速度较慢，GPU 为可选加速项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 视频/摄像头/RTSP 流多源输入的实时人体检测与追踪
- 逐帧 CSV 遥测日志（时间戳、置信度、边界框坐标）
- 带边界框标注与 FPS 叠加的 MP4 视频导出
- YOLOv8n/s/m 模型自动回退与批量处理、自定义训练支持

## 适用场景

- 监控视频或摄像头画面中检测与统计人员
- 门店/场馆做客流计数与占用分析
- 获取逐帧检测数据用于后续数据分析

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: **Advanced human detection engine with real-time analytics, CSV telemetry logging, and annotated video export powere
> L20: **Human Detector** is a cutting-edge real-time person detection system built on YOLOv8. It leverages advanced deep 


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `28ce98569be7` · [字段定义](../../DATASET.md)*
