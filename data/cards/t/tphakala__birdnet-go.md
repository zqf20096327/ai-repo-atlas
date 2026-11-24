# tphakala/birdnet-go

⭐ 2,471 · Go · NOASSERTION · 推送 2026-11-22 · [GitHub](https://github.com/tphakala/birdnet-go) · 个人维护

**树莓派上 24/7 本地运行的野生动物声景实时识别监测器**

自托管的实时声景分析系统：持续监听本地麦克风或 RTSP 网络音频流，用 BirdNET、Google Perch、蝙蝠模型在本地推理识别物种，在 Web 仪表盘呈现检测结果、频谱图与录音片段。支持多模型并行与跨模型共识、误报过滤、40+ 物种语言、多种告警推送与 Home Assistant/MQTT 集成。单二进制部署，Docker 多架构镜像支持，可运行在树莓派 4 上。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多模型并行推理：BirdNET v2.4、BirdNET+ v3.0、Google Perch v2、蝙蝠模型，Web UI 内安装无需重编译
- 本地麦克风与 RTSP 流多源分析，支持跨模型共识过滤
- 告警规则引擎：Discord/Slack/Telegram/MQTT/Home Assistant/BirdWeather 等多种投递目标
- 单静态二进制，树莓派 4 可 24/7 运行，OpenVINO 加速可选

## 适用场景

- 在树莓派或家庭服务器上搭建 24/7 鸟类声学监测站
- 检测院子/喂鸟器的到访物种并推送到手机或 Home Assistant
- 用超声波采样率记录和识别蝙蝠
- 将检测结果上传 BirdWeather 参与社区声学数据共享

## 场景标签

 · 领域:生物声学/生态监测

## 证据(README 行号)

> L34: **24/7 self-hosted AI sound monitor for birds, bats, and other wildlife.**
> L36: BirdNET-Go listens continuously to local microphones or network audio streams, identifies species locally using Bir

## 星数曲线

```mermaid
xychart-beta
    title "tphakala/birdnet-go 星数(近 27 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 2308 --> 2485
    line [2322, 2328, 2343, 2350, 2355, 2364, 2369, 2376, 2379, 2380, 2381, 2385, 2350, 2411, 2423, 2430, 2437, 2440, 2446, 2452, 2460, 2464, 2466, 2468, 2470, 2471, 2471]
```

2026-10-22 2,322 → 2026-11-24 2,471（+149）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `ef02f8967756` · [字段定义](../../DATASET.md)*
