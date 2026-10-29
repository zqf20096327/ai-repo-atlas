# ErcinDedeoglu/WhisperDock

⭐ 31 · C++ · CC0-1.0 · 推送 2026-10-20 · [GitHub](https://github.com/ErcinDedeoglu/WhisperDock) · [官网](https://hub.docker.com/r/dublok/whisperdock) · 个人维护

**Docker 化的 Whisper C++ 语音转文字 API 服务**

将 Whisper C++ 与 Python 封装为 Docker 容器，通过 HTTP API（/transcribe 端点）提供音频文件转录，返回逐段时间戳的转写文本。服务将 ffmpeg 可读取的音频转换为 16 kHz 单声道 WAV 后转录，上传超过 16 MB 会被拒绝，另有 /health 存活检查端点。提供 latest 稳定版与 main 每夜构建两种 Docker 镜像，也可从源码自行构建；GitHub Actions 自动同步 whisper.cpp 上游更新并发布镜像。面向希望快速集成转录能力的开发者与企业。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker 镜像一键部署，暴露 /transcribe 与 /health HTTP 端点
- 返回带逐段 timestamp 的转录结果
- 提供 latest 稳定版与 main 每夜构建两种镜像
- GitHub Actions 自动同步 whisper.cpp 上游并发布镜像

## 适用场景

- 在自己的服务中通过 HTTP API 快速集成语音转文字能力
- 本地或服务器一键运行 Whisper 转录服务，免去环境配置
- 自动跟进 whisper.cpp 上游更新获取新版本模型运行时

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository hosts the Dockerized speech-to-text transcription service, which utilizes Whisper C++ alongside Pyth
> L64: curl -X POST -F 'file=@/path/to/your/audio.wav' http://localhost:5000/transcribe

## 星数曲线

```mermaid
xychart-beta
    title "ErcinDedeoglu/WhisperDock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9e2e35be45d7` · [字段定义](../../DATASET.md)*
