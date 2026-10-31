# tarraschk/GardenGuardian

⭐ 13 · Python · 推送 2026-06-04 · [GitHub](https://github.com/tarraschk/GardenGuardian) · 个人维护

**树莓派驱动的 AI 鸽子检测与水枪驱逐系统**

面向树莓派硬件爱好者的动物驱逐原型：摄像头画面经 Hailo-8 加速运行 YOLOv8 检测，识别鸽子等目标后由 Pan-Tilt 云台（PCA9685 驱动舵机）瞄准目标中心，到位后通过 GPIO 继电器触发电动水枪射击，并将射击前后视频片段发送到 Telegram。支持 --no-fire、--dry-run 等安全模式与舵机紧急停止脚本。作者声明当前为无防水外壳的功能原型，整个项目开发过程借助 Claude 辅助完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Hailo-8 上运行 YOLOv8 实时检测（约 30 fps，GStreamer 管线）
- Pan-Tilt 云台瞄准 bbox 中心，误差小于阈值后触发电动水枪
- 射击视频片段通过 Telegram 推送并带冷却机制
- 提供舵机校准表与 16 通道 PWM 紧急停止脚本

## 适用场景

- 在阳台或庭院驱赶鸽子等鸟类
- 学习树莓派 + Hailo 边缘 AI 检测与云台控制的完整链路
- 作为人机协作 AI 物理世界实验的参考项目

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L44: Caméra → Détection Hailo (YOLOv8) → si cible confiante :
> L50: Détection live validée : GStreamer `libcamerasrc → 640×640 RGB → hailonet → hailofilter → appsink` (~30 fps).

## 星数曲线

```mermaid
xychart-beta
    title "tarraschk/GardenGuardian 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `894d05571889` · [字段定义](../../DATASET.md)*
