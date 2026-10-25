# SiliconLabsSoftware/arduino

⭐ 167 · C · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/SiliconLabsSoftware/arduino) · 组织维护

**让 Silicon Labs MCU 开发板接入 Arduino 生态的板级核心包**

面向使用 Silicon Labs EFR32/BGM 系列芯片开发板的 Arduino 板级支持包，覆盖 Arduino Nano Matter、xG24/xG27 Dev Kit、Seeed XIAO MG24 等 8 种板卡。通过 Arduino IDE 2.x 的 Boards Manager 安装，支持 BLE、Matter、Zigbee 多协议栈选择（Matter/Zigbee 资源占用较大），捆绑 Matter/Zigbee/ArduinoLowPower 等十余个库，其中 SilabsTFLiteMicro 提供 TensorFlow Lite for Microcontrollers 的设备端 AI/ML 能力。支持 J-Link 与 OpenOCD 调试；限制：USB-UART 桥默认仅支持 115200 bps。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 8 种 Silicon Labs 硬件板卡（BLE/Matter/Zigbee 组合）
- 捆绑 Matter 与 Zigbee 设备库及十余个外设驱动库
- SilabsTFLiteMicro 库支持设备端 TensorFlow Lite AI/ML
- 板载 SEGGER J-Link 调试器可从 Arduino IDE 使用

## 适用场景

- 用 Arduino IDE 开发 Silicon Labs 开发板的 BLE/Matter/Zigbee 应用
- 在 MCU 上运行 TensorFlow Lite Micro 推理
- 制作基于 BLE 的智能家居传感器（BTHome v2）

## 场景标签

 · 领域:嵌入式/物联网硬件开发

## 证据(README 行号)

> L3: This project enables **Silicon Labs** hardware to be used with the **Arduino** ecosystem.
> L89:  - **SilabsTFLiteMicro 🤖** - TensorFlow Lite for Microcontrollers AI/ML library [docs]

## 星数曲线

```mermaid
xychart-beta
    title "SiliconLabsSoftware/arduino 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-25"]
    y-axis "stars" 166 --> 168
    line [167, 167]
```

2026-10-22 167 → 2026-10-25 167（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `8bb27d3d2e9a` · [字段定义](../../DATASET.md)*
