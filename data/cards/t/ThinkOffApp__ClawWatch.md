# ThinkOffApp/ClawWatch

⭐ 69 · Kotlin · NOASSERTION · 推送 2026-09-12 · [GitHub](https://github.com/ThinkOffApp/ClawWatch) · [官网](https://thinkoff.io) · 组织维护

**在 Galaxy Watch 上原生运行的离线语音 AI 助手**

面向 Wear OS（推荐 Galaxy Watch 7 及以上）的语音智能体应用：内置 Vosk 离线语音识别、NullClaw（2.8 MB Zig 静态二进制）作为 agent 运行时、Android TTS 输出，LLM 调用走云端（默认 Anthropic Claude Opus 5，支持 22+ 提供商含 OpenAI/Gemini/Ollama）。部分命令（计时器、心率、体征）由本地路由直接在手表上执行。带情绪驱动动画的虚拟形象、Agent Kit 房间连接、手表传感器实时上下文，以及通过 ADB 配置的 Mac 端管理面板。需 Mac/Linux 从源码编译 NullClaw 与 APK 后经 ADB 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Vosk 离线 STT + Android TTS，LLM 之外全部在手表端运行
- NullClaw 静态二进制（2.8 MB，约 1 MB RAM）作为 agent 运行时，支持 22+ LLM 提供商
- 本地路由直接执行计时器、心率、体征等手表原生动作
- 六种情绪状态的虚拟形象动画与语速/音调联动

## 适用场景

- 在手表上说句话向 AI 助手提问并听语音回答
- 通过语音查看心率、体征或设置计时器
- 让 agent 连接 GroupMind 房间并播报家人动态

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L5: A voice-controlled smartwatch agent for Wear OS: an on-device LLM assistant living on your Galaxy Watch, with offlin
> L44: [tap mic] → Vosk STT (on-device, offline) → local command/router → NullClaw-first query path via Wear OS curl bridg

## 星数曲线

```mermaid
xychart-beta
    title "ThinkOffApp/ClawWatch 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 67 --> 70
    line [68, 69, 69]
```

2026-10-18 68 → 2026-10-26 69（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `01a45a4288ae` · [字段定义](../../DATASET.md)*
