# K-saif/Weapon-Detection-and-Alarm-System

⭐ 32 · HTML · MIT · 推送 2026-06-21 · [GitHub](https://github.com/K-saif/Weapon-Detection-and-Alarm-System) · 个人维护

**实时武器检测与告警系统：监控摄像头流并自动发邮件/Telegram 警报**

基于 Ultralytics YOLO 的实时武器检测系统：读取网络摄像头、视频文件或 RTSP/HTTP 流，对检测到的武器进行跟踪，含持续性门控、冷却计时与过期清理等告警去重逻辑，通过线程池异步发送 Email 与 Telegram 告警。可选启用 VLM（LLaVA/PaliGemma/Qwen）生成事件描述。提供预训练模型 best.pt（测试集 mAP50 为 0.991）、自定义训练数据集说明与 Web 仪表盘。从源码克隆并以 pip 安装依赖运行，不支持单张图片输入，Docker 化列为未来计划。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持摄像头/视频文件/RTSP/HTTP 流输入，持续性门控与冷却计时去重告警
- Email 与 Telegram 多通道异步告警
- 可选 VLM（LLaVA/PaliGemma/Qwen）生成事件描述
- 提供 Web 仪表盘：实时画面叠加、告警历史与统计

## 适用场景

- 对监控摄像头流做武器检测并自动接收告警
- 在自己的武器数据集上训练 YOLO 模型
- 通过仪表盘查看检测事件与统计

## 场景标签

`目标检测` `网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: By using Ultralytics YOLO real-time weapon detection with tracking, cooldown-based alerts, persistence filtering, an
> L61: ```bash

## 星数曲线

```mermaid
xychart-beta
    title "K-saif/Weapon-Detection-and-Alarm-System 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `6006cae5c42c` · [字段定义](../../DATASET.md)*
