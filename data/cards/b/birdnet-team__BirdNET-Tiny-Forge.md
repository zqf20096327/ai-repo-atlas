# birdnet-team/BirdNET-Tiny-Forge

⭐ 28 · Python · Apache-2.0 · 推送 2025-12-01 · [GitHub](https://github.com/birdnet-team/BirdNET-Tiny-Forge) · 组织维护

**面向嵌入式设备的 BirdNET-Tiny 模型训练与部署工具链**

基于 Kedro 的机器学习流水线工具，用于训练 BirdNET-Tiny 鸟鸣识别模型并部署到嵌入式设备（当前支持 ESP32-S3-Korvo-2 V3.0）。提供数据准备工具：从 xeno-canto（需 API key）与 AudioSet 下载鸟类录音，或使用自定义音频片段；训练与部署流程通过脚本执行。系统要求 Ubuntu 24.04、Python 3.10/3.11、bazel 与 docker，需先构建修补版 tflite-micro wheel。项目自述处于早期开发阶段，不建议生产使用，API 可能变更。由 BirdNET 与 fold ecosystemics 合作维护，康奈尔 K. Lisa Yang Center 等机构支持。

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

- Kedro 流水线训练 BirdNET-Tiny 并部署到嵌入式设备
- 支持 xeno-canto / AudioSet / 自定义音频三类数据准备
- 官方支持设备 ESP32-S3-Korvo-2 V3.0，BirdWatcher PUC 计划中

## 适用场景

- 训练自己的鸟鸣识别模型并烧录到边缘设备做长期录音记录
- 从 xeno-canto 或 AudioSet 批量下载特定鸟种的训练数据
- 制作低功耗的野外鸟类声音监测设备

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L6: BirdNET-Tiny Forge simplifies the training of BirdNET-Tiny models and their deployment on embedded devices.
> L22: - ESP32-S3-Korvo-2 V3.0

## 星数曲线

```mermaid
xychart-beta
    title "birdnet-team/BirdNET-Tiny-Forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5ae66e8d6227` · [字段定义](../../DATASET.md)*
