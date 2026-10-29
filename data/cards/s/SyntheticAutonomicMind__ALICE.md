# SyntheticAutonomicMind/ALICE

⭐ 18 · Python · GPL-3.0 · 推送 2026-10-19 · [GitHub](https://github.com/SyntheticAutonomicMind/ALICE) · 组织维护

**本地图像与音频生成服务：Web 界面+OpenAI 兼容 API**

Python 编写的本地生成服务，运行 Stable Diffusion（SD1.5/2.x/SDXL/FLUX）图像生成与 Stable Audio Open、MiniMax Music 3 音频合成。作为服务与编排层，模型权重从 CivitAI/HuggingFace 下载后按请求加载，提供 Web 管理界面、OpenAI 兼容 REST API、模型下载管理与 VRAM 感知切换。支持 NVIDIA CUDA、AMD ROCm/Vulkan、Apple Silicon MPS 与 CPU 四类后端，可经 macOS launchctl、Linux systemd 安装脚本或 Docker 部署，并与同组织的 SAM/CLIO 集成。生成内容默认本地保存，模型文件需 2-10 GB 另行下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本生图/图生图支持 SD1.5、SDXL、FLUX 与多种调度器
- 音频生成：Stable Audio Open（47s 立体声）与 MiniMax Music 3（最长 6 分钟歌曲）
- OpenAI 兼容 REST API 与 Web 管理界面、模型下载管理
- PyTorch 与 stable-diffusion.cpp 双后端，覆盖 CUDA/ROCm/Vulkan/MPS/CPU

## 适用场景

- 在自己硬件上生成图像与音乐，按次付费
- 通过 OpenAI 兼容 API 为本地应用提供生成服务
- 在 Steam Deck 等 AMD 设备上本地跑扩散模型

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L15: ALICE is a Python service that runs Stable Diffusion image generation and audio synthesis on your hardware. It prov
> L17: ALICE is the serving and orchestration layer. The model weights are separate — Stable Diffusion, FLUX, and audio mo
> L59: - OpenAI-compatible REST API — `POST /v1/chat/completions` for images, `POST /v1/audio/generations` for audio

## 星数曲线

```mermaid
xychart-beta
    title "SyntheticAutonomicMind/ALICE 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3e3782cefbf4` · [字段定义](../../DATASET.md)*
