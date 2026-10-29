# Praveenkottari/BD3-Dataset

⭐ 39 · Jupyter Notebook · 推送 2026-10-25 · [GitHub](https://github.com/Praveenkottari/BD3-Dataset) · 组织维护

**建筑缺陷检测数据集：3,965 张标注 RGB 图像供计算机视觉评测**

BD3 是面向自动建筑巡检的公开图像数据集：原始子集含 3,965 张标注 RGB 图像，覆盖藻斑、大小裂缝、剥落、脱落、污渍六类结构缺陷及正常墙面；另含 14,000 张经几何变换与颜色调整生成的增强子集。图像来自 50 余栋 10-60 年楼龄建筑的室内外墙面，采集距离约 1 米。README 给出五种 torchvision 预训练分类器（ViT、VGG16、ResNet18、AlexNet、MobileNetV2）在 60/20/20 划分下的基准结果与 ViT 混淆矩阵，并附预处理、增强、划分、训练与结果分析代码目录。

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

- 3,965 张标注 RGB 图像，覆盖 6 类结构缺陷与正常墙面
- 14,000 张几何/颜色变换增强图像子集
- 五种 torchvision 预训练分类器的基准评测结果
- 附预处理、增强、划分、训练与结果分析 Python 代码

## 适用场景

- 训练和评测建筑缺陷自动识别模型
- 对比不同深度学习分类器在结构缺陷数据上的表现
- 研究数据增强对缺陷检测模型泛化的影响

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L7: To address this gap, we present **BD3: Building Defects Detection Dataset**, specifically designed to evaluate and d
> L10: - **Original dataset**: 3,965 RGB images annotated to cover six common structural defects, along with normal wall i

## 星数曲线

```mermaid
xychart-beta
    title "Praveenkottari/BD3-Dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-29 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8ebf279a2072` · [字段定义](../../DATASET.md)*
