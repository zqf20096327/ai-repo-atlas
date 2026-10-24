# delta6189/Anime-Sketch-Colorizer

⭐ 65 · Jupyter Notebook · 推送 2026-06-28 · [GitHub](https://github.com/delta6189/Anime-Sketch-Colorizer) · 个人维护

**给开发者的动漫线稿自动上色 PyTorch 实现（参考图引导）**

基于 PyTorch 的动漫线稿自动上色项目：以参考图为条件，将线稿翻译为彩色插图，采用 GAN 架构（引用 Spectral Normalization、Attention U-Net、Weight Standardization、StyleGAN 等方法）。训练与测试通过 train.ipynb / test.ipynb notebook 进行，提供 Kaggle 上的 Anime Sketch Colorization Pair 数据集来源与 449MB 预训练 checkpoint（Google Drive）下载。README 附训练超参数（lr 2e-4、batch size 2、25 epoch）与作者训练硬件信息（GTX1060 6G、45 小时）。属研究/复现向代码，无打包安装方式。

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

- 参考图引导的线稿到彩色插图图像翻译（GAN）
- 提供 449MB 预训练 checkpoint 下载
- 训练与测试以 Jupyter notebook 形式提供（train.ipynb / test.ipynb）
- README 列出训练超参数与所用方法引用

## 适用场景

- 给动漫线稿自动生成彩色插图
- 在 Anime Sketch Colorization Pair 数据集上复现训练
- 研究参考图条件下的图像到图像翻译方法

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Automatic Sketch Colorization with reference image
> L23:  Please refer `train.ipynb`

## 星数曲线

```mermaid
xychart-beta
    title "delta6189/Anime-Sketch-Colorizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-24 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a030513d0bc7` · [字段定义](../../DATASET.md)*
