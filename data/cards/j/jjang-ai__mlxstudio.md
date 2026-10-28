# jjang-ai/mlxstudio

⭐ 989 · 推送 2026-10-27 · [GitHub](https://github.com/jjang-ai/mlxstudio) · [官网](https://mlx.studio) · 组织维护

**macOS 本地 LLM 运行应用：Apple Silicon 上跑模型并供 OpenAI 兼容 API**

原生 macOS 应用，封装 vMLX 推理服务器，基于 Apple MLX 框架在 Apple Silicon 上 GPU 加速运行大语言模型、视觉模型与图像生成，并以 OpenAI 兼容 HTTP API（localhost）对外服务。面向 Mac 用户与开发者：应用内可浏览下载 Hugging Face 模型，提供聊天、视觉、推理模型、工具调用、文生图、TTS、Whisper 转写等界面；引擎支持连续批处理、投机解码、KV Cache 量化。提供签名公证的 DMG 安装包，捆绑 Python 3.12 环境，无需系统 Python。要求 macOS 14.0+ 与 Apple Silicon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 API 服务器（/v1/chat/completions、/v1/responses）
- 基于 Apple MLX 框架的 GPU 加速推理，支持连续批处理/投机解码/KV Cache 量化
- 应用内从 Hugging Face 浏览并下载模型，无需 Python 配置
- 捆绑 Python 3.12 环境，DMG 签名并公证

## 适用场景

- 在 Mac 上本地运行开源模型并进行对话/图像生成
- 为 OpenAI 兼容客户端提供本机推理 API 端点
- 在应用内做模型转换、量化与诊断

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L12: MLX Studio is a full-featured macOS app that wraps the vMLX inference server — large language models, vision models
> L49: - **OpenAI-Compatible API** -- HTTP server on `localhost` for any compatible client
> L79: |**Server**|OpenAI-compatible API server (`/v1/chat/completions`, `/v1/responses`)|

## 星数曲线

```mermaid
xychart-beta
    title "jjang-ai/mlxstudio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 985 --> 989
    line [986, 988, 988]
```

2026-10-18 986 → 2026-10-28 988（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `06971237357a` · [字段定义](../../DATASET.md)*
