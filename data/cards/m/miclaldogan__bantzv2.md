# miclaldogan/bantzv2

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/miclaldogan/bantzv2) · 个人维护

**Linux 本地优先的个人 AI 管家：语音、记忆、定时任务、桌面控制**

运行于 Linux 的本地优先 AI 助手，以 1920s 英式管家人设与用户对话。核心机制：单一 LLM Lane 序列化所有本地推理（对话模型保温 30 分钟），大脑可把任务委派给 researcher/developer/reviewer 三个子代理（默认 gemma3:4b 小模型）。提供 Tauri+React 桌面端 Operations Center 与 CLI 两套界面。功能含持久记忆（ChromaDB+SQLite 知识图谱）、端到端本地语音（Porcupine 唤醒词/faster-whisper STT/Piper TTS）、APScheduler 定时任务、pyautogui 桌面控制、Gmail/日历/Telegram 集成。默认全本地，唤醒词需 Picovoice 免费 access key。README 声明仍处早期开发，部分功能（RL、主动干预）未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM Lane 单通道序列化本地推理，交互聊天优先
- 三角色子代理系统（researcher/developer/reviewer）按角色配置小模型
- MemPalace 持久记忆：ChromaDB 向量库 + SQLite 知识图谱混合召回
- 端到端本地语音链路：唤醒词→VAD→faster-whisper STT→Piper TTS

## 适用场景

- 在 Linux 桌面上通过语音或对话让 AI 助手代查邮件、管日程、做研究
- 夜间自动跑维护、邮件轮询并在早晨生成简报
- 通过 Telegram 远程访问家用电脑并执行任务

## 场景标签

`AI 助手` `语音 Agent` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Bantz is a local-first AI assistant that runs on your Linux machine and acts as a personal butler — it has a voice, 
> L129: - Three roles today (researcher / developer / reviewer, with aliases), each on its own small local model via `BANT

## 星数曲线

```mermaid
xychart-beta
    title "miclaldogan/bantzv2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `f08353ff3e68` · [字段定义](../../DATASET.md)*
