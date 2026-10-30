# zyinghua/uncond-image-generation-ldm

⭐ 16 · Python · 推送 2026-10-06 · [GitHub](https://github.com/zyinghua/uncond-image-generation-ldm) · 个人维护

**训练无条件潜在扩散模型的项目脚本，基于 diffusers 改写**

基于 Hugging Face diffusers 改写的无条件图像生成训练脚本：先用可更换的预训练 VQVAE 将图像压缩到潜在空间，再在潜在空间训练 DDPM UNet。预训练 VAE 可通过修改 train.py 顶部变量切换；数据支持本地文件夹、zip 文件或上传至 Hub 的数据集；通过 Accelerate 启动训练，支持单机与多 GPU 分布式，可选接入 wandb 记录日志。以 git clone 源码加 pip 安装依赖的方式使用，无打包发布形式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可更换预训练 VQVAE 的潜在扩散训练流程
- 数据集支持本地文件夹/zip/Hugging Face Hub 三种方式
- 通过 Accelerate 支持多 GPU 分布式训练
- 可选接入 wandb 记录训练日志

## 适用场景

- 在自有图像数据集上训练无条件潜在扩散模型
- 以 Oxford Flowers 等数据集学习扩散模型训练流程
- 多 GPU 环境下进行分布式扩散模型训练

## 场景标签

`图像生成` `模型训练` · 领域:内容生成

## 证据(README 行号)

> L1: ## Training an unconditional latent diffusion model
> L29: You can specify which pretrained VAE model to use by changing the `VAE_PRETRAINED_PATH` and `VAE_KWARGS` variables 
> L36: accelerate launch train.py \

## 星数曲线

```mermaid
xychart-beta
    title "zyinghua/uncond-image-generation-ldm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a1dda0c0b799` · [字段定义](../../DATASET.md)*
