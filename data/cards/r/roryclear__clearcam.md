# roryclear/clearcam

⭐ 2,802 · Python · GPL-3.0 · 推送 2026-11-23 · [GitHub](https://github.com/roryclear/clearcam) · [官网](https://clearcam.org) · 个人维护

**为任意 RTSP 安防摄像头添加目标检测、追踪与通知**

自托管 NVR 系统：接入 RTSP 摄像头流，运行目标检测与追踪（含 Qwen3 VL 的 AI 通知摘要），支持区域（Zone）配置、事件片段、浏览器 Web Push 通知及可自定义的通知推送目标（Home Assistant、Pushover、N8N 等）。服务端以 Python 从源码运行，支持 AMD/NVIDIA GPU 后端与 BEAM 编译选项；另有 iOS/Android 应用用于远程查看直播、接收通知与片段，付费 Premium 提供端到端加密的远程访问。Windows 需 ffmpeg 修复。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对任意 RTSP 摄像头流做目标检测、追踪与事件搜索
- Qwen3 VL 生成的 AI 通知摘要
- 浏览器 Web Push 通知（Vapid key 配置）及自定义通知 URL
- 服务端支持 AMD/NVIDIA GPU 后端与 BEAM 性能选项

## 适用场景

- 给现有 RTSP 摄像头自托管添加检测与通知
- 通过 Home Assistant 或 Pushover 接收人员/物体检测告警
- 用 iOS/Android 应用远程查看摄像头直播与事件片段

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: # clearcam: Add object detection, tracking, mobile notifications, AI summaries, and search to any security camera.
> L41: ## run NVR + inference in python from source

## 星数曲线

```mermaid
xychart-beta
    title "roryclear/clearcam 星数(近 27 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 1940 --> 2880
    line [2018, 2020, 2023, 2026, 2039, 2062, 2099, 2129, 2173, 2210, 2218, 2023, 2257, 2266, 2362, 2520, 2572, 2595, 2638, 2669, 2697, 2719, 2730, 2740, 2749, 2766, 2802]
```

2026-10-23 2,018 → 2026-11-25 2,802（+784）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `398a4a6f3048` · [字段定义](../../DATASET.md)*
