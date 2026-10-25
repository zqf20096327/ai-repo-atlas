# icon-lab/FDB

⭐ 42 · Python · MIT · 推送 2026-10-08 · [GitHub](https://github.com/icon-lab/FDB) · 组织维护

**傅里叶约束扩散桥（FDB）MRI 重建的官方 PyTorch 实现**

论文《Learning Fourier-constrained Diffusion Bridges for MRI Reconstruction》（IEEE TMI 2026）的官方代码库。提供基于扩散桥模型的 MRI 图像重建的训练与推理脚本，支持单线圈与多线圈数据，可通过参数指定欠采样率（如 R=2/4/8）、图像尺寸、对比度（T1/FLAIR）等。用户需自行准备 HDF5 格式数据（依赖 h5py），按依赖清单配置 Python 3.8 环境后 git clone 源码运行。代码基于 DiffuseRecon 与 Improved DDPM 的库修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扩散桥模型的训练脚本 train.py（单线圈/多线圈）
- 推理脚本 sample.py，支持欠采样率 R 与 T1/FLAIR 对比度参数
- 官方论文实现，附 BibTeX 引用条目

## 适用场景

- 复现论文中的 MRI 重建实验结果
- 在自己的单线圈或多线圈 MRI 数据上训练 FDB 模型
- 基于扩散桥方法开展医学图像重建研究

## 场景标签

 · 领域:医学影像/生成模型

## 证据(README 行号)

> L3: Official PyTorch implementation of FDB as described in the paper
> L5: Mirza, M. Usama, Onat Dalmaz, Hasan A. Bedel, Gokberk Elmas, Yilmaz Korkmaz, Alper Gungor, Salman UH Dar, Kader K. O

## 星数曲线

```mermaid
xychart-beta
    title "icon-lab/FDB 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d703a5a27a8a` · [字段定义](../../DATASET.md)*
