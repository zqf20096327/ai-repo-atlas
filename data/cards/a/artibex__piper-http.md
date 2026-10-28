# artibex/piper-http

⭐ 21 · Python · MIT · 推送 2026-03-06 · [GitHub](https://github.com/artibex/piper-http) · [官网](https://hub.docker.com/r/artibex/piper-http) · 个人维护

**将 Piper 文本转语音服务打包为 Docker HTTP API 的镜像**

基于 rhasspy/piper 的 Docker 镜像封装项目：提供预构建的 Docker Hub 镜像，首次启动自动下载默认德语语音模型（存储于命名卷 piper-models），在 5000 端口提供 HTTP API，GET 请求传入文本即返回 WAV 音频。通过 docker-compose 的 MODEL_DOWNLOAD_LINK 变量可切换 Hugging Face 上的其他语音；另附 Python 客户端脚本，依赖系统音频播放器（pw-play/paplay/mpv/ffplay）直接播放。给需要快速部署本地 TTS 服务的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker Compose 一条命令启动，预构建镜像来自 Docker Hub
- HTTP API 接收文本返回 WAV 音频，端口 5000
- 模型存储于命名卷，仅下载一次；可切换 Hugging Face 上的多语言语音
- 附 Python 客户端脚本，支持指定服务器 URL 并直接播放音频

## 适用场景

- 用 Docker 快速部署本地 TTS HTTP 服务
- 通过 curl 或 Python 客户端将文本合成语音
- 切换不同语言/说话人的 Piper 语音模型

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L2: Creates a docker image that runs the piper http service found in this repo:
> L22: That's it. The container pulls `artibex/piper-http:latest` from Docker Hub, downloads the default German voice on f
> L27: curl "http://localhost:5000/?text=Hello+World" -o hello.wav

## 星数曲线

```mermaid
xychart-beta
    title "artibex/piper-http 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `92fd9b935d65` · [字段定义](../../DATASET.md)*
