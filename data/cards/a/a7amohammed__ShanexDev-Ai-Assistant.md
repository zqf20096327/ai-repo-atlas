# a7amohammed/ShanexDev-Ai-Assistant

⭐ 3 · Python · 推送 2026-11-09 · [GitHub](https://github.com/a7amohammed/ShanexDev-Ai-Assistant) · [官网](https://shanexdev.odoo.com) · 个人维护

**语音优先 CLI AI 助手：唤醒词对话、屏幕控制与系统自动化**

以 Python 运行的语音优先命令行 AI 助手：通过唤醒词从待机进入交互，语音识别用离线流式 Moonshine，语音合成以 edge-tts 为主、gTTS+pygame 兜底；AI 回答由 Ollama 本地模型（可配 Ollama Cloud）生成，对话历史持久化为 JSON。提供屏幕读取（Tesseract OCR）、鼠标键盘自动化与 shell 命令执行。人格与长期记忆通过手编 JSON 配置文件定义，可调 prompt 预算以适配小型本地模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 离线流式 Moonshine 语音识别与唤醒词控制，说话时自动静音麦克风
- Ollama 本地/云端模型接入与持久化对话记忆
- Tesseract OCR 屏幕读取与鼠标/键盘/shell 命令自动化
- 人格与事实经 JSON 配置文件定义，无需改代码

## 适用场景

- 用语音在电脑上执行命令与打开网页
- 让助手读取并朗读屏幕上的文本
- 在本地模型下搭建可自定义人格的桌面语音助手

## 场景标签

`AI 助手` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: A voice-first CLI AI assistant. Say **"wake up"** and it answers **"Wake up"**.
> L56: - Ollama (local, or Ollama Cloud with `OLLAMA_HOST=https://ollama.com` + `OLLAMA_API_KEY`)

## 星数曲线

```mermaid
xychart-beta
    title "a7amohammed/ShanexDev-Ai-Assistant 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-29 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `810ccb7658f8` · [字段定义](../../DATASET.md)*
