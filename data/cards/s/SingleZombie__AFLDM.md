# SingleZombie/AFLDM

⭐ 108 · Python · NOASSERTION · 推送 2025-12-09 · [GitHub](https://github.com/SingleZombie/AFLDM) · [官网](https://zhouyifan.net/AF-LDM-Page/) · 组织维护 · 中文 README

**CVPR 2025 论文官方实现：改善 LDM 分数平移等变性的免混叠框架**

Alias-free Latent Diffusion Models 的官方 PyTorch 实现：针对 LDM 的 VAE 与去噪网络对分数平移不等变的问题，提出免混叠框架改善潜在扩散模型的分数平移等变性。提供推理脚本（无条件生成平移、视频编辑、图像插值、超分辨率、法向估计）与训练脚本（ImageNet 上训练免混叠 VAE/LDM/超分模型）。限制：微调后的免混叠 Stable Diffusion 生成能力弱，仅能做简单编辑；超分非盲超分，退化函数固定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提出免混叠框架改善 LDM 的分数平移等变性
- 覆盖视频编辑、图像插值、超分辨率、法向估计等应用
- 提供 ImageNet 上的 VAE/LDM/I2SB 超分训练脚本
- 基于 Diffusers 构建，CVPR 2025 论文官方实现

## 适用场景

- 复现论文中的平移等变性实验与各类应用
- 在 ImageNet 上训练免混叠 VAE 与潜在扩散模型
- 在视频编辑或图像插值任务中使用该框架

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L12: Official PyTorch implementation of Alias-free latent diffusion models.
> L18: We found the VAE and denoising network in LDM are not equivariant to fractional shifts. We propose an alias-free fr

## 星数曲线

```mermaid
xychart-beta
    title "SingleZombie/AFLDM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-29 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `22c4780b296d` · [字段定义](../../DATASET.md)*
