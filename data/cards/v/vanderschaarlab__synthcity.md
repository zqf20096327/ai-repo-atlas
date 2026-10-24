# vanderschaarlab/synthcity

⭐ 693 · Python · Apache-2.0 · 推送 2026-04-21 · [GitHub](https://github.com/vanderschaarlab/synthcity) · [官网](https://www.vanderschaar-lab.com/) · 组织维护

**面向隐私与公平的合成表格数据生成与评估库**

synthcity 是一个 Python 库（要求 Python 3.8+），用于生成和评估合成表格数据，服务于隐私保护、公平性与数据增强场景。它提供插件化架构，收录 GAN、VAE、贝叶斯网络、归一化流、扩散模型、LLM-based（GReaT）等多类参考模型，覆盖通用表格、时间序列、静态生存分析、图像及域适应等数据类型，并包含差分隐私（PATE-GAN、DP-GAN、PrivBayes）与公平性（DECAF）方法及多种正确性与隐私评估指标。限制：不处理缺失数据，需先用 HyperImpute 等工具插补。通过 PyPI 安装，支持从源码安装及 goggle/testing 等扩展。

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

- 插件化架构，收录 GAN/VAE/贝叶斯网络/归一化流/扩散/LLM-based 等多类生成模型
- 覆盖时间序列、生存分析、图像与域适应等数据类型
- 提供差分隐私与公平性生成方法（PATE-GAN、DP-GAN、PrivBayes、DECAF）
- 内含正确性与隐私评估指标及模型基准测试能力

## 适用场景

- 为机器学习训练生成保护隐私的合成表格数据
- 医疗等敏感数据场景下做去标识化的数据发布
- 数据稀缺时用合成数据增强训练集
- 对合成数据生成器做质量与隐私基准评测

## 场景标签

 · 领域:机器学习/合成数据

## 证据(README 行号)

> L3:  A library for generating and evaluating synthetic tabular data.
> L23:  - General purpose: GAN-based (AdsGAN, CTGAN, PATEGAN, DP-GAN),VAE-based(TVAE, RTVAE), Normalizing flows, Bayesian 

## 星数曲线

```mermaid
xychart-beta
    title "vanderschaarlab/synthcity 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 691 --> 694
    line [692, 693, 693]
```

2026-10-18 692 → 2026-10-24 693（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a75b5a9f2c2c` · [字段定义](../../DATASET.md)*
