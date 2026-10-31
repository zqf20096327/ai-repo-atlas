# ARM-software/CMSIS-Stream

⭐ 40 · C++ · Apache-2.0 · 推送 2026-06-04 · [GitHub](https://github.com/ARM-software/CMSIS-Stream) · [官网](https://arm-software.github.io/CMSIS-Stream/main/) · 组织维护

**面向嵌入式与富 OS 的低开销 AI/多媒体数据流框架**

ARM 维护的 CMSIS-Stream 框架，将视频、音频、DSP 与 AI 组件统一在同一数据流图中处理。由 Python 包描述图结构并在构建期生成静态调度代码（C++ 状态机、C API），运行时无 RTOS 依赖，可跑在裸机、Zephyr/CMSIS-RTOS 或 Posix/Linux/Mac 上。图组件间通过 dataflow 交换数据流，可选事件图以类似 RPC 的命名事件通信。仓库含 Cortex-M 关键词识别示例（MFCC + TFLM + 多数投票，使用 Helium 与 Ethos NPU）。带跨进程 IPC 的 Linux 版本开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 构建期计算静态调度并生成 C++ 调度器代码（C API）
- 支持裸机（无 RTOS）、Zephyr、CMSIS-RTOS、Posix 运行时
- 视频/音频/DSP/AI 组件统一在同一数据流图
- 可选事件图支持命名事件与参数的 RPC 式通信

## 适用场景

- 在 Cortex-M 等嵌入式板上搭建 AI + DSP 数据流应用
- 关键词识别等边缘 AI demo 的图构建与调度生成
- 同一框架下统一处理音视频流与 AI 推理组件

## 场景标签

 · 领域:嵌入式/边缘 AI 框架

## 证据(README 行号)

> L3: CMSIS-Stream is a low overhead framework that can be used to build AI + multi-media applications.
> L19: * Generate a **static scheduling** of the streaming graph that is computed **at build time** with several memory op

## 星数曲线

```mermaid
xychart-beta
    title "ARM-software/CMSIS-Stream 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-31"]
    y-axis "stars" 37 --> 41
    line [38, 39, 40, 40]
```

2026-10-18 38 → 2026-10-31 40（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f3246f1a2c77` · [字段定义](../../DATASET.md)*
