# tum-pbs/sparse-reconstruction

⭐ 21 · Jupyter Notebook · 推送 2026-01-20 · [GitHub](https://github.com/tum-pbs/sparse-reconstruction) · 组织维护

**用引导扩散模型从稀疏数据重建流场的论文参考实现**

慕尼黑工业大学团队发表的 Physics of Fluids 论文“Guiding diffusion models to reconstruct flow fields from sparse data”的官方实现。提供 2D 场景的 U-net 网络与训练代码（networks.py、diffusion.py 中的 masked_diffusion() 方法），以及示例 notebook 演示从预训练扩散模型采样并用掩码扩散方法从稀疏测量重建流场。使用 Kolmogorov 涡流数据集（需自行下载置于 data 目录），通过 trainer.py 脚本训练。目前仅含 2D 场景，3D 场景尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 掩码扩散引导方法（Diffusion 类的 masked_diffusion()）从稀疏测量重建流场
- 提供 2D 场景的网络与训练代码，含可调参数的 trainer.py
- 示例 notebook 演示预训练模型采样与稀疏重建流程

## 适用场景

- 复现论文中的流场稀疏重建方法
- 在 Kolmogorov 涡流数据集上训练扩散重建模型
- 基于代码开展 CFD 稀疏数据重建研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains the reference implementation of the framework presented in the article “Guiding diffusion m
> L8: The repository currently contains the network and training codes for the 2D scenario (3D scenario coming soon). More
> L11: The architecture of the U-net network behind the model can be found in `networks.py`. The implementation of our gui

## 星数曲线

```mermaid
xychart-beta
    title "tum-pbs/sparse-reconstruction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0fbb6e6e6e29` · [字段定义](../../DATASET.md)*
