# mlapaglia/OpenAlprWebhookProcessor

⭐ 25 · C# · 推送 2026-10-25 · [GitHub](https://github.com/mlapaglia/OpenAlprWebhookProcessor) · [官网](https://ipcamtalk.com/threads/openalpr-webhook-processor-for-ip-cameras.53364/) · 个人维护

**处理 OpenALPR webhooks 的车牌检测管理与摄像头叠加系统**

面向 IP 摄像头监控场景的车牌识别管理系统：接收并处理来自 OpenALPR web 服务器的车牌 webhook，管理多路 Hikvision/Dahua 摄像头（直播叠加显示、日夜模式切换、聚焦控制、检测区域遮罩），支持按车牌号或模式自定义告警并经推送/Pushover/webhook 转发通知；内置机器学习模块预测车牌下次到访时间并在后台自动重训模型。提供 Angular 前端与 ASP.NET Core 后端的管理界面，支持 Docker 部署，需持久化存储数据库、配置、模型与快照。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接收 OpenALPR webhook 的实时车牌处理与多摄像头管理
- 兼容 Hikvision/Dahua，支持视频叠加、日夜模式与聚焦控制
- 按车牌号/模式自定义告警，支持推送、Pushover 与 webhook 转发
- 机器学习到访预测与后台自动模型重训

## 适用场景

- 在摄像头画面上实时叠加显示识别到的车牌
- 监控指定车牌并在检测到时收到即时告警
- 分析车牌到访规律并预测下次出现时间

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L14: A comprehensive license plate recognition management system that processes webhooks from OpenALPR web servers, mana
> L19: - **Real-time Processing**: Receives and processes license plate webhooks from OpenALPR web servers
> L33: ### Machine Learning Predictions

## 星数曲线

```mermaid
xychart-beta
    title "mlapaglia/OpenAlprWebhookProcessor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `d313d6d67414` · [字段定义](../../DATASET.md)*
