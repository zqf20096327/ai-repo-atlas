# Abineshabee/Sing-Language-Detection

⭐ 44 · Python · 推送 2026-03-08 · [GitHub](https://github.com/Abineshabee/Sing-Language-Detection) · 个人维护

**基于 CNN 与 OpenCV 的 ASL 字母手势实时识别系统**

深度学习项目：用网络摄像头采集自定义数据集，经 HSV 阈值分割提取手部二值掩码，图像缩放至 64x64 后训练 Keras/TensorFlow 实现的卷积神经网络，最终在摄像头视频流中实时识别美国手语 A–Z 字母手势并显示预测结果。流程分三步：capture.py 采集数据（含 HSV trackbar 调节）、cnn_model.py 训练、recognise.py 实时识别。默认数据集规模较小（训练 350 张、测试 50 张），安装仅需 pip 安装 OpenCV/TensorFlow/Keras/NumPy。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HSV 颜色分割提取手部二值掩码，trackbar 可调参数
- CNN 分类 64x64 图像，识别 A–Z 共 26 类字母手势
- 三脚本流程：数据采集→训练→摄像头实时识别

## 适用场景

- 用摄像头实时识别美国手语字母手势
- 作为辅助沟通或无障碍软件的原型
- 学习 OpenCV 预处理与 CNN 图像分类的完整流程

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: A **deep learning based sign language recognition system** that detects **American Sign Language (ASL) alphabet gest
> L7: The model recognizes **hand gestures representing English alphabets (A–Z)** and predicts them in real time using a w

## 星数曲线

```mermaid
xychart-beta
    title "Abineshabee/Sing-Language-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4b28bbcc6217` · [字段定义](../../DATASET.md)*
