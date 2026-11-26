# lancejames221b/openjarvis

⭐ 10 · JavaScript · MIT · 推送 2026-07-06 · [GitHub](https://github.com/lancejames221b/openjarvis) · 个人维护

**自托管 Discord 语音/文本 AI 助手，语音接入 Claude 代理**

基于官方 Claude Code CLI 的 Discord 语音机器人：用户在语音频道说话，经 Whisper 转录后通过 `claude -p` 路由到 OpenClaw 网关代理，再以 TTS 回答。提供三档功能配置（REACTOR/FRIDAY/JARVIS），内置声纹认证、唤醒词、自我静音队列、模糊唤醒词匹配等机制，支持 5 种 TTS 引擎（Piper/Edge/Kokoro/Chatterbox/Qwen3）按硬件选择。依赖 Discord bot token 与 Claude CLI 登录，提供 systemd/systemctl 启动方式与 Docker 开发模式（mock TTS/STT，无需 GPU）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 种 TTS 引擎可选，覆盖 CPU/云免费/GPU 场景
- 三段式说话人验证流水线（VAD+声纹），附加延迟约 50ms
- 自我静音时任务继续执行、TTS 输出排队，解除静音后汇总简报
- 模糊唤醒词：按呼格模式匹配 Whisper 误听词，需声纹验证

## 适用场景

- 在 Discord 语音频道用对话方式查询日程、邮件并执行任务
- 蓝队运维中语音查询威胁情报、IOC 与 SIEM
- 蓝牙耳机免提运行个人助理，含晨间简报与媒体控制

## 场景标签

`AI 助手` `语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L9: **A Discord voice bot backed by the official Claude Code CLI.** Speak in a Discord voice channel — Jarvis hears you,
> L15: Not a chatbot. Not a voice assistant that sets timers. A full AI system with access to your calendar, email, code, 
> L155: **Key design principle:** The voice bot does not duplicate agent capabilities. Every voice request is forwarded to


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `988c1efea5ee` · [字段定义](../../DATASET.md)*
