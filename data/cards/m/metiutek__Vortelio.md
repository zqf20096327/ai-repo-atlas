# metiutek/Vortelio

⭐ 20 · Go · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/metiutek/Vortelio) · [官网](https://vortelio.netlify.app/) · 组织维护

**本地多模态 AI 平台：单二进制运行 LLM/图像/语音/视频/3D 模型**

Go 单二进制加内置 Web UI 的自托管离线 AI 平台，覆盖 GGUF LLM 运行（llama.cpp 后端自动安装更新）、Stable Diffusion/FLUX 图像生成、Whisper 语音转写、Kokoro/Bark TTS、视频与 3D 生成，并集成 CrewAI 多智能体编排和终端编码代理。提供 OpenAI 兼容与 Ollama 兼容 API，可作 OpenAI SDK/LangChain 的 base_url 直接替换；支持 CUDA/ROCm/Metal/CPU 自动检测、后台服务与自动更新。经 uv/PyPI、Windows 安装包或源码构建安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制覆盖 LLM/图像/语音/视频/3D 多模态本地推理
- OpenAI 兼容与 Ollama 兼容 API 双通道
- 内置 CrewAI 多智能体编排与终端编码代理 vortelio code
- 硬件自动检测（CUDA/ROCm/Metal/CPU），无需 Docker

## 适用场景

- 在本机离线运行各类开源模型，不依赖云服务与 API key
- 用现有 OpenAI SDK/LangChain 代码直接指向本地端点
- 搭建本地多智能体工作流（CrewAI）与编码代理

## 场景标签

`多模态` `推理引擎` `图像生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L23: **Vortelio** is a self-hosted, offline AI platform that replaces Ollama, ComfyUI, Whisper UIs, and CrewAI cloud ser
> L150: - 🧠 **LLMs** — llama.cpp backend (installed and kept up to date automatically, so new model architectures just wor
> L156: - 🔌 **API compatibility** — drop-in for OpenAI `/v1/chat/completions` and Ollama `/api/chat`

## 星数曲线

```mermaid
xychart-beta
    title "metiutek/Vortelio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-29 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c14c3b6389ff` · [字段定义](../../DATASET.md)*
