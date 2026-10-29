# CherylHuang/Faces2Anime

⭐ 108 · Jupyter Notebook · 推送 2026-03-04 · [GitHub](https://github.com/CherylHuang/Faces2Anime) · 个人维护 · 中文 README

**人脸转动漫/卡通风格的 GAN 风格迁移模型（硕士论文项目）**

基于 Swapping Autoencoder 框架的人脸到动漫/漫画/卡通风格迁移实现，属 2021 年 NTUST 硕士论文配套代码。训练方式为克隆原 swapping-autoencoder-pytorch 仓库并用本仓库代码覆盖若干文件；测试通过 Jupyter Notebook 进行，并提供两个已训练权重（.pt）。README 声明代码基于较早框架、以教育为目的，可能未清理优化。模型仅支持纹理语义的风格迁移，无法插值结构信息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 人脸到动漫/卡通的 GAN 风格迁移实现
- 提供两个已训练模型权重（model34/model42）
- 支持训练集内外风格、均值风格迁移与纹理插值
- 训练数据含 22,741 张 WEBTOON 动漫图像与 StyleGAN2/CelebA 人脸

## 适用场景

- 研究生成式人脸卡通化与风格迁移方法
- 复现并对比人脸风格迁移论文结果
- 作为 GAN 图像翻译的教学参考代码

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L7: This project is aim to accomplish style transfer from human faces to anime / manga / cartoon styles.
> L14: 1. Clone the original swapping-autoencoder-pytorch repo.
> L69: Unfortunately, our model fail to interpolate structures as it can only be applied to texture semantic style transfe

## 星数曲线

```mermaid
xychart-beta
    title "CherylHuang/Faces2Anime 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-29 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ecf556fdd428` · [字段定义](../../DATASET.md)*
