# Michedev/DDPMs-Pytorch

⭐ 89 · Python · MIT · 推送 2026-02-10 · [GitHub](https://github.com/Michedev/DDPMs-Pytorch) · 个人维护

**多篇 DDPM 扩散模型论文的 PyTorch 复现与训练库**

以 PyTorch Lightning 实现三篇扩散模型论文：Denoising Diffusion Probabilistic Models、Improved DDPM 与 Classifier-free Diffusion Guidance。提供 pip 包（含训练步骤的 Lightning 模型）与 git clone 两种使用方式，经 hatch 管理环境（cuda/cpu），通过 hydra yaml 配置训练，默认在 MNIST 上训练 Improved DDPM，支持自定义数据集与方差调度器（linear/cosine），并用 generate 脚本生成图像批次，可配置种子、设备与批次大小。

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

- 实现 DDPM / Improved DDPM / Classifier-free Guidance 三篇论文
- hydra yaml 配置训练，支持切换模型、调度器与噪声步数
- 支持 EMA、梯度裁剪与 TensorBoard 日志
- 可自定义数据集（继承 torch Dataset）与自定义方差调度器

## 适用场景

- 学习/研究扩散模型论文的实现细节
- 在自有数据集上训练 DDPM 并生成图像
- 复现论文超参数进行实验对比

## 场景标签

`图像生成` `模型训练` · 领域:内容生成

## 证据(README 行号)

> L7: Pytorch implementation of "_Improved Denoising Diffusion Probabilistic Models_",
> L8: "_Denoising Diffusion Probabilistic Models_" and "_Classifier-free Diffusion Guidance_"

## 星数曲线

```mermaid
xychart-beta
    title "Michedev/DDPMs-Pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-29 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5f119bbfa910` · [字段定义](../../DATASET.md)*
