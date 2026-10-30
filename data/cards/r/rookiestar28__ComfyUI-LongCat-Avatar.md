# rookiestar28/ComfyUI-LongCat-Avatar

⭐ 43 · Python · MIT · 推送 2026-08-08 · [GitHub](https://github.com/rookiestar28/ComfyUI-LongCat-Avatar) · 个人维护

**在 ComfyUI 中运行 LongCat Avatar 1.5 音频驱动数字人视频生成的自定义节点**

将官方 Avatar 1.5 流水线适配为 ComfyUI 自定义节点包，提供 9 个节点，覆盖 CUDA 推理、Whisper-large-v3 音频条件、必需的 distill LoRA、单/多音频数字人生成（480p/720p）、单文件 safetensors 与官方分片/INT8 DiT 加载，以及受控的官方权重自动下载；可选人声分离。运行路径面向 CUDA，需 NVIDIA GPU 与已装好的 CUDA PyTorch，CPU/MPS 不支持，另有 Apple Silicon MLX 测试分支 macOS-MLX。要求 Python >=3.10,<3.14 与 PATH 上的 ffmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个节点支持单音频 ai2v/at2v 与多音频数字人生成
- 支持单文件 safetensors、官方分片与 INT8 分片 DiT 三种权重模式
- Whisper-large-v3 音频条件与可选 Kim_Vocal_2 人声分离
- 提供官方 sharded DiT 与共享文本编码器的受控自动下载

## 适用场景

- 在 ComfyUI 工作流中用音频驱动生成数字人说话视频
- 在 ComfyUI 内加载 LongCat Avatar 1.5 官方或 INT8 权重
- 对含人声的音频做人声分离后再驱动生成

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: This repository adapts the official Avatar 1.5 pipeline to ComfyUI. It focuses on CUDA inference, Whisper-large-v3 a
> L60: Install the custom node inside ComfyUI:
> L71: Use the Python environment that launches ComfyUI. The runtime path is CUDA-oriented and expects a compatible NVIDIA

## 星数曲线

```mermaid
xychart-beta
    title "rookiestar28/ComfyUI-LongCat-Avatar 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-30 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c08bde7ee32f` · [字段定义](../../DATASET.md)*
