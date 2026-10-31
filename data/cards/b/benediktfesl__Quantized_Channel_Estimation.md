# benediktfesl/Quantized_Channel_Estimation

⭐ 15 · Python · NOASSERTION · 推送 2026-05-05 · [GitHub](https://github.com/benediktfesl/Quantized_Channel_Estimation) · 组织维护

**论文实现：粗量化系统的信道估计（GMM/MFA/VAE 生成模型）**

TUM 团队 IEEE TSP 2024 论文的官方代码实现，面向无线通信与信号处理研究者。基于条件高斯潜变量生成模型（GMM/MFA/VAE）学习信道分布先验，通过条件 Bussgang 分解导出参数化线性 MMSE 信道估计器，用于粗量化系统；支持从量化导频观测直接训练而无需真实信道样本。以 Python 脚本形式提供（Bussgang_GMM/MFA/VAE 等），GMM 变体支持 full/circulant/toeplitz 等多种协方差结构。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Bussgang-GMM / MFA / VAE 三类估计器实现
- 可从量化训练数据学习，无需真实信道样本
- GMM 支持 full/circulant/block-toeplitz 等结构化协方差
- 包含复现论文图 2 的协方差恢复脚本

## 适用场景

- 复现论文仿真结果并对比信道估计方法
- 在粗量化接收机场景下研究生成模型先验的信道估计
- 基于结构化协方差降低估计器内存与复杂度

## 场景标签

 · 领域:无线通信/信号处理

## 证据(README 行号)

> L10: This repository contains implementations of channel estimators for coarsely quantized systems based on conditionall
> L22: The proposed estimators are founded on conditionally Gaussian latent generative models, specifically Gaussian mixtu

## 星数曲线

```mermaid
xychart-beta
    title "benediktfesl/Quantized_Channel_Estimation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `eb14efa75b55` · [字段定义](../../DATASET.md)*
