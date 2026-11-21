# SanTiwari07/PotHoleDetection

⭐ 10 · Python · MIT · 推送 2026-11-05 · [GitHub](https://github.com/SanTiwari07/PotHoleDetection) · [官网](https://santiwari07.github.io/PotHoleDetection/) · 组织维护

**低成本坑洞检测系统：摄像头+加速度计双确认并记录位置与严重度**

IPDS 用两块 ESP32 组成传感器系统：ESP32-CAM 串流视频到笔记本电脑，运行微调后的 YOLOv8m 检测坑洞，SORT 跟踪赋稳定 ID；当轨迹越过参考线时向传感器节点查询 MPU6050 加速度计数据，仅当视觉检测与冲击信号同时成立才记录事件，输出含 DS3231 时间戳、NEO-6M GPS 坐标和 0–1 严重度分数的 CSV 与标注视频。提供 Colab、Wokwi 模拟与 Gradio UI 无硬件体验路径；离线模式跳过融合门，严重度仅基于视觉。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLOv8m + SORT 跟踪，每个坑洞计一次并赋持久 ID
- 视觉与加速度计双确认融合门（70% 置信度 + 30% 冲击）
- CSV 日志含 GPS、RTC 时间戳，可导出 GeoJSON 上地图
- Colab / Wokwi / Gradio 三种无硬件试用路径

## 适用场景

- 在道路巡检视频中离线检测并统计坑洞
- 搭建低成本车载设备生成带 GPS 的坑洞维护日志
- 将坑洞记录转成 GeoJSON 在 QGIS 等地图工具查看

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: **A low-cost dual-ESP32 + YOLOv8 rig that detects potholes in real time, tracks them, confirms each one with an acce
> L43: A pothole is logged only if the camera sees it **and** the accelerometer feels it. Severity (0–1) = 70% detection c

## 星数曲线

```mermaid
xychart-beta
    title "SanTiwari07/PotHoleDetection 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-18 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `d7fdfeac8bff` · [字段定义](../../DATASET.md)*
