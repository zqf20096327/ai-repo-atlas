# paladini/voice-separator-demucs

⭐ 41 · Python · MIT · 推送 2026-07-23 · [GitHub](https://github.com/paladini/voice-separator-demucs) · [官网](https://hub.docker.com/r/paladini/voice-separator) · 个人维护

**自托管 Web 应用：用 AI 从音乐中分离人声与乐器**

基于 Demucs 模型（Facebook/Meta AI）的自托管音频分离 Web 应用，后端为 FastAPI + PyTorch。用户通过浏览器界面上传 MP3/WAV/FLAC/M4A/AAC 文件或粘贴 YouTube 链接（限 10 分钟），分离出人声、鼓、贝斯等元素并下载。提供 4 种 Demucs 模型可选：默认 CPU Lite 版无需 GPU，htdemucs 等高质量模型需 GPU。首次运行自动下载约 200MB 模型；主要面向无编程需求的个人用户，声明仅限个人与教育用途。

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

- Web 界面操作，无需编程，支持 5 种音频格式
- 4 种 Demucs 模型可选，默认 CPU Lite 版无需 GPU
- 支持直接处理 YouTube 视频（限 10 分钟）
- 提供 Docker 一条命令部署与 FastAPI 交互式 API 文档

## 适用场景

- 制作卡拉OK伴奏或提取人声
- 单独提取鼓、贝斯等乐器音轨用于练习或混音
- 本地自托管处理音频，不上传第三方服务

## 场景标签

 · 领域:音频处理/AI 应用

## 证据(README 行号)

> L3: A simple and efficient self-hosted web application to separate audio elements (vocals, drums, bass, other instrument
> L135: This application uses **Demucs**, an AI model developed by Facebook/Meta AI specifically for music source separati

## 星数曲线

```mermaid
xychart-beta
    title "paladini/voice-separator-demucs 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-25"]
    y-axis "stars" 38 --> 42
    line [39, 40, 41, 41]
```

2026-10-18 39 → 2026-10-25 41（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `721a0e71c22b` · [字段定义](../../DATASET.md)*
