# Vanguard-s/Electronic-Component-Sorter

⭐ 161 · Python · MIT · 推送 2025-11-17 · [GitHub](https://github.com/Vanguard-s/Electronic-Component-Sorter) · 个人维护

**用摄像头识别电子元件类别的 CNN 分类器（7 类）**

基于 Keras/TensorFlow 的 CNN 模型，通过摄像头采集图像将电子元件分为电阻、电容、LED、晶体管、电位器、二极管、集成电路 7 类；对晶体管、IC 集成 OpenVINO OCR 提取文字，对电容用第二个 CNN 细分 6 种类型。前端为 Flask 网页应用，需 Python 3.11.4、修改源码内多处模型/标签路径后运行 app.py，配合 WinRAR 解压模型压缩包。README 记录了已知问题（偶发误分类、OCR 受厂商 logo 干扰）及电阻色环识别尚未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CNN 将元件分为 7 类的多层分类
- OpenVINO OCR 提取晶体管/IC 文字信息
- 电容细分 CNN（陶瓷/钽/电解/云母/纸/聚酯 6 类）
- Flask 网页界面，摄像头按键采集图像

## 适用场景

- 实验或工作台上快速识别电子元件类别
- 初学者避免用错元件
- 减少人工识别元件的时间和错误

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L55: - Used a trained CNN model to initially classify electronic components into 7 categories: resistors, capacitors, LE
> L64: - Further details about transistors and ICs was obtained by integrating OpenVINO OCR to extract text from images th
> L68: - Integrated the trained model into the Flask web application to create a user-friendly interface, that allows user

## 星数曲线

```mermaid
xychart-beta
    title "Vanguard-s/Electronic-Component-Sorter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 159 --> 162
    line [160, 161, 161]
```

2026-10-18 160 → 2026-10-31 161（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e96a25bca3ad` · [字段定义](../../DATASET.md)*
