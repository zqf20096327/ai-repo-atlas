# hissain/jscipy

⭐ 25 · Java · MIT · 推送 2026-06-21 · [GitHub](https://github.com/hissain/jscipy) · [官网](https://hissain.github.io/jscipy) · 个人维护

**面向 JVM 与 Android 的 Java 科学计算/信号处理库**

受 Python SciPy 启发的 Java 科学计算与信号处理库，运行于 JVM 与 Android。模块覆盖 IIR/FIR 滤波（Butterworth、Chebyshev、Elliptic、Bessel、firwin）、FFT/DCT/STFT/Hilbert 变换、Welch PSD、峰值检测、波形生成、插值与 RK4 ODE 求解器。各模块以 Python SciPy 输出为基准做'Golden Master'精度测试（RMSE）。以 Gradle/Maven 依赖形式从 Maven Central 分发，无需前置依赖，另提供 Android 示例应用；MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 滤波/变换/谱分析/插值/ODE 等科学计算模块，API 命名对齐 SciPy
- 以 Python SciPy 为基准的 Golden Master 精度测试（RMSE 报告）
- 支持 JVM 与 Android，经 Maven Central 以 Gradle 依赖分发
- zero-phase（filtfilt）、SOS（sosfilt）等多种滤波模式

## 适用场景

- 在 JVM/Android 的 ML 流水线中做信号处理，替代调用 Python SciPy
- Java 项目中的滤波、FFT、谱分析与峰值检测
- Android 应用内运行科学计算与 DSP 算法

## 场景标签

 · 领域:科学计算/信号处理

## 证据(README 行号)

> L13: **jSciPy** is a comprehensive **Java Scientific Computing and Signal Processing Library** designed for **Machine Le
> L21: In modern machine learning workflows, most signal processing tasks rely on Python's SciPy utilities. However, there

## 星数曲线

```mermaid
xychart-beta
    title "hissain/jscipy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `8561a096c1f6` · [字段定义](../../DATASET.md)*
