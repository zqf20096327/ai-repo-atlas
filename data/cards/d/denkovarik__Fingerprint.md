# denkovarik/Fingerprint

⭐ 13 · Jupyter Notebook · 推送 2026-01-27 · [GitHub](https://github.com/denkovarik/Fingerprint) · 个人维护

**用 GAN 增强潜指纹图像的研究项目，PyTorch 实现**

针对潜指纹识别中的低质量图像增强问题，基于 PyTorch DCGAN 教程改编的 GAN 生成增强的二值指纹图像；判别器含两部分——常规真假判别网络与用于保持脊线结构相似的孪生网络，两部分损失合并计算。训练数据为用 Anguli 合成生成的近百万张指纹图像（含 1 万个唯一指纹，约 17GB）。项目在 Paperspace Notebook 中开发，README 记录了多轮 GAN 与孪生网络实验，包括类别分组应对 mode collapse、孪生网络测试准确率 93%-97% 等结果。

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

- 判别器组合常规判别网络与孪生网络，约束增强图像保留原指纹脊线结构
- 合成数据集含近百万张指纹图像（1 万个唯一指纹，约 17GB）
- 孪生网络在未增强指纹图像上报告 97% 测试准确率（2.0 版）
- 通过类别分组批处理与降低判别器学习率缓解 mode collapse

## 适用场景

- 研究 GAN 用于潜指纹增强以提升匹配准确率
- 复现指纹 GAN 与孪生网络训练实验
- 获取合成指纹数据集用于指纹识别研究

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L6: An open problem in the area of Latent Fingerprint Recognition is the enhancement of poor quality fingerprints. Altho
> L8: The GAN in this repo was adapted from PyTorch DCGAN TUTORIAL. It is similar to traditional GANs, but its discriminat

## 星数曲线

```mermaid
xychart-beta
    title "denkovarik/Fingerprint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f58a9df21f60` · [字段定义](../../DATASET.md)*
