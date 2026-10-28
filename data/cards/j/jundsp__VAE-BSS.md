# jundsp/VAE-BSS

⭐ 48 · Python · GPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/jundsp/VAE-BSS) · 个人维护

**PyTorch VAE 实现的图像无监督盲源分离**

基于 PyTorch 的变分自编码器盲源分离模型实现，附带训练与评估程序，对应 EUSIPCO 2021 论文。提供预训练模型（约 75 MB），可分离混合 MNIST 手写数字图像，支持 K=2/3/4 假设源数，含普通自编码器、VAE 及带掩码 VAE 的对比。评估脚本直接使用预训练模型，训练脚本仅用混合数据以无监督方式从头训练，含隐空间维度、先验概率、批大小等超参数设置，自动下载并准备 MNIST 数据。

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

- 提供预训练模型（约 75 MB），evaluate.py 可直接运行分离混合 MNIST 图像
- 无监督训练：仅需混合数据，无需真实源图像标签
- 包含普通 AE、VAE、带掩码 VAE 三种模型对比
- train.py 支持隐空间维度、先验概率等超参数调整

## 适用场景

- 复现论文中的 VAE 盲源分离实验
- 在混合 MNIST 图像上运行预训练模型做源分离
- 调整超参数从头训练自己的 VAE 分离模型

## 场景标签

 · 领域:信号处理/深度学习

## 证据(README 行号)

> L3: A PyTorch model of the variational auto-encoder for unsupervised blind source separation, with training and evaluati
> L28: **`evaluate.py`** uses models that we pre-trained in an unsupervised way to separate mixed MNIST handwritten digit 


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7c1475f1e607` · [字段定义](../../DATASET.md)*
