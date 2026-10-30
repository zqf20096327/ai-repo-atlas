# runzhliu/docker-antigravity

⭐ 21 · Dockerfile · MIT · 推送 2026-03-11 · [GitHub](https://github.com/runzhliu/docker-antigravity) · 个人维护 · 中文 README

**把 Antigravity 装进 Docker 并经浏览器访问的自托管镜像**

基于 linuxserver/chrome 构建的 Docker 镜像：容器内安装 Google Artifact Registry 官方 Debian 源的 Antigravity，通过 Selkies-GStreamer（WebRTC）串流 Openbox 桌面，用户在浏览器 https://localhost:3001 访问，无需本地安装。内置 nginx 提供 HTTPS（自签名或 Let's Encrypt，含每周自动续期 cron）。不发布预构建镜像，须本地 docker build；基础镜像仅 linux/amd64，ARM 主机经 QEMU 模拟构建。限制：仅供个人学术研究，用户需自行遵守 Google 服务条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 linuxserver/chrome，经 Selkies(WebRTC) 浏览器串流桌面
- 可选 Let's Encrypt 证书自动获取与每周无停机续期
- 支持 HTTP Basic Auth、PUID/PGID、/config 卷持久化
- ARM 主机（如 Apple Silicon）经 QEMU 模拟构建 amd64 镜像

## 适用场景

- 在服务器或 NAS 上自托管 Antigravity，通过浏览器使用
- 为公网部署配可信 HTTPS 证书
- 在无本地安装条件的主机上运行 Antigravity

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Run Antigravity in a Docker container with a browser-accessible GUI via Selkies — no local installation required.
> L100: 1. Builds on `linuxserver/chrome`, which provides a lightweight Openbox desktop streamed via Selkies-GStreamer (We
> L101: 2. Installs Antigravity from Google Artifact Registry's official Debian repository.

## 星数曲线

```mermaid
xychart-beta
    title "runzhliu/docker-antigravity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c6815f40e9d7` · [字段定义](../../DATASET.md)*
