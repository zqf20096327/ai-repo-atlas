# eren23/one_layer_image_gen

⭐ 20 · Jupyter Notebook · 推送 2025-12-20 · [GitHub](https://github.com/eren23/one_layer_image_gen) · 个人维护

**FAE 论文的 PyTorch 复现：把预训练视觉编码器适配用于图像生成**

复现论文《One Layer Is Enough: Adapting Pretrained Visual Encoders for Image Generation》核心逻辑的 PyTorch 实现：用单注意力层压缩（DeepAdapter）将 DINOv3 1024 维特征压到 64 维潜空间，配合冻结的 Feature Refiner 与像素解码器重建 RGB 图像，再以 SimpleDiT（rectified flow）在潜空间训练扩散生成。数据管线使用 COCO 2017（25,000 样本）磁盘缓存与 memory-mapped 加载。面向图像生成研究者与深度学习开发者，以 notebook cell 组织训练流程；与原论文存在多处简化（编码器、数据集、潜维度等）。

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

- DeepAdapter 将 DINOv3 特征从 1024 维压缩到 64 维潜空间
- 四阶段训练：特征对齐、解码器稳定、GAN 训练、Flow Matching
- SimpleDiT 扩散变换器采用 rectified flow，Euler 采样 50-100 步
- COCO 特征磁盘缓存（memory-mapped float16）支持流式加载

## 适用场景

- 复现或研究 FAE 的特征压缩图像生成方法
- 基于预训练视觉编码器做潜空间生成实验
- 学习多阶段（重建+GAN+流匹配）生成训练管线

## 场景标签

`图像生成` `模型训练` · 领域:内容生成

## 证据(README 行号)

> L3: A PyTorch implementation replicating the core logic of FAE (Feature Auto-Encoder) from the paper "One Layer Is Enoug
> L171: The model generates 224x224 images from pure noise by:

## 星数曲线

```mermaid
xychart-beta
    title "eren23/one_layer_image_gen 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [21, 20, 20]
```

2026-10-18 21 → 2026-10-28 20（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8ed703a200d5` · [字段定义](../../DATASET.md)*
