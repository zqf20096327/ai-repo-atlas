# sumedhachugh/Lithography-Hotspot-Detection

⭐ 48 · Jupyter Notebook · 推送 2025-12-26 · [GitHub](https://github.com/sumedhachugh/Lithography-Hotspot-Detection) · 个人维护

**深度学习检测光刻热点的研究代码：ViT/CNN/ANN 对比**

对应 IEEE 论文的研究实现仓库：针对集成电路设计版图中的光刻热点（易导致开路/短路的难印刷图形），用深度学习替代计算代价高的光刻仿真进行检测，报告在 ICCAD 基准数据集上达到 97.9% 准确率。实现涵盖 Vision Transformer、CNN 与 ANN 并比较结果。代码以 notebook 形式提供，数据集通过 Google Drive 链接给出，含五个子数据集的样本数统计。

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

- ViT / CNN / ANN 三种模型实现并对比结果
- 在 ICCAD 基准数据集上报告 97.9% 检测准确率
- 五个子数据集的训练/测试样本构成均有说明

## 适用场景

- 复现论文中的光刻热点检测实验
- 对比不同网络结构在该任务上的表现
- 获取 ICCAD 光刻热点基准数据集入口

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L10: Lithography simulation is computationally expensive way for hotspot detection so I chose Deep learning based techni
> L12: ### Folder titled 'notebooks' contains code files

## 星数曲线

```mermaid
xychart-beta
    title "sumedhachugh/Lithography-Hotspot-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-27 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f2d6ccc5e80d` · [字段定义](../../DATASET.md)*
