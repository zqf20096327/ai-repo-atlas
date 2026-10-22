# eadmin2/jarvis_ai

⭐ 194 · Python · MIT · 推送 2026-06-13 · [GitHub](https://github.com/eadmin2/jarvis_ai) · 个人维护

**自托管的钢铁侠风格语音助手与全息 HUD，接入 Hermes Agent**

构建在 NousResearch 开源 Hermes Agent 之上的语音交互前端：本地 Whisper（CPU，可选局域网 NVIDIA 机器上的 large-v3-turbo 侧车）做实时语音转写，转写文本交给具备持久记忆、终端访问、网页搜索与 80+ 技能的 Hermes Agent 执行，回复经 ElevenLabs 云端 TTS 逐句流式播报（含云端前隐私脱敏）。浏览器 HUD 提供工具调用预览、危险命令审批卡、媒体面板、用量与主机 CPU/GPU 监控。服务器端为 Python FastAPI，测试环境为 macOS/Apple Silicon，需自装 Hermes Agent、Python 3.11+ 与 ElevenLabs API key，仅限局域网使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 Whisper STT，可选 LAN 内 NVIDIA 侧车加速至 large-v3-turbo 并自动回退
- 语音与打字聊天共享同一持久 Hermes 会话，记忆跨重启保留
- 危险命令审批卡、STOP 中断与打断感知的 barge-in
- 密钥不出浏览器（allowlist 代理）、TTS 前秘密字符串脱敏、LAN-only 设计

## 适用场景

- 在家里局域网用自己的硬件跑一个语音操控的 AI 助手
- 通过语音让 agent 执行文件读写、跑命令、搜网页等任务
- 在浏览器或手机主屏上以 HUD 界面监控 agent 行为并审批危险操作

## 场景标签

 · 领域:AI 应用/语音交互

## 证据(README 行号)

> L3: A self-hosted, Iron-Man-style voice assistant and command center built on top of
> L9: **Everything runs on your own hardware.** The only cloud calls are your LLM
> L21: Click the ring and speak. Your words transcribe **live on screen** while you

## 星数曲线

```mermaid
xychart-beta
    title "eadmin2/jarvis_ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 189 --> 195
    line [190, 193, 194]
```

2026-10-18 190 → 2026-10-22 194（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `924579af5f79` · [字段定义](../../DATASET.md)*
