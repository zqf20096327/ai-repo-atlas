# CamoLover/AssaultronProject

⭐ 15 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/CamoLover/AssaultronProject) · [官网](https://camolover.dev/APP/ASR-7/) · 个人维护

**具身 AI 智能体：带人格、视觉语音感知与自主行为的机器人项目**

以《辐射》Assaultron 为原型的具身 AI agent，采用分层认知-行为-身体架构：LLM 驱动意图推理（Ollama 本地/Gemini/OpenRouter 三选一），配情绪与人格系统、核心/情景记忆；行为层用效用仲裁选择行为（威慑、巡逻等），虚拟身体管理姿态与手势，可选经 ESP32/Arduino 控制舵机与 LED 实现实体化。感知层含 TensorFlow Lite 目标检测、MediaPipe 人脸跟踪、openWakeWord 唤醒词、Mistral Voxtral 语音识别、xVASynth 语音合成。以 Python/Flask 提供 Web 界面，附 Discord bot 与邮件/GitHub 工具集成。硬件实体化为可选，纯软件即可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ollama/Gemini/OpenRouter 多 LLM 后端
- 效用仲裁的行为选择与人格情绪系统
- 视觉/语音多模态感知（目标检测、人脸跟踪、唤醒词、STT/TTS）
- 可选 ESP32/Arduino 舵机与 LED 实体化

## 适用场景

- 搭建有性格的桌面具身 AI 伴侣，语音对话并观察情绪姿态
- 把虚拟身体映射到 ESP32/Arduino 舵机实现实体机器人
- 通过 Web 面板或 Discord 远程交互并监控认知状态

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L25: - 🧠 **Think** with intention-based reasoning using LLMs (Ollama, Gemini, or OpenRouter)
> L30: - 🎯 **Act** autonomously through behavior selection and utility-based decision-making
> L59: - **Vision System**: Real-time object detection using TensorFlow Lite

## 星数曲线

```mermaid
xychart-beta
    title "CamoLover/AssaultronProject 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `fa2b584b282a` · [字段定义](../../DATASET.md)*
