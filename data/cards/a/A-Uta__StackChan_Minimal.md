# A-Uta/StackChan_Minimal

⭐ 24 · C++ · Apache-2.0 · 推送 2026-06-15 · [GitHub](https://github.com/A-Uta/StackChan_Minimal) · 个人维护

**M5Stack AtomS3R 小型 AI 陪伴机器人固件，接本地 STT/LLM/TTS**

运行在 M5Stack AtomS3R（ESP32-S3）上的小型 AI 陪伴机器人固件，面向演示、学习与 Maker 活动。固件本体不含任何 AI 模型或服务二进制，需另建本地服务：whisper.cpp 做语音识别、llama.cpp/LM Studio/Ollama 通过 OpenAI 兼容 API 提供对话、piper-plus 做语音合成，可选接 VOICEVOX 适配器。另含 Wi-Fi 配置门户、MAX30100 心率/SpO2 参考值演示（声明非医疗设备、数值未校准）与可选舵机动作。提供 Apache-2.0 许可与 BOOTH 入门 PDF。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 OpenAI 兼容 API 接入 llama.cpp / LM Studio / Ollama 本地 LLM 对话
- whisper.cpp 本地语音识别与 piper-plus 外部 TTS 服务器合成
- MAX30100 心率/SpO2 参考值演示（明确非医疗用途、未校准）
- 固件不含任何模型或服务二进制，需自行部署本地 AI 服务

## 适用场景

- Maker 组装一台接本地 AI 服务的桌面陪伴机器人
- 学习 ESP32 固件与本地 STT/LLM/TTS 服务的集成方式
- 演示活动中展示全本地化语音对话流程

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: StackChan Minimal is a small AI companion robot project for M5Stack AtomS3R.
> L5: It connects an ESP32-based body to local AI services such as speech recognition, local LLMs, and text-to-speech serv

## 星数曲线

```mermaid
xychart-beta
    title "A-Uta/StackChan_Minimal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `159b9950426b` · [字段定义](../../DATASET.md)*
