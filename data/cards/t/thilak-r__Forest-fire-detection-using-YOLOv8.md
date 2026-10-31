# thilak-r/Forest-fire-detection-using-YOLOv8

⭐ 14 · Jupyter Notebook · 推送 2025-11-29 · [GitHub](https://github.com/thilak-r/Forest-fire-detection-using-YOLOv8) · 个人维护

**基于 YOLOv8 的实时森林火灾烟雾检测系统，含 Telegram 告警**

使用 YOLOv8 对上传图片、视频流和实时摄像头画面进行火焰与烟雾检测的深度学习应用；当火焰检测置信度超过 0.75 时，通过 Telegram Bot API 实时发送告警。提供 Flask 网页前端展示检测画面与告警通知，并附有在 DFireDataset 上的模型评估指标（Fire 类 mAP@0.5 为 0.963，Smoke 类为 0.883）。本地运行方式为 git clone 源码后执行。面向需要在视频流中做火灾检测与即时告警的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv8 检测图片、视频与实时摄像头中的火焰与烟雾
- 置信度 > 0.75 时通过 Telegram Bot API 实时告警
- Flask 前端展示实时检测与告警通知
- 公开 DFireDataset 上的精确率/召回率/mAP 评估结果

## 适用场景

- 对摄像头画面做实时火灾烟雾监测
- 检测到火焰时即时收到 Telegram 告警
- 对上传图片或视频进行火焰烟雾分析

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L19: A powerful computer vision system that leverages **YOLOv8** for detecting **fire** and **smoke** from:
> L24: Alerts are sent in real time using **Telegram Bot API** when fire confidence exceeds a critical threshold.

## 星数曲线

```mermaid
xychart-beta
    title "thilak-r/Forest-fire-detection-using-YOLOv8 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2ef03a03721f` · [字段定义](../../DATASET.md)*
