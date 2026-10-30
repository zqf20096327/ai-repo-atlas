# Alijanloo/Retail-Shelf-Monitoring

⭐ 16 · Python · MIT · 推送 2025-11-06 · [GitHub](https://github.com/Alijanloo/Retail-Shelf-Monitoring) · 个人维护

**基于 CCTV 视觉分析的零售货架监控系统（缺货/错放检测）**

利用现有 CCTV 视频流做实时货架分析的计算机视觉系统：YOLOv12-M 检测商品，MobileNetV3 嵌入结合 FAISS 相似度搜索识别 SKU，DBSCAN 自动生成货架网格并做排面合规（planogram）比对，SORT + Kalman 滤波保证跨帧时序一致性，时间共识过滤减少误报，最终经 PySide6 桌面端展示实时画面与告警供员工确认。检测模型在 SKU-110k 上微调（mAP50–95 = 0.56），支持 ONNX/OpenVINO/TensorRT 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv12-M 商品检测，SKU-110k 微调（mAP50–95 = 0.56）
- MobileNetV3 + FAISS 的 SKU 识别（Top-1 93%）
- SORT + Kalman 跟踪与时间共识过滤降误报
- PySide6 桌面端实时叠加展示与告警确认

## 适用场景

- 门店用现有摄像头自动发现缺货与错放商品
- 核对实际陈列与排面图（planogram）的合规性
- 在桌面端查看实时货架分析并确认告警

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: A real-time retail shelf monitoring solution powered by computer vision and machine learning. The system leverages e
> L9: * **Real-time Shelf Analysis** using YOLOv12-M for product detection
> L20: CCTV Stream → Keyframe Selection → Shelf Detection →

## 星数曲线

```mermaid
xychart-beta
    title "Alijanloo/Retail-Shelf-Monitoring 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7814dd1b983b` · [字段定义](../../DATASET.md)*
