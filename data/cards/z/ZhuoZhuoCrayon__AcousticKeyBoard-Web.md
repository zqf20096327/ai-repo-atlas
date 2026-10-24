# ZhuoZhuoCrayon/AcousticKeyBoard-Web

⭐ 88 · Python · MIT · 推送 2026-04-03 · [GitHub](https://github.com/ZhuoZhuoCrayon/AcousticKeyBoard-Web) · 个人维护 · 中文 README

**基于声学信号与深度学习的键盘敲击键位识别学习项目**

通过麦克风采集键盘敲击声，识别被敲击键位的系统：处理流程为 VAD 有效信号提取、中值滤波降噪、MFCC 特征提取，再以 TensorFlow 搭建 LSTM/BLSTM 模型训练预测。以 Django Web 后端形式提供（需配置环境变量与 MySQL 数据库后 migrate 运行），另有安卓端独立仓库。作者自述为学习性质项目，指出泛化到不同敲击习惯的难度较大。

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

- VAD + 中值滤波降噪 + MFCC 特征提取的信号处理流程
- TensorFlow 搭建 LSTM/BLSTM 模型进行键位预测
- Django Web 后端与独立安卓端仓库

## 适用场景

- 学习信号处理与深度学习在声学识别中的应用
- 复现键盘敲击键位识别实验
- 了解 Django 部署深度学习模型的工程方式

## 场景标签

 · 领域:声学信号处理/深度学习

## 证据(README 行号)

> L5:  基于声学信号处理及深度学习的键盘敲击识别系统。
> L42: 基于 Tensorflow 搭建 LSTM 模型，在堆层数不多的情况已经达到比较好的效果。

## 星数曲线

```mermaid
xychart-beta
    title "ZhuoZhuoCrayon/AcousticKeyBoard-Web 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 86 --> 89
    line [87, 88, 88]
```

2026-10-18 87 → 2026-10-24 88（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ea503ceb83b4` · [字段定义](../../DATASET.md)*
