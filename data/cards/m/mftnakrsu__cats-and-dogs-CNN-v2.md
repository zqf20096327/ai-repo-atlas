# mftnakrsu/cats-and-dogs-CNN-v2

⭐ 10 · Jupyter Notebook · 推送 2026-11-18 · [GitHub](https://github.com/mftnakrsu/cats-and-dogs-CNN-v2) · 个人维护

**基于 VGG16 预训练模型的猫狗二分类教程项目**

一个图像分类学习项目：数据不足场景下使用在 ImageNet（140 万标注图像、1000 类）上预训练的卷积网络做猫狗二分类。选用 VGG16 作为骨干，通过 keras.applications 加载 imagenet 权重、include_top=False 去掉原 1000 类分类头，替换为自定义二分类头；报告验证准确率约 92%。另含 ConvNet 各层激活可视化的解读：边缘检测器、逐层抽象化与激活稀疏性分析。README 未给出安装与运行说明。

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

- 加载 VGG16 imagenet 权重做猫狗二分类迁移学习
- include_top=False 替换自定义二分类头
- 验证准确率约 92%
- 卷积层激活可视化与逐层特征解读

## 适用场景

- 学习预训练模型迁移学习的基本流程
- 理解卷积网络各层学到的特征表示
- 复现猫狗图像二分类任务

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: One of the most common methods used when our dataset is insufficient is to use pre-trained models.
> L24:  conv_base=VGG16(weights=('imagenet'),

## 星数曲线

```mermaid
xychart-beta
    title "mftnakrsu/cats-and-dogs-CNN-v2 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-19 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `960810ecaf3c` · [字段定义](../../DATASET.md)*
