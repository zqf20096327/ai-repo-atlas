# Tencent-Hunyuan/Twins

⭐ 39 · Python · MIT · 推送 2026-07-26 · [GitHub](https://github.com/Tencent-Hunyuan/Twins) · 组织维护 · 中文 README

**ICML 2026 论文代码：focal loss 训练统一表示的扩散生成**

腾讯混元发布的 Twins 论文官方代码（ICML 2026），发布其中生成实验部分：在 SigLIP2 编码器 + Flux-VAE 组成的表示自编码器（RAE）潜空间上，训练 Stage-2 双头扩散 Transformer（DiTDH-XL），使用 focal/MSE 目标建模连续表示目标。提供 ImageNet-1k 上的单节点/多节点训练脚本、ODE（Euler）采样（支持 classifier-free guidance 与 autoguidance）、FID 评估流程；全部配置由 OmegaConf YAML 驱动。面向复现论文实验的科研人员。

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

- SigLIP2 + Flux-VAE 表示自编码器潜空间上的 Stage-2 扩散 Transformer 训练
- focal/MSE 损失建模连续表示目标
- 支持单节点（默认 8 GPU）与多节点训练
- 提供 CFG/autoguidance 采样与 FID-50k 评估脚本

## 适用场景

- 复现论文中 ImageNet-1k 上的生成实验
- 在自定义数据上训练统一表示的潜空间扩散模型
- 对比 focal loss 与 MSE 目标的生成效果

## 场景标签

`图像生成` `模型训练` · 领域:内容生成

## 证据(README 行号)

> L6: Twins learns to predict a **unified representation** for multimodal understanding and
> L9: This repository releases the generation experiment from the paper: a Stage-2 latent

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/Twins 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-30 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d4b02218e9f7` · [字段定义](../../DATASET.md)*
