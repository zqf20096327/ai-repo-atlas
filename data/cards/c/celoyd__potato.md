# celoyd/potato

⭐ 87 · Python · NOASSERTION · 推送 2026-01-17 · [GitHub](https://github.com/celoyd/potato) · 个人维护

**小型卫星影像全色锐化（pansharpening）模型，生成高分辨率彩色影像**

Potato 是一个 pansharpening 研究项目：输入卫星采集的全色（高分辨率灰度）与多光谱（低分辨率彩色）影像，输出融合后的高分辨率彩色影像，模型为参数量少于 5 万的小型卷积神经网络。采用 5 个可见光波段到 oklab 色彩空间的拟合矩阵变换训练，损失函数为逐像素 oklab ΔE，并在训练中注入合成传感器伪影以处理全分辨率数据。提供快速上手指南、文档与训练基础设施，面向需要处理卫星影像的用户，非商业用途免费。README 展示了与 Maxar、Google Earth 及 ZS-Pan 的输出对比。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 少于 5 万参数的小型 CNN 完成 pansharpening
- 波段→oklab 拟合色彩变换训练，逐像素 ΔE 损失
- 训练时注入合成传感器伪影以适应全分辨率数据
- 提供文档、训练基础设施与快速上手指南

## 适用场景

- 把卫星全色与多光谱影像融合成高分辨率彩色影像
- 对现有商业/研究 pansharpening 输出做对比分析
- 作为 pansharpening 方法的科研参考实现

## 场景标签

`图像视频处理` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L17: Potato is a pansharpening research project. It contains a working pansharpener, documentation, and training infrast
> L27: Potato is a small convolutional neural network, with fewer than 50k parameters. This is smaller than the smallest o

## 星数曲线

```mermaid
xychart-beta
    title "celoyd/potato 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 85 --> 88
    line [86, 87, 87]
```

2026-10-18 86 → 2026-10-31 87（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `4695c796974f` · [字段定义](../../DATASET.md)*
