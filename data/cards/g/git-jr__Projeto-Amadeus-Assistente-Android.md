# git-jr/Projeto-Amadeus-Assistente-Android

⭐ 19 · Kotlin · MIT · 推送 2026-10-12 · [GitHub](https://github.com/git-jr/Projeto-Amadeus-Assistente-Android) · 个人维护

**Android 虚拟助手 App：文本/语音对话与代理操作其他应用**

面向 Android 手机用户的虚拟助手应用（葡萄牙语，源自 YouTube 视频系列项目）：支持文本与语音对话、可由用户教授和编辑回答、离线唤醒词"Amadeus"（Vosk）、可设为系统默认助手。代理模式通过无障碍服务读取屏幕并在其他应用中执行点击、输入、滚动等操作，可录制宏作为任务示例。AI 提供方可选 OpenAI（依赖仓库外 Cloud Function）、Google Gemini 或设备端 LiteRT-LM 本地模型（如 Gemma 3 1B）。技术栈为 Kotlin/Java + Firebase，需自行配置 Firebase 项目并用 Gradle 编译，已上架 Google Play。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本/语音对话，回答可由用户教授与编辑
- Vosk 离线识别唤醒词"Amadeus"
- 代理模式经无障碍服务在其他应用中执行操作并录制宏
- AI 提供方可在 OpenAI、Gemini 与 LiteRT-LM 本地模型间选择

## 适用场景

- 用语音或文字与手机助手对话
- 通过自然语言指令让助手在其他应用中代为操作
- 把常用操作录成宏复用

## 场景标签

`聊天机器人` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Amadeus é um assistente virtual para celulares Android. Ele conversa por texto
> L33: - Permite escolher a IA usada: OpenAI (via Cloud Function), Google Gemini (via

## 星数曲线

```mermaid
xychart-beta
    title "git-jr/Projeto-Amadeus-Assistente-Android 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `84675f155c1f` · [字段定义](../../DATASET.md)*
