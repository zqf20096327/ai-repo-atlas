# yihong1120/Construction-Hazard-Detection

⭐ 348 · Python · AGPL-3.0 · 推送 2026-10-21 · [GitHub](https://github.com/yihong1120/Construction-Hazard-Detection) · [官网](https://visionnaire-cda17.web.app/) · 个人维护 · 中文 README

**工地摄像头实时安全隐患检测系统（未戴安全帽/接近机械等）**

面向建筑工地实时摄像头的 AI 安全监控系统：基于 YOLO 检测 11 类目标，识别未戴安全帽/反光背心的工人、工人距机械车辆过近、进入锥筒划定管控区、机械贴近电线杆等隐患；用 HDBSCAN 聚类安全锥坐标生成受控区域，并以后处理规则提升判定准确性。运行时以 main.py、YOLO worker 进程、MediaMTX 流媒体、PostgreSQL 记录、Redis 协调及一组 FastAPI 服务组成，支持 FCM/LINE/Telegram 等多渠道通知，提供 HLS/WebRTC 播放、Flutter 前端源（另仓）与训练/评估/数据增强工具。要求 Python 3.14，需 Docker Compose 启动基础设施，GPU 推理可选 CUDA/TensorRT。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLO 检测 11 类目标，覆盖未戴安全帽/背心、接近机械、误入管控区等规则
- HDBSCAN 聚类安全锥坐标生成受监控区域
- 多 YOLO worker 经共享内存共享 GPU 推理，MediaMTX 提供 HLS/WebRTC 播放
- 支持 FCM/LINE/Messenger/Telegram/微信等 8 种语言与多渠道通知，含 MCP server 可选组件

## 适用场景

- 工地安全员通过实时摄像头监控工人防护装备穿戴情况
- 对工人靠近机械车辆或误入危险区域自动告警并推送通知
- 留存违规记录与截图供安全管理复盘

## 场景标签

 · 领域:计算机视觉/工业安全监控

## 证据(README 行号)

> L47: AI-assisted construction-site safety monitoring for live cameras. The current
> L55: - Workers without hard hats.
> L58: - Workers inside cone-derived controlled areas.

## 星数曲线

```mermaid
xychart-beta
    title "yihong1120/Construction-Hazard-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 347 --> 349
    line [348, 348]
```

2026-10-18 348 → 2026-10-24 348（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c9c6c58a5894` · [字段定义](../../DATASET.md)*
