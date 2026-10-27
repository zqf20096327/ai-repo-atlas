# MartinsRepo/Arduino-Uno-Q-Projects

⭐ 40 · Python · Apache-2.0 · 推送 2026-02-19 · [GitHub](https://github.com/MartinsRepo/Arduino-Uno-Q-Projects) · 个人维护

**Arduino Uno Q（Qualcomm+STM32）AI 项目教程与实验合集**

面向 Arduino Uno Q 双核架构（Qualcomm QRB2210 运行 Debian Linux 的 MPU 与 STM32U585 运行 Zephyr 的 MCU）的项目文档仓库：涵盖 SPI OLED 显示、本地 Ollama 模型运行、USB 摄像头接入、MediaPipe 人脸检测、由 LLM 解读人脸图像、在设备上运行 Agent OpenClaw 并将 Sketch 作为工具调用，以及舵机应用等。记录 Zephyr 调试、GPIO/SPI 映射排查等技术细节。受限于本地运行（USB-C SD 卡），LLM 平均响应约 90 秒，README 以此为前提给出低频决策型项目设计模式（LLM 做慢速高层决策，MCU 处理实时任务）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖本地 Ollama LLM 在 MPU 上运行、MCU 处理实时任务的分工模式
- MediaPipe 人脸检测 + LLM 人脸解读项目
- 在设备上运行 Agent OpenClaw 并将 Arduino Sketch 作为工具
- 记录 Zephyr 调试与 SPI/GPIO 映射等底层问题

## 适用场景

- 在 Arduino Uno Q 上部署本地 LLM 做低频决策型应用
- 查找双核（MPU+MCU）架构的 AI 硬件项目思路
- 排查 Zephyr 核与标准 AVR 行为差异、引脚映射问题

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L9: We document the journey of pushing this board beyond its documentation—from low-level bit-banging and Zephyr debuggi
> L24:  - Display text on a SPI driven OLED display
> L89: ## Who this is for

## 星数曲线

```mermaid
xychart-beta
    title "MartinsRepo/Arduino-Uno-Q-Projects 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-27 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3b1ad7ef0afa` · [字段定义](../../DATASET.md)*
