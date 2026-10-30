# DivitMittal/Driver-Drowsiness-Detection

⭐ 16 · Jupyter Notebook · MIT · 推送 2026-10-22 · [GitHub](https://github.com/DivitMittal/Driver-Drowsiness-Detection) · [官网](https://deepwiki.com/DivitMittal/Driver-Drowsiness-Detection) · 个人维护

**基于孪生神经网络的实时驾驶员疲劳检测系统**

通过摄像头持续采集驾驶员面部视频帧，结合深度学习与计算机视觉进行实时困倦检测：计算眼睛纵横比（EAR）识别闭眼/微睡眠，监测头部姿态变化（点头、俯仰），分析嘴部形态检测打哈欠。核心采用孪生神经网络架构，通过比较输入对（当前帧与清醒基准帧、睁眼与闭眼）学习相似度度量。技术栈为 Python、TensorFlow/Keras、OpenCV、Dlib、Imutils 等。README 未给出具体安装与运行命令，也未声明系统级依赖或演示链接。

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

- 实时摄像头面部监测与 EAR 眼睛纵横比闭眼分析
- 头部姿态估计与打哈欠检测
- 孪生神经网络比较输入对学习相似度以检测状态变化
- 含 anchor/positive/negative 数据预处理管线与模型架构图示

## 适用场景

- 行车过程中对驾驶员疲劳状态进行实时提醒
- 作为计算机视觉/孪生网络的学习与研究项目
- 扩展到其他需要细微状态变化检测的监控场景

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L14: Driver fatigue represents a significant risk factor in vehicular accidents globally. This project implements a real
> L30: * **Siamese Neural Network Integration:** The core innovation lies in utilizing a Siamese Neural Network architectu

## 星数曲线

```mermaid
xychart-beta
    title "DivitMittal/Driver-Drowsiness-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2e8e2dc74fd0` · [字段定义](../../DATASET.md)*
