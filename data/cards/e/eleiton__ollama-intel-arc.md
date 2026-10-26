# eleiton/ollama-intel-arc

⭐ 426 · Dockerfile · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/eleiton/ollama-intel-arc) · 个人维护

**在 Intel Arc GPU 上用容器部署 Ollama、SD、Whisper 的方案**

面向 Intel Arc 显卡（含 Meteor Lake 核显）用户的 Docker/Podman Compose 部署方案：提供原生 SYCL llama.cpp 后端自编译的 Ollama 镜像（两阶段构建，无 IPEX-LLM 依赖）及免编译的 Vulkan 备选路径，并配套 Open WebUI 聊天界面、ComfyUI/SD.Next 图像生成与 Whisper 语音识别容器。运行参数通过 .env 配置（上下文长度、KV 缓存类型、GPU offload 等），默认值针对 UMA 核显调优；Stable Diffusion 与 Whisper 容器基于 Intel Extension for PyTorch。开发者环境为 Fedora 43 + Core Ultra 7 155H。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生 SYCL ggml-sycl 后端的 Ollama 两阶段本地构建镜像
- 免编译的 Vulkan 备选 compose（复用官方 ollama/ollama 镜像）
- Ollama 运行参数经 .env 配置（KV 缓存、flash attention、GPU offload 等）
- 配套 Open WebUI、ComfyUI、SD.Next、Whisper 容器

## 适用场景

- 在 Intel Arc GPU 的 Linux 机器上本地跑 LLM
- 通过 Open WebUI 进行对话并生成图像
- 用 Whisper 容器转录或翻译音频文件

## 场景标签

`推理引擎` `图像生成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L13: The Ollama container runs a **native SYCL (or Vulkan) llama.cpp backend** built directly from upstream Ollama — no 
> L19:  * Runs Ollama with a **native llama.cpp `ggml-sycl` backend**, compiled from Ollama source against Intel® oneAPI (
> L56: $ podman compose -f docker-compose.ollama-sycl.yml up -d --build

## 星数曲线

```mermaid
xychart-beta
    title "eleiton/ollama-intel-arc 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 424 --> 427
    line [425, 426, 426]
```

2026-10-18 425 → 2026-10-26 426（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `486e00252c8b` · [字段定义](../../DATASET.md)*
