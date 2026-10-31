# Jen-Hung-Ho/ros2_jetbot_voice

⭐ 15 · Python · 推送 2026-04-07 · [GitHub](https://github.com/Jen-Hung-Ho/ros2_jetbot_voice) · 个人维护

**ROS2 Jetbot 语音控制节点集：语音识别驱动机器人动作**

一组面向 NVIDIA Jetson Orin Jetbot 的 ROS2 节点：通过 NVIDIA RIVA ASR 服务客户端将人声解码为文本，再由 1D CNN 文本分类模型判定意图（聊天、视觉或机器人指令），经 RIVA TTS 将回复转为语音播放；配合 LLM 聊天、VLM 视觉、Lidar 辅助避障自驾、实时目标检测跟随行人等动作执行。需在 Docker 容器内运行，依赖 RIVA 服务器与 NanoLLM 容器，硬件要求 Jetson Orin Nano/NX。

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

- RIVA ASR 客户端节点将语音解码为 ROS2 文本消息
- 1D CNN 文本分类模型预测语音意图并映射动作
- RIVA TTS 将聊天/视觉回复转为语音输出
- 支持自驾避障、行人跟随、导航等机器人动作

## 适用场景

- 用语音命令控制 Jetbot 执行自驾、跟随、导航等动作
- 为机器人搭建语音对话与视觉问答交互
- 在 Jetson Orin 平台上构建语音驱动机器人原型

## 场景标签

`语音识别` `语音合成` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: Jetbot Voice-Activated Copilot is a set of ROS2 nodes that utilize the NVIDIA RIVA Automatic Speech Recognition (ASR
> L22:  - Employs the Nvidia RIVA Speech Recognition (ASR) service client side ROS2 node to decode human speech into text.
> L57:  - **Voice to Action Mapping:** Upon initialization, the Jetbot ASR Agent lazily loads a simple pre-trained 1D conv

## 星数曲线

```mermaid
xychart-beta
    title "Jen-Hung-Ho/ros2_jetbot_voice 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `de85275ca1cb` · [字段定义](../../DATASET.md)*
