# Teriks/dgenerate

⭐ 45 · Python · BSD-3-Clause · 推送 2026-10-26 · [GitHub](https://github.com/Teriks/dgenerate) · [官网](https://dgenerate.readthedocs.io) · 个人维护

**脚本化命令行图像/视频生成与编辑工具（Stable Diffusion 生态）**

dgenerate 是可脚本化的命令行工具兼 Python 库，用于图像生成与编辑（文生图、图生图、inpainting、ControlNet/IP-Adapter/LoRA），支持 LTX、Wan、Hunyuan 等模型一次性生成整段视频，并可对 GIF/WebP/MP4 等逐帧做扩散变换或超分（ESRGAN/SwinIR）。内置 shell 语言与 Tkinter Console UI；量化与 GGUF/FP8 优化支持在有限硬件上运行大模型。另有本地 Qwen 模型从自然语言生成配置脚本的 assistant 子命令。面向需要自动化批量生成与脚本化工作流的开发者，需 Python 3.11+ 与 NVIDIA/AMD/Apple Silicon GPU（CPU 可用但慢）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 SD1.5/2.x/SDXL/SD3/Flux/Qwen-Image 等多种图像模型的生成与编辑
- LTX/Wan/Hunyuan 等模型整段视频生成与逐帧动画处理
- GGUF/FP8/INT8 量化与硬件加速 matmul，有限硬件运行大模型
- 内置 shell 脚本语言、REPL Console UI 与插件体系

## 适用场景

- 批量组合参数自动生成图像变体
- 用提示词或首尾帧生成/延长视频片段
- 对 GIF/MP4 等做逐帧风格化、超分或修复处理
- 通过自然语言让本地 Qwen 模型写出 dgenerate 配置脚本

## 场景标签

`图像生成` `视频生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L16: ``dgenerate`` is a scriptable command-line tool (and library) for generating and editing images, generating whole v
> L28: * Text to image, image to image, inpainting, and diffusion-based upscaling with SD 1.5 / 2.x, SDXL, SD3 / SD3.5, St
> L37: * Generate whole clips in one pipeline call: LTX-2.5 (``--model-type ltx2``) and LTX-Video (``--model-type ltx-vide

## 星数曲线

```mermaid
xychart-beta
    title "Teriks/dgenerate 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-27"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-27 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `71a32d4e7658` · [字段定义](../../DATASET.md)*
