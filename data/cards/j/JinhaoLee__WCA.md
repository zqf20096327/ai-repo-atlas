# JinhaoLee/WCA

⭐ 19 · Python · MIT · 推送 2026-03-23 · [GitHub](https://github.com/JinhaoLee/WCA) · 组织维护

**ICML 2024 论文 WCA 官方代码：优化 VLM 相似度分数做零样本分类**

ICML 2024 论文 Visual-Text Cross Alignment 的官方实现。方法将输入图像切分为局部图像块，用图像编码器提取局部视觉特征，再用大语言模型为类别标签生成详细文本描述，计算加权视觉-文本相似度矩阵并求和得到最终分数，以改进 CLIP 等视觉语言模型在零样本分类中的对齐。README 提供 conda 安装依赖、数据集配置（cfgs 目录）与 main.py 运行说明，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 局部视觉提示：图像切分为局部图像块编码
- LLM 生成类别详细文本描述作为文本提示
- 加权视觉-文本相似度矩阵计算最终对齐分数

## 适用场景

- 复现论文的零样本图像分类实验
- 在 CLIP 等模型基础上改进图像-文本对齐与分类精度
- 研究视觉语言模型中局部特征与 LLM 描述的对齐机制

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L29: Recent research shows that using a pre-trained vision-language model (VLM), like CLIP, to align a query image with 
> L32: **Overview of weighted visual-text cross alignment (WCA)**. The process begins with *localized visual prompting*, w

## 星数曲线

```mermaid
xychart-beta
    title "JinhaoLee/WCA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `233e749d18a8` · [字段定义](../../DATASET.md)*
