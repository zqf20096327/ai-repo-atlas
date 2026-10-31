# SammAsuba/Brain-tumor-classifier

⭐ 14 · Jupyter Notebook · MIT · 推送 2025-12-29 · [GitHub](https://github.com/SammAsuba/Brain-tumor-classifier) · 个人维护

**CNN 对 MRI 脑瘤做四分类的深度学习项目**

基于 TensorFlow/Keras 的卷积神经网络，读取 224×224 灰度 MRI 图像，分类为胶质瘤、脑膜瘤、垂体瘤与非肿瘤四类。仓库含训练脚本与评估可视化 Jupyter 笔记本；数据集不随仓库提供，需自行从 Kaggle 等来源获取并按类别目录组织。模型为 3 个卷积块加全连接层与 dropout，使用 Adam 与分类交叉熵；报告整体测试准确率 88%，训练曲线显示出现过拟合迹象；随机初始化与打乱导致结果存在波动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四分类 CNN：胶质瘤/脑膜瘤/垂体瘤/非肿瘤
- 训练脚本与独立评估可视化笔记本分离
- 报告精确率/召回率/F1 与混淆矩阵等分类指标
- 数据需自备并按 data/Train、data/Test 目录结构组织

## 适用场景

- 复现脑瘤 MRI 四分类的 CNN 基线实验
- 学习医学影像分类项目的训练与评估流程
- 在自备 MRI 数据集上对比模型表现

## 场景标签

 · 领域:医学影像/深度学习

## 证据(README 行号)

> L3: This project presents a Convolutional Neural Network (CNN)-based approach for brain tumor classification from MRI sc
> L64: The trained CNN achieves an overall test accuracy of **88%**.

## 星数曲线

```mermaid
xychart-beta
    title "SammAsuba/Brain-tumor-classifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c2c2bb1e0735` · [字段定义](../../DATASET.md)*
