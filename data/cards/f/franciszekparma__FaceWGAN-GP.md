# franciszekparma/FaceWGAN-GP

⭐ 20 · Python · MIT · 推送 2026-03-22 · [GitHub](https://github.com/franciszekparma/FaceWGAN-GP) · 个人维护

**PyTorch 从零实现的 WGAN-GP 人脸生成器：从噪声生成 128x128 人脸**

从零实现的 Wasserstein GAN with Gradient Penalty（WGAN-GP）项目，用 PyTorch 训练生成器从 128 维噪声向量合成 128x128 RGB 人脸。生成器采用 ConvTranspose2d 上采样加每级 5 个残差块；判别器（critic）使用 InstanceNorm、步进卷积与 DropBlock2D 以配合梯度惩罚；判别器与生成器按 3:1 步数交替训练，Adam betas=(0.0, 0.9)，500 步线性预热。仓库仅含最佳模型检查点，完整检查点历史需邮件联系作者。曾在 NVIDIA H100 上训练 14 小时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从零实现的 WGAN-GP：梯度惩罚替代权重裁剪，约束 critic 梯度范数趋近 1
- 生成器：128 维噪声 → ConvTranspose2d 逐级上采样 + 每级 5 个残差块 → 128x128 RGB
- critic 采用 InstanceNorm、步进卷积、DropBlock2D 等适配梯度惩罚的设计
- 超参数（batch 256、1024 epochs、GP lambda 10 等）集中定义于 code/utils.py

## 适用场景

- 用自己的脸部图片数据训练 GAN 生成合成人脸
- 学习 WGAN-GP 的实现细节（梯度惩罚、critic 设计、训练循环）
- 基于现有检查点生成人脸样本并调整超参数复训

## 场景标签

`图像生成` `模型训练` · 领域:内容生成

## 证据(README 行号)

> L3: A from-scratch PyTorch implementation of a Wasserstein GAN with Gradient Penalty that learns to generate 128x128 hum
> L27: Takes a 128-dimensional noise vector and progressively upsamples it into a 128x128 RGB image.

## 星数曲线

```mermaid
xychart-beta
    title "franciszekparma/FaceWGAN-GP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `ed7db8a8c56c` · [字段定义](../../DATASET.md)*
