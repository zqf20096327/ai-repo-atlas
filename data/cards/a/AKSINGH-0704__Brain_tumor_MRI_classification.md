# AKSINGH-0704/Brain_tumor_MRI_classification

⭐ 16 · Jupyter Notebook · 推送 2026-05-18 · [GitHub](https://github.com/AKSINGH-0704/Brain_tumor_MRI_classification) · 个人维护

**脑瘤 MRI 四分类的 CNN vs ResNet50 对比实验管线**

基于 TensorFlow/Keras 的医学影像分类实验项目：在 Kaggle 脑瘤 MRI 数据集约 7,000 张图像上，对比从零训练的自定义 CNN 基线与 ImageNet 预训练的 ResNet50 迁移学习，输出 4 类（胶质瘤/脑膜瘤/垂体瘤/无肿瘤）softmax 概率。管线含分层划分、训练集限定的数据增强、后置归一化等防泄漏控制，以召回率为主要评估指标，附失败模式分析。README 声明为实验研究项目而非临床工具，ResNet50 结果 91.8% 验证准确率，Meningioma/No Tumor 两类 AUC 接近随机；CNN 结果尚未填入，Grad-CAM 为规划项。通过源码与 Jupyter notebook 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CNN 与 ResNet50 迁移学习的对照实验设计，含逐项 ML 决策依据
- 防数据泄漏控制：分层划分、仅训练集增强、后置归一化
- 以召回率为主要指标并附失败模式与混淆矩阵分析
- 4 类 softmax 概率输出（胶质瘤/脑膜瘤/垂体瘤/无肿瘤）

## 适用场景

- 复现或学习医学影像分类的对比实验管线
- 研究迁移学习在小规模 MRI 数据上的表现与失败模式
- 作为脑瘤 MRI 分类项目的实验代码参考

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L19: *Comparative CNN vs ResNet50 study for multiclass brain tumor detection*
> L43: This project builds a comparative deep learning pipeline to study what two architecturally different models learn f

## 星数曲线

```mermaid
xychart-beta
    title "AKSINGH-0704/Brain_tumor_MRI_classification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `54293720e7cc` · [字段定义](../../DATASET.md)*
