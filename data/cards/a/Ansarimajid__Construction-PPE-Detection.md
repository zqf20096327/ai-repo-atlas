# Ansarimajid/Construction-PPE-Detection

⭐ — · [GitHub]() · 个人维护

**工地安全帽/反光衣/口罩实时检测系统，带 API 与告警**

基于 YOLOv8 的建筑工地 PPE（个人防护装备）合规监测系统：实时检测安全帽、反光衣、口罩与人员，共 10 个检测类别。提供 FastAPI 后端（CRUD/流媒体/导出接口），支持摄像头、RTSP 流与视频文件多路并发；违规记录存入 SQLite 或 PostgreSQL 并附帧截图，通过邮件与 Webhook 告警；Bootstrap 5 网页仪表盘展示 MJPEG 实时画面与 WebSocket 检测计数。测试环境无需摄像头或 GPU（YOLO 模型被 mock）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv8 实时检测 10 类目标（含未佩戴违规类别）
- FastAPI 后端 + 多摄像头（webcam/RTSP/视频文件）并发处理
- 违规日志存储（SQLite/PostgreSQL）附帧截图，支持 CSV 导出
- 邮件与 Webhook 告警（Slack/Teams 等），Docker 生产部署

## 适用场景

- 工地监控摄像头自动检查工人是否佩戴安全帽和反光衣
- 违规事件留档并导出报表供安全管理审查
- 通过 Webhook 把违规推送到团队 Slack/Teams 频道

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L13: **Detect helmets, vests, and masks in real-time — log every violation, stream live feeds to a web dashboard, and al
> L19: Construction sites are among the most hazardous work environments. Manual supervision of PPE compliance is unreliab

## 星数曲线

```mermaid
xychart-beta
    title "Ansarimajid/Construction-PPE-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-25 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `2ac2d76a2018` · [字段定义](../../DATASET.md)*
