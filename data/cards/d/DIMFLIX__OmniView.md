# DIMFLIX/OmniView

⭐ 30 · Python · GPL-3.0 · 推送 2026-06-17 · [GitHub](https://github.com/DIMFLIX/OmniView) · [官网](https://pypi.org/project/omniview/) · 个人维护 · 中文 README

**多摄像头视频流采集与多路显示库，供计算机视觉接入**

Python 库，用于同时接收和处理多路 USB 与 IP（RTSP）摄像头视频流：支持自动重连、可配置分辨率/FPS、多线程帧处理、D3D11/VAAPI 硬件解码（失败自动回退软件），并提供 USB 2.0 集线器复用调度——自动检测共享同一 hub 的摄像头并以滚动窗口轮换（K 路活跃、其余停放）。通过 frame_callback 回调将帧交给用户处理逻辑，自带查看流的 GUI。许可为 GPL-3.0，另声明受专利保护、使用分发需书面许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- USB/IP(RTSP) 多路摄像头流管理与自动重连
- USB hub 复用：自动检测拓扑并滚动轮换避开 ENOSPC 带宽限制
- D3D11/VAAPI 硬件加速解码，自动软件回退
- frame_callback 回调系统便于接入计算机视觉处理

## 适用场景

- 多摄像头监控画面同时采集与查看
- 为计算机视觉流水线提供多路视频帧输入
- USB 2.0 hub 带宽不足时轮换驱动多台摄像头

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L23: A system for simultaneous viewing and processing of streams from multiple cameras (USB/IP) with the ability to inte
> L31: - Flexible callback system for video processing

## 星数曲线

```mermaid
xychart-beta
    title "DIMFLIX/OmniView 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2438362b19f1` · [字段定义](../../DATASET.md)*
