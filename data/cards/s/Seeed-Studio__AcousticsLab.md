# Seeed-Studio/AcousticsLab

⭐ 24 · C++ · GPL-3.0 · 推送 2026-08-27 · [GitHub](https://github.com/Seeed-Studio/AcousticsLab) · [官网](https://seeed-studio.github.io/AcousticsLab/) · 组织维护

**面向 MCU/SBC 的声音与振动分析嵌入式 AI 框架**

Seeed Studio 维护的跨平台声学与振动分析框架，运行于 ESP32 等微控制器与单板机：内含 GEDAD 轻量异常检测算法（陀螺仪/三轴加速度计数据）与语音命令关键词识别（兼容 Teachable Machine 训练的模型）。采用分层架构：硬件抽象层（HAL）、核心库（DSP/ML）、API 与应用层，可移植到 Arduino、MicroPython 等平台。配套 Python Web 控制台实时可视化音频/振动数据并控制设备；通过 ESP-IDF v5.4.1 工具链构建烧录。GPLv3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GEDAD 轻量级陀螺仪/加速度计异常检测算法
- 语音命令关键词识别，兼容 Teachable Machine 训练的模型
- 分层架构：HAL + 核心库 + API + 应用层，支持移植到 Arduino/MicroPython
- Web 控制台实时可视化音频/振动数据并控制设备

## 适用场景

- 在 ESP32 等 MCU 上部署声音事件与关键词识别
- 对陀螺仪/加速度计数据做设备端异常检测
- 通过 Web 控制台实时查看声学传感器数据与分析结果

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: AcousticsLab is a cross-platform framework for sound and vibration analysis, with advanced algorithms for anomaly de
> L51: - Gyroscope Euclidean Distance Anomaly Detection (GEDAD): A lightweight algorithm for detecting anomalies in gyrosc
> L53: - Speech Commands: An algorithm for recognizing keywords and simple audio events, compatible with models trained us

## 星数曲线

```mermaid
xychart-beta
    title "Seeed-Studio/AcousticsLab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `5fd14c830e2b` · [字段定义](../../DATASET.md)*
