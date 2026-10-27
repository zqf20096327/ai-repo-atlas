# JesperDramsch/seismic-transfer-learning

⭐ 93 · Jupyter Notebook · MIT · 推送 2026-10-12 · [GitHub](https://github.com/JesperDramsch/seismic-transfer-learning) · [官网](https://library.seg.org/doi/abs/10.1190/segam2018-2996783.1) · 组织维护

**用预训练 CNN 迁移学习做地震相分类的研究代码**

SEG 2018 会议论文配套代码：在二维叠后地震剖面上应用在大规模图像数据库上预训练的图像分类网络（如 VGG16），通过迁移学习不微调地评估其对地震数据的分类表现，实现自动地震解释。使用方式为打开 Notebook、下载 F3 地震数据与 Model Zoo 中的模型后运行实验。由丹麦技术大学两位作者维护，附论文与演示引用信息。

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

- 迁移学习应用预训练 CNN 于地震相分类
- 无需微调（without fine-tuning）的评估方式
- 提供 Notebook 形式实验流程，配合 F3 数据与 Model Zoo

## 适用场景

- 复现论文中的地震相分类实验
- 探索预训练图像网络在地震数据上的迁移表现
- 地震解释的深度学习研究参考

## 场景标签

 · 领域:地球物理/深度学习

## 证据(README 行号)

> L5: > We explore propagation of seismic interpretation by deep learning in stacked 2D sections. We show the application 
> L64: We explore transfer training for automatic seismic interpretation without fine-tuning.

## 星数曲线

```mermaid
xychart-beta
    title "JesperDramsch/seismic-transfer-learning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-27 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5eaa6aab8f25` · [字段定义](../../DATASET.md)*
