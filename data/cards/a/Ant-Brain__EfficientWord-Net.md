# Ant-Brain/EfficientWord-Net

⭐ 319 · Jupyter Notebook · Apache-2.0 · 推送 2026-02-11 · [GitHub](https://github.com/Ant-Brain/EfficientWord-Net) · [官网](https://ant-brain.github.io/EfficientWord-Net/) · 组织维护

**给开发者的少样本自定义热词检测 Python 引擎**

纯 Python 编写的热词（唤醒词）检测库，基于少样本学习与 FaceNet 启发的孪生网络架构，使用 Google TFLite 做实时推理。开发者录制 4-10 个发音样本即可生成自定义热词的参考嵌入文件，无需额外付费；内置 Mycroft、Google、Alexa 等预置热词，支持单流检测多个热词。提供两种模型（Resnet_50_Arc_loss 与 First_Iteration_Siamese），可在树莓派类设备上运行，但 Resnet 模型（约 88MB）无法在 Arduino 等小型设备上运行；当前模型仅在单词上训练，处理长短语的准确度受限，音频处理窗口为 1 秒/1.5 秒。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4-10 个发音样本即可生成自定义热词参考文件
- TFLite 实时推理，演示验证可在树莓派上运行
- 单音频流同时检测多个热词的计算友好方案
- 内置 Mycroft/Google/Firefox/Alexa 等预置热词嵌入

## 适用场景

- 为家庭助手/IoT 程序添加自定义唤醒词激活
- 在树莓派上做本地实时热词检测
- 为不同指令词分别触发不同程序逻辑

## 场景标签

 · 领域:语音/边缘 AI

## 证据(README 行号)

> L3: Home assistants require special phrases called hotwords to get activated (e.g., "OK Google"). EfficientWord-Net is a
> L5: ### Demo of EfficientWord-Net on Pi

## 星数曲线

```mermaid
xychart-beta
    title "Ant-Brain/EfficientWord-Net 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 318 --> 320
    line [319, 319]
```

2026-10-18 319 → 2026-10-22 319（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9d5c06abf0a0` · [字段定义](../../DATASET.md)*
