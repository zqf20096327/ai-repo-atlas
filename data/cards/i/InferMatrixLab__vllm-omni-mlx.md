# InferMatrixLab/vllm-omni-mlx

⭐ 26 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/InferMatrixLab/vllm-omni-mlx) · 组织维护

**Apple Silicon 上的全模态模型推理服务器，OpenAI/Anthropic 兼容 API**

vLLM-Omni 的 Apple Silicon 轻量版本：基于 MLX 引擎栈，以单进程、batch-1 低延迟设计提供 OpenAI 与 Anthropic 兼容的 chat API 及 OpenAI 语音合成/识别端点，支持文本、图像、音频输入与文本、语音输出。通过 mlx-vlm/mlx-audio 加载 Hugging Face 模型（Qwen3-TTS/Omni/ASR、VoxCPM2 等），核心安装约 440 MB 且不含 torch。限制：单模型串行生成、工具调用未支持、语音输出对话与视频输入为进行中工作；需 Python 3.10+ 与 arm64 Mac，尚无 PyPI wheel，须源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- OpenAI /v1/chat/completions、Anthropic /v1/messages 与 /v1/audio/* 端点，均支持流式
- 流式 TTS 首音频约 0.1 s，持续 RTF 0.29–0.45（官方 README 数据）
- 跨轮 prompt cache、--draft-model 投机解码、--kv-bits 量化 KV cache 等性能选项
- 核心安装约 440 MB，无 FastAPI/pydantic/torch

## 适用场景

- 在 Mac 上本地部署 Qwen3 系列 TTS/ASR/Omni 模型并通过 OpenAI 兼容 API 调用
- 为语音合成或语音识别服务搭建轻量单进程后端
- 本地零样本语音克隆与文本描述音色生成

## 场景标签

`推理引擎` `语音合成` `语音识别` `多模态` · 领域:内容生成

## 证据(README 行号)

> L18: vllm-omni-mlx is its lightweight Apple Silicon counterpart: the same serving surface —
> L19: OpenAI- and Anthropic-compatible chat APIs plus OpenAI speech synthesis — on MLX,
> L24: - **Lightweight by design**: one model per process, no scheduler, no worker pool, no FastAPI/pydantic

## 星数曲线

```mermaid
xychart-beta
    title "InferMatrixLab/vllm-omni-mlx 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-19 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `8272e685da9b` · [字段定义](../../DATASET.md)*
