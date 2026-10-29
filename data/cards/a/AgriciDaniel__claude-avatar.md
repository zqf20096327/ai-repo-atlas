# AgriciDaniel/claude-avatar

⭐ 31 · HTML · MIT · 推送 2026-04-10 · [GitHub](https://github.com/AgriciDaniel/claude-avatar) · [官网](https://agricidaniel.com) · 个人维护

**连接 Claude Code CLI 的 3D 语音对话数字人，带口型同步**

基于 TalkingHead 的 3D 数字人网页应用：麦克风录音经 faster-whisper (large-v3-turbo, CUDA) 转录，文本送入已认证的 Claude Code CLI 持久会话（stream-json 协议，无 API key），回答经 edge-tts 神经语音合成，利用词级时间戳驱动数字人口型同步。前端为分栏布局：3D 头像+聊天区与 CLI 活动日志。运行需 Claude Code CLI、Python 3.10+、Node.js 18+、ffmpeg 与 NVIDIA GPU，通过 node server.cjs 启动后浏览器打开页面使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- faster-whisper large-v3-turbo 在 CUDA 上做语音转录，模型常驻 VRAM
- Claude Code CLI 持久会话（stream-json，约 5s 响应，无需 API key）
- edge-tts 神经语音 + 词级时间戳驱动 TalkingHead 口型同步
- 常驻 Whisper 转录服务器与一次性转录回退两种模式

## 适用场景

- 在浏览器里与 Claude 进行带 3D 数字人形象的语音对话
- 查看 CLI 活动日志了解对话背后的调用过程
- 作为 TalkingHead 语音对话应用的二次开发起点

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L10: Mic → faster-whisper (GPU) → Claude Code CLI → edge-tts → Avatar lip-sync
> L14: - **Claude** — Persistent `claude` CLI session via `stream-json` protocol (~5s response, no startup overhead)

## 星数曲线

```mermaid
xychart-beta
    title "AgriciDaniel/claude-avatar 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6b2e84267239` · [字段定义](../../DATASET.md)*
