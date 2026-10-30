# berndporr/deepNeuronalFilter

⭐ 15 · C++ · GPL-3.0 · 推送 2025-11-26 · [GitHub](https://github.com/berndporr/deepNeuronalFilter) · [官网](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0277974) · 个人维护

**闭环深度学习滤波库：借助噪声参考信号去除信号噪声**

C++ 实现的 Deep Neuronal Filter（DNF）库，用深度学习进行闭环自适应滤波，从含噪信号中去除噪声，需要提供噪声参考信号。依赖 IIR/FIR 滤波库（iir1/fir1）与 boost，用 cmake+make 编译并 sudo make install 安装；OpenCV 仅为 EEG 示例的实时绘图可选项。附 eeg_filter 与 eeg_sim 两个 EEG 去噪示例程序，另提供在线与 PDF 文档及 libtorch 版本链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 闭环滤波：借助噪声参考信号去除信号噪声
- 提供真实与模拟 EEG 数据去噪示例程序（eeg_filter / eeg_sim）
- 依赖 iir1/fir1 滤波库，cmake+make 构建
- 另有 libtorch 版本的 DNF 可用

## 适用场景

- 用噪声参考信号对生理信号（如 EEG）做去噪
- 实时信号去噪处理与可视化
- 嵌入式/实时 DSP 场景下的深度学习滤波开发

## 场景标签

 · 领域:数字信号处理/深度学习

## 证据(README 行号)

> L1: # Deep Neuronal Filter (DNF)
> L59:  - eeg_filter: removes noise from real EEG data (release)

## 星数曲线

```mermaid
xychart-beta
    title "berndporr/deepNeuronalFilter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `56956838d758` · [字段定义](../../DATASET.md)*
