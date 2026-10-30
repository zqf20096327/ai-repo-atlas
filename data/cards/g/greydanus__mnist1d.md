# greydanus/mnist1d

⭐ 263 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/greydanus/mnist1d) · 个人维护

**MNIST 的 1D 类比数据集，用于测量空间归纳偏置**

面向深度学习研究者的合成数据集：以 40 维一维时序信号构造 0-9 数字模板，经随机填充、平移、相关噪声、缩放等变换生成默认 4000+1000 样本，规模约为 MNIST 的 1/100。不同模型（逻辑回归/MLP/CNN/GRU）在该数据集上测试精度差异明显，可用于量化 CNN 空间先验、彩票假设、深度双下降、元学习等实验。通过 pip 安装后本地生成数据，API 支持调整噪声、平移、剪切等参数；依赖 NumPy/SciPy/PyTorch。已被 Understanding Deep Learning 教材用作教学数据集，ICML 2024 论文发表。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40 维一维时序数据集，默认 4000 训练 + 1000 测试样本
- 模板经平移/相关噪声/缩放等随机变换程序化生成，参数可通过 API 调整
- 不同模型族测试精度差异显著（MLP 68% vs CNN 94%）
- 提供量化空间先验、彩票假设、双下降、元学习等示例实验 notebook

## 适用场景

- 在低算力下快速复现深度学习现象（双下降、彩票假设）
- 量化比较模型的空间归纳偏置差异
- 作为教学场景下的轻量级分类数据集

## 场景标签

 · 领域:机器学习研究/数据集

## 证据(README 行号)

> L5: Most machine learning models get around the same ~99% test accuracy on MNIST. Our dataset, MNIST-1D, is 100x smaller
> L106: This is a synthetically-generated dataset which, by default, consists of 4000 training examples and 1000 testing e

## 星数曲线

```mermaid
xychart-beta
    title "greydanus/mnist1d 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 261 --> 264
    line [262, 263, 263]
```

2026-10-18 262 → 2026-10-30 263（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7c52c042679b` · [字段定义](../../DATASET.md)*
