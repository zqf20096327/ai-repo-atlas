# froehlicht/motion2midi

⭐ 32 · HTML · 推送 2025-12-04 · [GitHub](https://github.com/froehlicht/motion2midi) · [官网](https://motion2midi.com/) · 个人维护

**摄像头手部追踪驱动的 MIDI 控制插件，用于 DAW**

闭源分发的 macOS 音频插件（AU/VST3），用 YOLO 模型通过摄像头实时追踪双手位置，将左右手 X/Y 映射为 4 路 MIDI CC 输出，经 IAC Driver 虚拟 MIDI 总线路由进 DAW，可绑定任意可映射参数。README 提供下载安装、Ableton Live 与 FL Studio 的映射步骤及 FAQ。当前为 v0.9.2-beta，仅支持 macOS 12+，Windows 计划中；处理全部本地进行，需接受 EULA，禁止再分发。

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

- YOLO 手部追踪输出 4 路 MIDI CC（默认 CC 11-14，可改）
- 以 AU 与 VST3 插件形式提供，兼容 Ableton Live 11、FL Studio 21
- 支持 Mute/Solo、可视化开关、随 DAW 项目保存的设置
- 视频处理全部本地进行

## 适用场景

- 在 DAW 中用手部动作实时控制滤波器、音量等参数
- 表演或制作时用手势进行 MIDI 实时控制
- macOS 用户免鼠标调节软音源/效果器参数

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L29: - **Real-time hand tracking** using YOLO computer vision model
> L30: - **4 MIDI CC outputs** - Map left/right hand X/Y positions to any parameter

## 星数曲线

```mermaid
xychart-beta
    title "froehlicht/motion2midi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4bf5c1fad95b` · [字段定义](../../DATASET.md)*
