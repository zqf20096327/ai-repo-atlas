# MahdiKordian/DigitVision

⭐ 4 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/MahdiKordian/DigitVision) · [官网](https://digitvision-app.streamlit.app/) · 个人维护

**识别手写数字的 Streamlit Web 应用**

一个手写数字识别 Web 应用：上传或拍摄照片，经 CNN 输出预测数字与置信度。预处理流水线用 HSV 色彩掩膜提取红墨水，含 Otsu 阈值回退，再按 MNIST 方式裁剪、缩放至 20px、补边至 28×28 并按质心居中。界面显示 top-3 预测、概率图、预处理过程可视化与最近 10 次预测记录。仓库内置已训练模型，Streamlit 直接运行；提供 train.py 可复现训练。限制：每次仅识别单个数字。

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

- CNN 在 MNIST 测试集上的准确率为 99.32%
- HSV 色彩掩膜 + Otsu 阈值回退的数字分割流水线
- 展示检测框、二值掩膜与 28×28 模型输入的预处理可视化
- 仓库内置已训练模型，无需重训即可运行

## 适用场景

- 拍摄或上传手写数字照片获取识别结果
- 查看图像预处理各步骤的中间结果
- 复现 MNIST 模型训练流程

## 场景标签

`模型训练` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: **Handwritten digit recognition, powered by deep learning.**
> L24: MNIST models usually stop at a notebook: great accuracy on clean 28×28 test images, and no idea what happens with a

## 星数曲线

```mermaid
xychart-beta
    title "MahdiKordian/DigitVision 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-26 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `009ce9856752` · [字段定义](../../DATASET.md)*
