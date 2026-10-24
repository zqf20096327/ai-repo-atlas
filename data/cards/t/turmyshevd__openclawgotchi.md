# turmyshevd/openclawgotchi

⭐ 52 · Python · MIT · 推送 2026-06-15 · [GitHub](https://github.com/turmyshevd/openclawgotchi) · [官网](https://openclawgotchi.github.io/openclawgotchi/) · 个人维护

**运行在树莓派上的电子墨水屏 AI 宠物/agent，经 Telegram 对话**

部署在 Raspberry Pi Zero 2W（512MB 内存）上的 agentic 机器人：通过 Telegram（可选 Discord）对话交互，在 Waveshare 2.13 寸墨水屏上以 Kaomoji 表情显示 25+ 种情绪。具备语义记忆、Obsidian 兼容知识库、XP 升级系统、每 4 小时的心跳自检、定时任务与自修改代码能力。双模式运行：标准模式经 LiteLLM 调用 GLM/Gemini 等模型（支持 Whisper 语音转录与 Vision 图像分析），Pro 模式使用 Claude Code CLI。裸机运行无沙箱，靠 ALLOWED_USERS 白名单控制访问。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LiteLLM 标准模式 + Claude Code CLI Pro 模式双状态运行
- E-Ink 屏幕渲染 25+ 种 Kaomoji 情绪与 XP 等级显示
- 语义记忆 + Obsidian 兼容知识库（含 dreaming 巡检）
- 内置 coding/system/weather/obsidian-pro 等 8 项技能与 Lite 模式工具集

## 适用场景

- 在树莓派上养一个可通过 Telegram 对话的 AI 陪伴机器人
- 用自然语言让 agent 管理定时任务、记忆与笔记库
- 低成本硬件（约 $50 套件）体验边缘端 agentic AI

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L24: * **Agentic Core**: I am not just a chatbot. I am an OpenClaw instance optimized for the edge. You give me a task, 
> L73: * **Standard Mode (Efficient)**: Using LiteLLM (**GLM-5.1**, Gemini, etc.). I am fast, can code, use bash, tools, g
> L116: - **Telegram**: required. This is the primary control path and the setup wizard assumes you have a Telegram bot to

## 星数曲线

```mermaid
xychart-beta
    title "turmyshevd/openclawgotchi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-24 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `534113b5e5dc` · [字段定义](../../DATASET.md)*
