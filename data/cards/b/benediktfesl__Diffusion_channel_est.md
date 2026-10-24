# benediktfesl/Diffusion_channel_est

⭐ 88 · Python · BSD-3-Clause · 推送 2026-06-17 · [GitHub](https://github.com/benediktfesl/Diffusion_channel_est) · 个人维护

**扩散模型做低复杂度 MIMO 信道估计的论文源码**

IEEE Wireless Communications Letters 2024 论文 'Diffusion-Based Generative Prior for Low-Complexity MIMO Channel Estimation' 的源码实现：用轻量 CNN 结合 SNR 位置嵌入学习稀疏角度域信道分布，配合避免随机重采样并截断反向扩散步骤的估计策略，实现低复杂度、低内存开销的信道估计。提供在 Zenodo 数据集上评估预训练模型、从零训练与基线估计器评估的脚本。测试环境为 Python 3.10 与 PyTorch 2.1.1，运行命令默认指定 cuda:0。另提供可复用的 diffusers 兼容 DMSE 调度器独立包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扩散模型估计器，含 MSE 最优估计收敛性证明
- 轻量 CNN + SNR 位置嵌入学习稀疏角度域信道分布
- 避免随机重采样并截断低 SNR 反向扩散步骤的估计策略
- 提供预训练模型评估、从零训练与基线对比脚本

## 适用场景

- 复现论文中 MIMO 信道估计的数值实验
- 在自有信道数据集上训练扩散模型信道估计器
- 复用 DMSE 调度器到其他 diffusers 兼容项目

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: Source code of the paper
> L11: This letter proposes a novel channel estimator based on diffusion models (DMs), one of the currently top-rated gene

## 星数曲线

```mermaid
xychart-beta
    title "benediktfesl/Diffusion_channel_est 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 87 --> 89
    line [88, 88]
```

2026-10-18 88 → 2026-10-24 88（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `e50b5bf06f58` · [字段定义](../../DATASET.md)*
