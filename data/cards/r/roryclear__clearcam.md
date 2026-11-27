# roryclear/clearcam

⭐ 2,881 · Python · GPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/roryclear/clearcam) · [官网](https://clearcam.org) · 个人维护

**给任意 RTSP 监控摄像头添加目标检测、追踪与通知的 NVR**

自托管 NVR 软件：对 RTSP 摄像头画面运行目标检测与追踪，生成事件通知与剪辑，支持 AI 通知摘要（Qwen3 VL）与搜索。服务器端通过 Python 从源码运行，浏览器访问 localhost:8080；可通过 Web Push（VAPID）或自定义 URL 对接 Home Assistant、Pushover、N8N 等接收通知。提供 iOS/Android 应用用于远程查看实时画面、事件剪辑与接收通知（premium 功能）。Windows 需 ffmpeg 修复，未正式支持。

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

- 对任意 RTSP 摄像头运行目标检测与追踪（YOLOv9/tinygrad）
- AI 通知摘要（Qwen3 VL）与事件搜索
- 浏览器 Web Push 通知及自定义通知 URL（Home Assistant/Pushover/N8N）
- iOS/Android 应用远程查看实时画面与事件剪辑

## 适用场景

- 给现有 RTSP 摄像头添加检测与通知功能
- 自托管监控，接 Home Assistant 自定义告警
- 手机远程查看摄像头画面与事件剪辑

## 场景标签

`目标检测` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: # clearcam: Add object detection, tracking, mobile notifications, AI summaries, and search to any security camera.
> L41: ## run NVR + inference in python from source
> L46: - use DEV=AMD / DEV=NV python3.12 clearcam.py if your CPU is being used instead of your GPU

## 星数曲线

```mermaid
xychart-beta
    title "roryclear/clearcam 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 1938 --> 2966
    line [2023, 2026, 2039, 2062, 2099, 2129, 2173, 2210, 2218, 2023, 2257, 2266, 2362, 2520, 2572, 2595, 2638, 2669, 2697, 2719, 2730, 2740, 2749, 2766, 2802, 2853, 2881]
```

2026-10-25 2,023 → 2026-11-27 2,881（+858）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `4c5141859f57` · [字段定义](../../DATASET.md)*
