# mikeoliphant/NeuralAudio

⭐ 149 · C++ · MIT · 推送 2026-10-09 · [GitHub](https://github.com/mikeoliphant/NeuralAudio) · 个人维护

**在实时音频应用中运行神经放大器模型的 C++ 库**

面向实时音频开发的 C++ 库，加载并运行神经放大器建模（NAM）WaveNet/LSTM 及 RTNeural keras 模型，用 Process() 接口按采样块处理音频。内置优化静态实现（A1/A2 多种架构），未覆盖的架构回退到 NAM Core 或 RTNeural 动态实现。支持输入输出校准（dBu）、质量缩放因子、外采样率过采样、模型元数据与感受野查询，并标注各操作的实时安全性。通过 git clone 加 CMake 编译构建，提供多个编译优化选项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 NAM WaveNet/LSTM（A1/A2）与 RTNeural keras（LSTM/GRU）模型
- 内置优化静态实现，未覆盖架构回退到 NAM Core 或 RTNeural
- 输入/输出 dB 校准与模型质量缩放（0.0-1.0）
- 实时安全注意事项在各 API 中明确标注

## 适用场景

- 在音频插件或实时音频应用中运行吉他放大器捕获模型
- 按性能与质量需求切换模型加载实现与质量缩放
- 跨平台（Linux/macOS/Windows）嵌入神经音频处理能力

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: NeuralAudio is a C++ library designed to make it easy to use neural network machine learning models (ie: guitar ampl
> L13: - Neural Amp Modeler (NAM) WaveNet and LSTM models, A1 and A2 support

## 星数曲线

```mermaid
xychart-beta
    title "mikeoliphant/NeuralAudio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 148 --> 151
    line [150, 149, 149]
```

2026-10-18 150 → 2026-10-31 149（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8d58edf63be8` · [字段定义](../../DATASET.md)*
