# rohitgit1/Target-Detection-in-MSTAR-Images

⭐ 26 · Python · 推送 2026-09-21 · [GitHub](https://github.com/rohitgit1/Target-Detection-in-MSTAR-Images) · 个人维护

**MSTAR SAR 图像军用车辆目标识别的深度学习套件**

面向 DARPA/AFRL MSTAR 数据集的 SAR 自动目标识别（ATR）Python 套件：实现 A-ConvNet 与 ResNet-18 SAR 深度学习架构，以及 PCA+SVM、随机森林等经典 ML 基线，支持 SOC/EOC 基准评测；内置 Lee/Frost 斑噪滤波、对数动态范围压缩与 Grad-CAM 雷达可解释性热图。提供 Streamlit 战术雷达 Web 控制台（含 3D 后向散射可视化）、mstar-atr 统一 CLI、Python 库导入与 Colab 笔记本，并附带 10 类目标样本切片与合成数据生成器，可离线运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- A-ConvNet（0.38M 参数）在 SOC 基准报告 99.13% 准确率
- Lee/Frost 自适应斑噪滤波与 Grad-CAM 散射中心热图
- Streamlit 交互式 Web 控制台与 mstar-atr 统一 CLI
- 内置 10 类目标样本与合成 SAR 数据生成器，无需手动下载大数据集

## 适用场景

- 在 MSTAR 基准上复现或对比 SAR 目标识别模型
- 对 SAR 图像做单张推理并生成 Grad-CAM 可解释性热图
- 通过 Streamlit 控制台交互式探索雷达回波与滤波效果

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L10: A modernized, production-grade Deep Learning and Computer Vision suite for **Synthetic Aperture Radar (SAR)** Autom
> L12: Features state-of-the-art **A-ConvNet** and **ResNet-18 SAR** architectures, classical ML baselines (PCA + SVM/Rand

## 星数曲线

```mermaid
xychart-beta
    title "rohitgit1/Target-Detection-in-MSTAR-Images 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `05c2f568551b` · [字段定义](../../DATASET.md)*
