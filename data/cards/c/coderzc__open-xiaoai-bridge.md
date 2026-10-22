# coderzc/open-xiaoai-bridge

⭐ 417 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/coderzc/open-xiaoai-bridge) · 个人维护 · 中文 README

**将小爱音箱桥接到外部 AI 服务（OpenClaw、小智等）的网关**

服务端桥接器，把刷机后的小爱音箱接入 OpenClaw、QwenPaw、小智 AI 及 OpenAI 兼容服务（含 Ollama、LM Studio 等 /v1/chat/completions 后端）。机制上通过自定义唤醒词路由到不同后端与 Agent Session，支持连续对话（本地 VAD+SherpaASR 或接管小爱原生 ASR）、多 Agent 动态切换、多种 TTS provider（小爱原生/豆包/OpenAI/MLX-Audio），并提供 HTTP API 远程控制播放与唤醒。仅含服务端，需先在音箱上刷机安装 Rust Client。Docker Compose 为推荐部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个音箱经自定义唤醒词路由到多种 AI 后端与 Agent Session
- 连续对话支持 local_asr（VAD+SherpaASR）与接管小爱原生 ASR 两种模式
- HTTP API（默认 9092）远程播放文字/音频、TTS、唤醒与打断
- 四种 TTS provider：小爱原生、豆包、OpenAI 兼容、MLX-Audio

## 适用场景

- 让小爱音箱改用自选的 AI Agent 作为语音助手
- 同一台音箱用不同唤醒词唤起多个隔离的 AI 人格
- 通过 HTTP API 从外部程序向音箱推送 TTS 播报或控制播放

## 场景标签

`语音 Agent` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: **小爱音箱与外部 AI 服务（小智 AI、OpenClaw、OpenAI 兼容服务、QwenPaw）的桥接器**
> L21: |🔌 **OpenAI 兼容服务**|接入 Hermes Agent API Server、OpenAI、Ollama、LM Studio 等 `/v1/chat/completions` 服务|
> L34: > **⚠️ 本项目仅包含服务端**，需要先在小爱音箱上安装 Client 端。

## 星数曲线

```mermaid
xychart-beta
    title "coderzc/open-xiaoai-bridge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 411 --> 418
    line [412, 415, 417]
```

2026-10-18 412 → 2026-10-22 417（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `d5c4fa3aca2d` · [字段定义](../../DATASET.md)*
