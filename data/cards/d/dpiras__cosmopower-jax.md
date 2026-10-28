# dpiras/cosmopower-jax

⭐ 50 · Jupyter Notebook · GPL-3.0 · 推送 2025-11-27 · [GitHub](https://github.com/dpiras/cosmopower-jax) · 个人维护

**JAX 可微分宇宙学功率谱模拟器，加速高维贝叶斯推断**

CosmoPower 的 JAX 扩展：用神经网络模拟器给出宇宙学功率谱（如 CMB 温度谱）的可微分预测，支持在 CPU 和 GPU 上以数百参数运行 Hamiltonian Monte Carlo，并提供导数计算。兼容复用原 CosmoPower 训练的 .pkl 模型（无需重训练），含 TensorFlow>=2.14 模型转换脚本与示例 Jupyter notebook。以 pip 包提供；当前不提供在 JAX 中训练神经网络的代码。面向宇宙学研究者，附 arXiv 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 宇宙学功率谱的可微分预测与导数计算
- 支持数百参数的 Hamiltonian Monte Carlo，CPU/GPU 运行
- 可复用原 CosmoPower 的 .pkl 模型（含 TF>=2.14 转换脚本）
- GPL-3 许可，附论文与 Jupyter 示例

## 适用场景

- 宇宙学参数的高维贝叶斯推断（如含大量 nuisance 参数的 MCMC）
- 在 JAX 流水线中获取功率谱及其梯度
- 把已有 CosmoPower 训练模型迁移到 JAX 使用

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L8: `CosmoPower-JAX` in an extension of the CosmoPower framework to emulate cosmological power spectra in a differentiab
> L36:  emulator = CPJ(probe='cmb_tt')
> L37:  emulator_predictions = emulator.predict(cosmo_params)

## 星数曲线

```mermaid
xychart-beta
    title "dpiras/cosmopower-jax 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-28 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a7874c8c6409` · [字段定义](../../DATASET.md)*
