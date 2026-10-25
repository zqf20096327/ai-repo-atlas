# apacha/MusicSymbolClassifier

⭐ 36 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/apacha/MusicSymbolClassifier) · 个人维护

**训练深度神经网络分类手写音乐符号的 Python 训练器**

通用音乐符号分类器的模型训练部分：基于 TensorFlow/Keras 训练深度网络，将手写音乐符号图像分类为多个类别（README 不同位置标注 79 类与 32 类），训练数据来自 HOMUS、MUSCIMA++、Rebelo、printed、Audiveris、fornes、OpenOMR 等数据集，可自动下载 HOMUS。提供 TrainModel.py 及 PowerShell 脚本，支持选择模型配置（如 vgg4、res_net_4）、输入尺寸、minibatch 大小、优化器与类别权重平衡等参数，输出 .h5 模型文件。配套 Android 实时分类应用与 C#/WPF 手工标注工具另在别处。研究发表于 ICDAR 2017 论文。

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

- 训练深度网络将手写音乐符号图像分类为多类别
- 支持 8 种数据集组合训练（homus/rebelo1/rebelo2/printed/audiveris/muscima_pp/fornes/openomr）
- 可配置模型结构、输入尺寸、优化器与类别权重平衡等超参数
- 附 ICDAR 2017 论文与结果对比表格链接

## 适用场景

- 训练手写音乐符号分类模型用于光学乐谱识别（OMR）研究
- 复现论文中的训练配置或调整超参数做对比实验
- 为配套 Android 应用产出 .h5 分类模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository is the model trainer part of the Universal Music Symbol Classifier, which classifies handwritten Mus
> L47: Run `python ModelTrainer/TrainModel.py` or `ModelTrainer/TrainBestModel.ps1` for automatically training a neural ne

## 星数曲线

```mermaid
xychart-beta
    title "apacha/MusicSymbolClassifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0818a7847bb1` · [字段定义](../../DATASET.md)*
