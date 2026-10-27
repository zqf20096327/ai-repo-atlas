# loblawbob873-svg/posterchanai

⭐ 26 · Python · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/loblawbob873-svg/posterchanai) · 个人维护

**自托管的 Nostr 个人云 + Jellyfin 兼容媒体服务器 + 本地 AI**

单机自托管平台：以自运行的 Nostr 中继为唯一数据存储（NIP-44 加密事件），提供笔记、日历、联系人（CalDAV/CardDAV）、文件、密码管理器、邮件、文件夹同步等个人云功能，并附 Jellyfin 兼容媒体服务器、ActivityPub 联邦服务器、直播与 bot 平台。AI 部分：内置 llama.cpp 后端（CPU/CUDA/HIP/Intel Arc），OpenAI 兼容 /v1/ 端点，支持聊天、文生图/视频/音乐、TTS/STT、语音克隆，多机轮询负载均衡。以 Docker Compose 一条命令启动，另提供 Gentoo 基础的 PosterChanOS 桌面系统 ISO 与桌面/Android 客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据以 NIP-44 加密的 Nostr 事件存储于自运行中继，无外部数据库
- 内置 llama.cpp 后端（CPU/CUDA/HIP/Intel Arc SYCL）+ OpenAI 兼容 /v1/，支持 function calling
- Jellyfin 兼容媒体服务器，支持 Quick Connect 客户端接入与 NVIDIA/AMD/CPU 转码
- 生成能力覆盖图像、文生视频、文生音乐（ACE-Step）、TTS/STT 与语音克隆

## 适用场景

- 用一台自有服务器替代云盘、密码管理器与日历联系人同步
- 在自有硬件上运行本地 LLM 并以 OpenAI 兼容接口供工具调用
- 搭建仅限自己与授权好友使用的私人媒体库与直播节点
- 以 Nostr 身份登录同时接入 Mastodon 等联邦宇宙

## 场景标签

 · 领域:自托管/个人云/fediverse

## 证据(README 行号)

> L12: **Replace the cloud, then put a GPU behind it.** Your notes, calendar, contacts, addressbook, files, photos, passwo
> L16: **Then the part a cloud drive can't do:** the same box runs your own models. Chat, image, voice, video and music ge
> L94: - 🔌 **Bring any model, or host it** — cloud (any OpenAI-compatible API) or the **built-in native `llama.cpp`** back

## 星数曲线

```mermaid
xychart-beta
    title "loblawbob873-svg/posterchanai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 27
    line [25, 26]
```

2026-10-18 25 → 2026-10-27 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `2e8597c161a8` · [字段定义](../../DATASET.md)*
