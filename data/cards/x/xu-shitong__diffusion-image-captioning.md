# xu-shitong/diffusion-image-captioning

⭐ 56 · Jupyter Notebook · 推送 2025-11-26 · [GitHub](https://github.com/xu-shitong/diffusion-image-captioning) · 个人维护

**基于扩散语言模型的图像描述生成研究实现**

论文（arXiv:2210.04559）的官方代码实现，模型名 CLIP-DiffusionLM：将去噪扩散概率模型应用于图像描述的文本生成，用较少推理步数生成图像标题。在 Flickr8k 上取得 0.1876 BLEU-4，Flickr8k+Flickr30k 联合训练取得 0.2470 BLEU-4。仓库提供 Flickr8k 的 CLIP 特征下载（Flickr30k 需自行提取）、训练代码 CLIP-DDPM.py 与超参数配置，在单块 Nvidia A30 GPU 上训练 Flickr8k 约 5 小时（15 epochs）。

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

- 去噪扩散模型用于图像描述文本生成
- 比自回归模型更少的推理步数生成标题
- 提供 Flickr8k 提取好的 CLIP 特征与训练代码/超参
- 报告 Flickr8k BLEU-4 0.1876、联合数据集 0.2470

## 适用场景

- 复现论文的扩散式图像描述生成实验
- 研究扩散语言模型在文本生成任务上的应用
- 在 Flickr8k/Flickr30k 上进行图像描述训练与评测

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: Research project on image captioning using diffusion language model. Our model is named as CLIP-DiffusionLM.
> L5: Inspired by the recent success of the denoising diffusion model on image synthesis tasks, we apply denoising diffusi

## 星数曲线

```mermaid
xychart-beta
    title "xu-shitong/diffusion-image-captioning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-26 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `497391927226` · [字段定义](../../DATASET.md)*
