# AkagawaTsurunaki/zerolan-core

⭐ 121 · Python · MIT · 推送 2026-04-14 · [GitHub](https://github.com/AkagawaTsurunaki/zerolan-core) · [官网](https://github.com/AkagawaTsurunaki/zerolan-core) · 个人维护 · 中文 README

**本地 AI 模型统一部署与推理服务封装层，供配套机器人等项目调用**

将 LLM、ASR、TTS、图像字幕、视频字幕、OCR 等开源可本地部署的模型以统一管线封装为 Web 服务，通过 config.yaml 配置模型 ID、路径、host/port，用 starter.py 启动器部署，对外提供 predict/stream-predict 等 HTTP 接口。每个模型有独立的 uv 或 Anaconda 虚拟环境安装流程，模型默认从 HuggingFace 下载（可配镜像）。LLM 已集成 GLM-4、ChatGLM3、Qwen-7B、Yi-6B、shisa、DeepSeek-R1-Distill 系列及 Ollama 服务；README 给出各模型显存占用与已知问题（如 JSON 语法错误、多卡报错），TTS 依赖特定 fork 的 GPT-SoVITS。主要服务于 ZerolanLiveRobot 等相关项目，作者仅在 Windows 11 与 Ubuntu 22.04 上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一管线封装 LLM/ASR/TTS/OCR/图像与视频字幕六类模型并暴露 HTTP 接口
- 统一 config.yaml 配置与 starter.py 服务启动器
- 每个模型提供 uv 与 Anaconda 两套环境创建流程及显存占用数据
- 支持 HuggingFace 镜像（HF_ENDPOINT）下载模型

## 适用场景

- 为 ZerolanLiveRobot 等机器人项目提供本地 AI 服务后端
- 在同一配置下部署多类本地模型并通过 HTTP API 调用
- 在自有服务器上集中托管 LLM/ASR/TTS 等 GPU 推理服务

## 场景标签

`推理引擎` `语音合成` `语音识别` `OCR` · 领域:内容生成

## 证据(README 行号)

> L5: ZerolanCore 集成了众多开源的、可本地部署的人工智能模型或服务，旨在使用统一的管线设计封装大语言模型（LLM）、自动语音识别（ASR）、文本转语音（TTS）、图像字幕（Image Captioning）、光学字符识别（OC
> L11: 本项目的核心模块结构如下，你可以根据需要选择安装不同类型的 AI 模型：
> L40: > 放到一个你购买的远程服务器上，而 ZerolanLiveRobot 放到你的笔记本电脑上（和远程服务器不是一个主机），

## 星数曲线

```mermaid
xychart-beta
    title "AkagawaTsurunaki/zerolan-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 119 --> 122
    line [120, 121]
```

2026-10-18 120 → 2026-10-28 121（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f78ea6d52d7c` · [字段定义](../../DATASET.md)*
