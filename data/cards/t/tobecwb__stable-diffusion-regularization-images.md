# tobecwb/stable-diffusion-regularization-images

⭐ 162 · 推送 2026-10-09 · [GitHub](https://github.com/tobecwb/stable-diffusion-regularization-images) · 个人维护

**预生成的 Stable Diffusion 正则化图像数据集（512/768/1024px）**

由 tobecwb 发布的预渲染正则化图像数据集：用 Stable Diffusion 1.5、2.1 与 SDXL 1.0 基础检查点生成 man 与 woman 两个类别的图像，每类 5000 张，提供 512px、768px 与 1024px 三种尺寸，用于 Dreambooth、Textual Inversion 等训练中定义类、防止训练漂移到其他类别。生成时仅使用基础检查点与简单提示词。README 未给出安装或下载命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- man/woman 两类各 5000 张预生成图像
- 覆盖 SD 1.5 / 2.1 / SDXL 1.0 三种检查点
- 提供 512px / 768px / 1024px 三种分辨率

## 适用场景

- Dreambooth 或 Textual Inversion 训练时作为正则化图像
- 避免训练漂移到相近类别（如 toy plane）

## 场景标签

 · 领域:图像生成/训练数据

## 证据(README 行号)

> L1: # Stable Diffusion Regularization Image Dataset
> L13: All images were generated with Stable Diffusion 1.5, 2.1, and SDXL 1.0 checkpoint.
> L14: For each class (man and woman), a total of 5000 images were generated.

## 星数曲线

```mermaid
xychart-beta
    title "tobecwb/stable-diffusion-regularization-images 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 160 --> 163
    line [161, 162, 162]
```

2026-10-18 161 → 2026-10-29 162（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8118aba08ddc` · [字段定义](../../DATASET.md)*
