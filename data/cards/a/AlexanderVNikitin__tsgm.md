# AlexanderVNikitin/tsgm

⭐ 232 · Python · Apache-2.0 · 推送 2026-03-10 · [GitHub](https://github.com/AlexanderVNikitin/tsgm) · [官网](https://tsgm.readthedocs.io) · 组织维护

**合成时间序列数据集的生成与评估框架**

面向合成时间序列数据的开源 Python 框架（NeurIPS'24 论文），覆盖四块功能：用 GAN/VAE/结构时序等生成模型产出合成数据、7 类时序增强方法（加噪、Warping 等）、从一致性/隐私/公平性/下游性能维度评估合成数据的多组指标，以及便捷访问 140+ 常用时序数据集（UCR、EEG、股票等）。基于 Keras 3，支持 TensorFlow/PyTorch/JAX 三种后端，提供 tsgm-gd 与 tsgm-eval 两个命令行工具，要求 Python 3.8+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GAN/ConditionalGAN/BetaVAE/TimeGAN 等多种生成模型实现
- 含隐私（成员推断攻击）、公平性、下游性能的合成数据评估指标
- 140+ 常用时序数据集的统一访问 API
- Keras 3 多后端（TensorFlow/PyTorch/JAX），含 M1/M2 芯片安装指引

## 适用场景

- 训练生成模型并产出合成时间序列数据集
- 对时序数据做增强以扩充训练集
- 从一致性、隐私、下游效果等维度评估合成数据质量
- 在实验中统一加载常用时序数据集

## 场景标签

 · 领域:机器学习/时间序列生成

## 证据(README 行号)

> L23: TSGM is an open-source framework for synthetic time series dataset generation and evaluation.
> L25: The framework can be used for creating synthetic datasets (see :hammer: Generators ), augmenting time series data (

## 星数曲线

```mermaid
xychart-beta
    title "AlexanderVNikitin/tsgm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 231 --> 233
    line [232, 232]
```

2026-10-18 232 → 2026-10-25 232（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `10157056ae1b` · [字段定义](../../DATASET.md)*
