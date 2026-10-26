# arminfabritzek/WatchMyBirds

⭐ 29 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/arminfabritzek/WatchMyBirds) · 个人维护

**从摄像头实时检测与分类鸟类的自托管监控应用**

面向观鸟与生态监测的自托管应用：读取 USB 摄像头或 RTSP/IP 摄像头视频流，经多阶段 AI 流水线（检测+分类）实时识别鸟类，提供活动模式与物种统计分析仪表盘、WebRTC 低延迟直播（经 go2rtc 中继）、物种百科（Wikipedia 描述）、检测复核队列与 ONVIF 摄像头发现/PTZ 控制。支持 Docker 一条命令部署，也提供树莓派预构建系统镜像（AP 热点首次配置）。全部本地运行，检测数据不出设备。树莓派 4 上单鸟完整周期约 10-11 秒，树莓派 5 约 1.5-2 秒。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多阶段 AI 流水线：YOLOX-S 检测 + 分类器的实时鸟类识别
- Docker 一条命令部署；树莓派 4/5 预构建 appliance 镜像
- WebRTC 低延迟直播、ONVIF 发现与 PTZ 控制、分析仪表盘
- 完全本地运行，检测数据不离开设备

## 适用场景

- 在后院喂鸟点用树莓派做长期鸟类监测
- 生物多样性观察与公民科学记录
- 生态研究或教学项目中搭建低成本野生动物监控

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L37: - 🎯 **Real-time detection** — Multi-stage AI pipeline (detection + classification)
> L5:  AI-powered bird detection and classification from live camera streams

## 星数曲线

```mermaid
xychart-beta
    title "arminfabritzek/WatchMyBirds 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `235300fb7b36` · [字段定义](../../DATASET.md)*
