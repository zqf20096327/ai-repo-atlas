# rust-dd/iTransformer

⭐ 22 · Rust · MIT · 推送 2026-01-10 · [GitHub](https://github.com/rust-dd/iTransformer) · [官网](https://crates.io/crates/itransformer) · 个人维护

**面向多变量时间序列预测的 iTransformer Rust 实现**

基于 Hugging Face Candle 框架的 iTransformer（倒置 Transformer）Rust 实现，用于多变量时间序列预测：将每个变量视为 token 并跨变量施加注意力，提供 ITransformer、ITransformer2D（时间 token）与 ITransformerFFT（Fourier token）三个变体，支持多种预测步长与部分变量训练后对未见变量的零样本泛化，可通过 feature 开启 macOS Metal 与 CUDA 加速。以 crates.io 库形式发布，需 Rust 与 Cargo 环境，依据清华大学团队的原始论文与实现改编。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 ITransformer / ITransformer2D / ITransformerFFT 三个模型变体
- 每个变量作为 token、跨变量注意力的倒置架构
- Metal（macOS）与 CUDA 硬件加速（Candle feature）
- 零样本泛化：部分变量训练后可推广到未见变量

## 适用场景

- 在 Rust 项目中做多变量时间序列预测（如交通、气象、电力数据）
- 需要 GPU（Metal/CUDA）加速的时间序列建模
- 复现或扩展 iTransformer 架构的研究实验

## 场景标签

 · 领域:机器学习/时间序列预测

## 证据(README 行号)

> L7: An **iTransformer** implementation in **Rust** using Hugging Face Candle, inspired by the lucidrains iTransformer re
> L11: iTransformer introduces an **inverted Transformer architecture** designed for **multivariate time series forecastin

## 星数曲线

```mermaid
xychart-beta
    title "rust-dd/iTransformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b526d7659677` · [字段定义](../../DATASET.md)*
