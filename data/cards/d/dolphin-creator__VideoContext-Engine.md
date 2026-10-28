# dolphin-creator/VideoContext-Engine

⭐ 39 · Python · 推送 2025-12-04 · [GitHub](https://github.com/dolphin-creator/VideoContext-Engine) · 个人维护

**本地视频理解微服务：场景切分+Whisper 转录+Qwen3-VL 描述**

基于 FastAPI 的本地视频理解微服务（v3.19，Public Beta）：先用 HSV 直方图做 CPU 场景切分，再用本地 openai-whisper 产出按场景对齐的时间轴转录与音频特征（语速、静音比等），并用视觉语言模型（默认 Qwen3-VL 2B）对每场景 1–5 个关键帧生成描述与标签，最后汇总全局摘要。输出 JSON 或 txt，结构面向下游 LLM/RAG 管道。macOS 走 MLX 后端，Windows/Linux 走 llama.cpp（自述未充分测试）；提供 RAM 两种模式与 Swagger UI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 场景切分 + Whisper 转录 + VLM 视觉描述 + 全局摘要的组合管线
- 默认 Qwen3-VL 2B，可通过 vlm_model 指向任意 MLX/GGUF 视觉模型
- ram-/ram+ 两种内存模式：按请求加载或预加载加速
- 输出语言跟随用户 prompt 语言，JSON 损坏时有修复/降级逻辑

## 适用场景

- 把长视频转成结构化场景级上下文喂给 LLM 或 RAG 管道
- 对 YouTube 链接或本地视频生成带时间轴的转录与视觉描述
- 在 Apple Silicon 机器上完全本地运行视频分析微服务

## 场景标签

`语音识别` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L7: Local-first microservice for **understanding videos**: scene segmentation + Whisper ASR + Qwen3-VL vision-language m
> L51: - 👁️ **Visual Analysis (Qwen3-VL)**
> L41: - 🎙️ **Audio Transcription (Whisper)**

## 星数曲线

```mermaid
xychart-beta
    title "dolphin-creator/VideoContext-Engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-28 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e41d847e4c74` · [字段定义](../../DATASET.md)*
