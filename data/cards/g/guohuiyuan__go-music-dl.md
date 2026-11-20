# guohuiyuan/go-music-dl

⭐ 6,604 · Go · AGPL-3.0 · 推送 2026-11-17 · [GitHub](https://github.com/guohuiyuan/go-music-dl) · [官网](https://music.zkkp.nyc.mn) · 个人维护 · 中文 README

**多端音乐搜索下载工具，提供 AI 可调用的播放器控制接口**

基于 Go 的多平台音乐聚合工具，提供 Web、TUI、桌面端与 Android/iOS 包，覆盖单曲、歌单、专辑、排行榜搜索下载与本地音乐管理，聚合网易云、QQ、酷狗、Bilibili、Apple Music、Spotify 等 13 个平台。同时暴露 AI 能力索引与播放器控制接口：AI 通过 HTTP 命令经 SSE 推送到已打开的网页播放器，实现点歌、切歌、暂停、音量调节，多客户端按 client_id 隔离。AI 接口默认无鉴权，文档提示勿直接暴露公网。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 经 HTTP+SSE 直接操控已打开的网页播放器（播放/暂停/音量/进度）
- 聚合 13 个音乐平台的搜索、下载、歌词与无损解析
- 提供 /music/api/ai/index 与 llms.txt 的 AI 能力索引
- Web、TUI、桌面、Android APK、iOS IPA 多端发布

## 适用场景

- 命令行或 Web 界面聚合搜索并下载各平台歌曲与歌单
- 让 AI Agent 通过接口替用户点歌和控制播放
- 扫描整理本地音频并同步到 WebDAV

## 场景标签

 · 领域:音视频/媒体工具

## 证据(README 行号)

> L7: Go Music DL 是一个多平台音乐搜索与下载工具，支持 **Web**、**TUI** 和**桌面端**，覆盖单曲、歌单、专辑、排行榜与本地音乐。它同时暴露了一套 AI 可调用的接口——**AI 可以直接操控你正开着的网页播放
> L64: #### AI 可以直接操控网页播放器
> L103: * **多端使用**：Web、TUI 终端和原生桌面应用，桌面端自动启动内置服务。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `e4d058f3deaf` · [字段定义](../../DATASET.md)*
