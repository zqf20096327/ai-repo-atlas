# rprabhat/chart-digitizer

⭐ 18 · Python · Apache-2.0 · 推送 2026-04-03 · [GitHub](https://github.com/rprabhat/chart-digitizer) · 个人维护

**从图表图像提取数据点的机器学习工具（Jupyter Notebook）**

以 Jupyter Notebook 形式提供的图表数字化工具：针对柱状图、折线图和散点图图像，使用 CNN 目标检测识别数据点，并用 OpenCV 与 Tesseract OCR 检测图例和坐标轴，提取数值数据。仓库内含随机图表生成器（用于生成训练数据）、CNN 模型训练与数据提取流程。运行需 Python 3.x、Jupyter、OpenCV、Tesseract OCR 与 TensorFlow/PyTorch。采用 Apache 2.0 许可，参考文献列出 ChartSense、WebPlotDigitizer、Engauge Digitizer。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CNN 目标检测识别柱状图/折线图/散点图的数据点
- OpenCV 与 Tesseract OCR 用于图例与坐标轴检测
- 内置随机图表生成器用于训练数据

## 适用场景

- 从论文或报告的图表图像中提取原始数值数据
- 批量将柱状图/折线图/散点图转换为数据点

## 场景标签

`目标检测` `OCR` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L10: Chart Digitizer extracts numerical data from chart images (bar charts, line charts, scatter plots) using:
> L11: - **Machine Learning** - CNN-based object detection for accurate data point identification

## 星数曲线

```mermaid
xychart-beta
    title "rprabhat/chart-digitizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2acd6007e67c` · [字段定义](../../DATASET.md)*
