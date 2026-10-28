# julian-8897/conv-vae-pytorch

⭐ 20 · Jupyter Notebook · MIT · 推送 2026-04-03 · [GitHub](https://github.com/julian-8897/conv-vae-pytorch) · 个人维护

**PyTorch 卷积 VAE 实现：在 CelebA 上训练图像重建与生成**

标准变分自编码器（VAE）的 PyTorch 实现：编码器为卷积网络，解码器为转置卷积网络，近似后验为对角协方差的全因子高斯分布。支持在 CelebA 数据集上训练，图像从 178x218 缩放裁剪为 64x64 以加快训练。以 proof of concept 定位，提供训练、断点恢复与测试脚本，并在 128 与 256 维潜空间下展示重建与生成样本。需 Python>=3.9、PyTorch>=1.9，通过 git clone 与 requirements.txt 安装。

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

- 卷积编码器 + 转置卷积解码器的标准 VAE 实现
- 支持 CelebA 数据集训练与断点恢复
- 提供图像重建与生成两类任务的评估结果（128/256 维潜空间）

## 适用场景

- 学习或验证 VAE 的 PyTorch 实现细节
- 在 CelebA 上训练并复现图像重建与生成实验
- 作为 VAE 相关研究的代码起点

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L12: A PyTorch implementation of the standard Variational Autoencoder (VAE). The amortized inference model (encoder) is 
> L16: The VAE model was evaluated on several downstream tasks, such as image reconstruction and image generation. Some sa

## 星数曲线

```mermaid
xychart-beta
    title "julian-8897/conv-vae-pytorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `6def306c3366` · [字段定义](../../DATASET.md)*
