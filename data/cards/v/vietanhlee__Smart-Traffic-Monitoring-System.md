# vietanhlee/Smart-Traffic-Monitoring-System

⭐ 37 · TypeScript · AGPL-3.0 · 推送 2026-05-12 · [GitHub](https://github.com/vietanhlee/Smart-Traffic-Monitoring-System) · [官网](https://smart-traffic-monitoring-system.vercel.app/) · 个人维护

**实时车辆检测与交通流监测系统，含可视化看板与 AI 问答**

基于 YOLO + ByteTrack 的交通监测系统：实时检测与跟踪多路摄像头车辆，统计各道路的车流量与平均速度，经 FastAPI 提供 REST/WebSocket/WebRTC API，前端 React 看板展示分析数据；内置 LangGraph ReAct 聊天机器人，用自然语言查询已处理的交通数据。模型支持 INT8 OpenVINO/TensorRT 量化与 torch-pruning 剪枝，支持 CPU 和 GPU。部署依赖 PostgreSQL、Redis、MinIO，提供手动与 Docker Compose 两种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLO + ByteTrack 实时车辆检测与多路摄像头多进程处理
- LangGraph ReAct 聊天机器人以自然语言查询交通数据
- INT8 OpenVINO/TensorRT 量化与 torch-pruning 模型剪枝
- REST/WebSocket/WebRTC API 与 JWT 认证

## 适用场景

- 我想对多条道路做实时车流量和车速监测
- 通过聊天机器人用自然语言查询交通统计
- 在 Web 看板上查看实时路况图表与视频流

## 场景标签

`目标检测` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: An intelligent traffic monitoring system that uses AI to detect and track vehicles in real time. It provides a live 
> L13: - Real-time vehicle detection and tracking (YOLO + ByteTrack)
> L18: - AI chatbot (LangGraph ReAct) for natural language queries

## 星数曲线

```mermaid
xychart-beta
    title "vietanhlee/Smart-Traffic-Monitoring-System 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-29 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a2a7ff91f6e3` · [字段定义](../../DATASET.md)*
