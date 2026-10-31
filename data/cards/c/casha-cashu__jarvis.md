# casha-cashu/jarvis

⭐ 14 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/casha-cashu/jarvis) · [官网](https://casha-cashu.github.io/jarvis/) · 个人维护

**Linux/macOS 本地语音 AI 助手：唤醒词+LLM+bash 代理**

面向终端用户的桌面语音助手：Vosk/faster-whisper 离线语音识别，Piper TTS 俄语语音合成，唤醒词“джарвис”触发。接入 Ollama（本地）、OpenAI、Anthropic、OpenRouter 作为 LLM，通过原生 tool-calling 执行 bash/read/write 操作，设有三层审批门（硬封禁清单→危险模式检测→auto/strict/yolo 审批）。支持多模态屏幕分析、Telegram 机器人入口与 Tauri+React 桌面 GUI。提供 deb 安装包与源码安装两种方式，自动识别 Hyprland/KDE/GNOME/i3/Sway/macOS 等桌面环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Vosk/faster-whisper 语音识别 + Piper TTS 合成的本地语音管线
- 三层审批门的 bash/read/write 工具代理（blocklist→危险模式检测→approval gate）
- 多 LLM 提供商支持：Ollama/OpenAI/Anthropic/OpenRouter，原生 tool-use
- Tauri 2 + React 19 桌面 GUI 与 Telegram 机器人入口

## 适用场景

- 用语音控制 Linux/macOS 桌面：切换工作区、开应用、调音量
- 让本地 LLM 代理通过 bash 工具自动执行系统任务
- 通过 Telegram 远程使用同一助手
- 语音听写文本到任意输入框

## 场景标签

`AI 助手` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L11: Голосовой ИИ-ассистент для Linux и macOS. Распознаёт речь (Vosk / Whisper), выполняет системные команды, отвечает ч
> L17: - **LLM интеграция** — Ollama (локально, с tool-use), OpenAI (нативный API, с tool-use), Anthropic Claude (нативный
> L21: - **Bash-агент** — LLM (Ollama, OpenAI, Anthropic) вызывает bash/read/write tools через нативный tool-calling API. 

## 星数曲线

```mermaid
xychart-beta
    title "casha-cashu/jarvis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `35539fb96e87` · [字段定义](../../DATASET.md)*
