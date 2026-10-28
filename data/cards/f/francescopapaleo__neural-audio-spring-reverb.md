# francescopapaleo/neural-audio-spring-reverb

⭐ 65 · Python · AGPL-3.0 · 推送 2026-06-12 · [GitHub](https://github.com/francescopapaleo/neural-audio-spring-reverb) · [官网](https://francescopapaleo.github.io/neural-audio-spring-reverb/) · 个人维护

**用深度神经网络建模弹簧混响的音频效果研究代码库**

基于 UPC/UPF 音乐技术组硕士论文成果的研究代码库，使用 CNN（时序卷积网络）与 LSTM/GRU 等架构对弹簧混响这一音频效果进行神经网络建模。提供 CLI 完成数据集下载（springset/egfxset/customset，来自 Zenodo）、训练、测试与推理，结果经 Tensorboard 记录；集成 Neutone SDK 可导出模型到 DAW 插件；附冲激响应测量、RT60 计算等工具。安装方式为 git clone 源码后 pip install -e .。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TCN/LSTM/GRU 架构的弹簧混响神经网络建模与训练/推理 CLI
- 从 Zenodo 下载 springset/egfxset/customset 数据集
- 集成 Neutone SDK 导出模型至 DAW 插件或独立应用
- 冲激响应测量与 RT60 计算工具

## 适用场景

- 训练自己的弹簧混响神经模型并导出到 DAW 使用
- 复现或对比虚拟模拟建模研究中的网络架构
- 测量模型或物理设备的冲激响应与 RT60

## 场景标签

 · 领域:音频信号处理/音乐技术

## 证据(README 行号)

> L3: This repository is based on the results of a Master's thesis developed at the Music Technology Group (MTG), Universi
> L5: *This project wants to address the modelling of the spring reverb, using deep neural networks, in particular: CNN (c

## 星数曲线

```mermaid
xychart-beta
    title "francescopapaleo/neural-audio-spring-reverb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-28 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `dafe963f14a3` · [字段定义](../../DATASET.md)*
