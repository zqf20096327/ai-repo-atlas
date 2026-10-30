# hwdsl2/scribecrate-live

⭐ 38 · Shell · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/hwdsl2/scribecrate-live) · [官网](https://scribecrate.live) · 个人维护 · 中文 README

**自托管实时语音转文字服务器，WebSocket 流式转写 + OpenAI 兼容 API**

基于 WhisperLive 与 faster-whisper 的自托管语音转文字 Docker 服务器：通过 WebSocket 端口接收 16kHz PCM 音频流，实时返回渐进式转写分段；另提供 OpenAI 兼容的 /v1/audio/transcriptions REST 端点处理音频文件，可被 OpenAI SDK 直接调用。支持全部 Whisper 模型、VAD 静音跳过、离线模式（预缓存模型）与 API-key 认证。可运行于 CPU（amd64/arm64）或 NVIDIA GPU（:cuda 镜像，仅 linux/amd64），基础镜像约 750MB，默认 base 模型需约 700MB 空闲内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WebSocket 流式实时转写（麦克风/音频流，渐进分段更新）
- OpenAI 兼容 REST API，可直接对接 OpenAI SDK 与应用
- 支持全部 Whisper 模型与 VAD 静音跳过
- 离线模式（WHISPERLIVE_LOCAL_ONLY）与 CPU/NVIDIA GPU 双镜像

## 适用场景

- 在我的服务器上私有化部署实时字幕或直播转写
- 用 OpenAI SDK 把音频文件转成文字而不调用第三方服务
- 内网/离线环境运行语音转文字服务

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L9: ScribeCrate Live is a self-hosted real-time speech-to-text server powered by WhisperLive and faster-whisper. It prov
> L15: - **Real-time WebSocket transcription:** transcribe live microphone audio or audio streams with progressive segment

## 星数曲线

```mermaid
xychart-beta
    title "hwdsl2/scribecrate-live 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-30 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `56fc4f20f704` · [字段定义](../../DATASET.md)*
