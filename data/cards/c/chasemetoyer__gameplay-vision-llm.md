# chasemetoyer/gameplay-vision-llm

⭐ 14 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/chasemetoyer/gameplay-vision-llm) · 个人维护

**多模态游戏视频理解研究框架：视觉+音频+LLM 问答**

研究框架，对游戏视频做多模态感知与自然语言问答：以 SAM3/SigLIP 做视觉分割与语义嵌入、VideoMAE 做时序理解、Wav2Vec2/Whisper 做音频处理、PaddleOCR 做屏显文字提取，通过学习到的投影层将异构嵌入映射到 Qwen3-VL-8B 的 4096 维隐空间，再经 LoRA 微调实现长时程推理。提供混合检索（时间戳+语义）、分层时间上下文压缩、自动联网检索工具、置信度评分与三阶段基准评测（GlitchBench/VideoGameQA-Bench/LongVideoBench 等）。按显存提供 light/standard/full 三档预设（约 20/28/45GB），需 CUDA 12.8+ 与 NVIDIA GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多编码器（SAM3/SigLIP/VideoMAE/Wav2Vec2/Whisper/OCR）投影到统一 LLM 隐空间
- LoRA 微调 Qwen3-VL-8B 实现长时程推理与因果问答
- 混合检索（时间戳窗口+语义检索）与分层时间上下文压缩
- 3 阶段基准评测与三档硬件感知配置预设

## 适用场景

- 对游戏录像做自然语言问答与时序事件总结
- 在 GlitchBench、VideoGameQA-Bench 等基准上评测视频问答系统
- 检测游戏 glitch 并生成结构化 bug 报告
- 按显存档位在消费级/数据中心 GPU 上运行视频推理

## 场景标签

`多模态` `RAG` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L19: This project implements a multimodal perception-reasoning pipeline for analyzing gameplay videos. The system integr
> L97: - **Base Model**: Qwen/Qwen3-VL-8B-Instruct
> L106: This project has been tested on:

## 星数曲线

```mermaid
xychart-beta
    title "chasemetoyer/gameplay-vision-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `21d334ef1eb9` · [字段定义](../../DATASET.md)*
