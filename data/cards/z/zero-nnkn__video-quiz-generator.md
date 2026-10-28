# zero-nnkn/video-quiz-generator

⭐ 21 · Python · 推送 2026-10-05 · [GitHub](https://github.com/zero-nnkn/video-quiz-generator) · 个人维护

**从视频生成测验题的 Web 应用：转写加 LLM 出题**

面向观看视频后想自测理解的用户：上传视频后，后端用 Faster Whisper（Whisper 的重新实现，CPU Float32 运行）做语音转写，再调用 LLM API（Google Bard 的非官方 cookie API、OpenAI GPT）生成测验题。架构为前后端分离：Streamlit 前端 + FastAPI 后端，需同时运行。提供 pip 依赖安装与 Docker Compose 快速启动两种方式；限制包括仅测试过英文、OpenAI 配置未经充分测试、生成题目需人工复核。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Faster Whisper 语音转写（CPU Float32，可改配置）
- 支持 Google Bard（非官方 API）与 OpenAI GPT 两种出题后端
- Streamlit + FastAPI 前后端分离架构
- 提供 Docker Compose 快速启动

## 适用场景

- 看完教学视频后生成测验题检验掌握程度
- 为课程或讲座视频快速出题

## 场景标签

 · 领域:教育/AI 应用

## 证据(README 行号)

> L2: This is a simple web app that let you generate quizzes❓ from given video to check your understanding after watching 
> L8:  - Speech recognition: Using Faster Whisper, a reimplementation of OpenAI's Whisper, with faster inference and appro
> L9:  - Quizzes generation: Using available APIs. Note that bard's API has not been released yet. So we use an Bard-API (

## 星数曲线

```mermaid
xychart-beta
    title "zero-nnkn/video-quiz-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `c709a31c513d` · [字段定义](../../DATASET.md)*
