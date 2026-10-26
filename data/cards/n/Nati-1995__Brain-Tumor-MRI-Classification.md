# Nati-1995/Brain-Tumor-MRI-Classification

⭐ 44 · Jupyter Notebook · 推送 2026-08-16 · [GitHub](https://github.com/Nati-1995/Brain-Tumor-MRI-Classification) · [官网](https://nati-1995.github.io/Brain-Tumor-MRI-Classification/) · 个人维护

**脑肿瘤 MRI 分类项目：检测与四分类，含 Grad-CAM 可解释性**

基于 EfficientNetB0 迁移学习的脑肿瘤 MRI 图像分类研究项目，覆盖肿瘤/无肿瘤二分类（准确率 99.4%）与胶质瘤/脑膜瘤/垂体瘤/无肿瘤四分类（94.75%）两个任务。采用两阶段训练（冻结骨干训练头部后解冻上层微调）、平方根阻尼类权重处理类别不平衡，并用 Grad-CAM 热力图验证模型关注肿瘤区域。提供 Gradio 交互界面，在 Google Colab 上以 notebook 形式运行。README 明确声明为研究与教育项目，非医疗器械，不得用于实际诊断；仅在单一公开数据集上训练，未做跨数据集泛化与临床验证。

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

- EfficientNetB0 迁移学习，二分类准确率 99.4%、四分类 94.75%（3 种子平均）
- Grad-CAM 可解释性：热力图定位肿瘤区域并解释误分类
- 两阶段训练策略与平方根阻尼类权重处理类别不平衡
- Gradio 交互界面同时运行双模型并展示结果解读

## 适用场景

- 学习迁移学习与医学图像分类的完整训练流程
- 复现脑肿瘤 MRI 分类实验并查看 Grad-CAM 可解释性分析
- 作为医学影像深度学习教育项目的参考实现

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Deep-learning classification of brain MRI scans using transfer learning, with
> L13: An interactive interface (Gradio) runs both models on an uploaded scan, shows a

## 星数曲线

```mermaid
xychart-beta
    title "Nati-1995/Brain-Tumor-MRI-Classification 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-26 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ab6e9533fd10` · [字段定义](../../DATASET.md)*
