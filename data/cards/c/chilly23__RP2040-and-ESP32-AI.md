# chilly23/RP2040-and-ESP32-AI

⭐ 54 · Python · MIT · 推送 2026-08-17 · [GitHub](https://github.com/chilly23/RP2040-and-ESP32-AI) · 个人维护

**ESP32-S3 上本地运行 28.9M 参数 TinyLM 的双板嵌入式演示**

由 ESP32-S3 与 RP2040 组成的双板端侧 AI 演示：ESP32-S3 运行 28.9M 参数 PLE TinyLM 模型完成纯本地文本生成，模型存于自定义 flash 分区并内存映射，热输出头与暂存缓冲置于 PSRAM；RP2040 作为显示节点，经 UART 接收生成文本并在 128x64 I2C OLED（U8g2）上渲染。仓库含 ESP32 固件、可移植 C 推理运行时、宿主侧导出/数值校验/困惑度检查工具及 RP2040 显示节点程序。基于 slvDev/esp32-ai 工作，训练数据为 TinyStories，采用 Per-Layer Embeddings（Gemma 3n）技术，无需云端 API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ESP32-S3 运行 28.9M 参数 PLE TinyLM，模型存 flash 分区并内存映射
- 共享于宿主与 ESP32 的可移植 C 推理运行时（llm.h）
- 宿主侧模型导出、数值正确性与困惑度校验工具
- RP2040 经 UART 接收生成文本并在 OLED 显示

## 适用场景

- 在微控制器上体验完全本地的小型语言模型推理
- 学习嵌入式 LLM 的模型量化、分区与 PSRAM 部署流程
- 搭建 ESP32+RP2040 双板串口显示的端侧 AI 硬件演示

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: RP2040 and ESP32 AI is a two-board embedded AI demo built around an ESP32-S3
> L31: - ESP32-S3 runs the actual 28.9M-parameter PLE TinyLM model
> L68: memory-maps it, stages the hot buffers in PSRAM, and generates text from the

## 星数曲线

```mermaid
xychart-beta
    title "chilly23/RP2040-and-ESP32-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-26 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8efd8b3c2a69` · [字段定义](../../DATASET.md)*
