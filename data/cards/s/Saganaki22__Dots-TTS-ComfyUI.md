# Saganaki22/Dots-TTS-ComfyUI

⭐ 40 · Python · Apache-2.0 · 推送 2026-06-11 · [GitHub](https://github.com/Saganaki22/Dots-TTS-ComfyUI) · [官网](https://github.com/rednote-hilab/dots.tts) · 个人维护 · 中文 README

**ComfyUI 自定义节点：dots.tts 语音合成、克隆与 Whisper 转录**

为 ComfyUI 提供 dots.tts 系列模型（base/SOAR/MF，FP32 与 BF16）的加载、文本转语音生成、零样本语音克隆及 Whisper large-v3-turbo 转录节点。支持 24 种官方基准语言，模型文件从 Hugging Face 自动下载。提供可选 torch.compile（Inductor/Triton，CUDA 专用）加速，编译按 max_audio_patches 长度分桶惰性执行；默认 500 patch 约合 160 秒音频预算。可通过 ComfyUI-Manager、uv 或 pip 安装依赖，安装器不自动升级 ComfyUI 核心包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 加载/生成/语音克隆/Whisper 转录四个节点
- 6 个 dots.tts 检查点自动下载（FP32/BF16）
- 可选 torch.compile 加速（CUDA+Triton，惰性分桶编译，最高 1024 patch）
- 24 种官方基准语言，语言下拉含 auto/none

## 适用场景

- 在 ComfyUI 工作流中做文本转语音与低延迟合成
- 零样本克隆参考音频的音色
- 用 Whisper 节点转录音频

## 场景标签

`语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L9: ComfyUI custom nodes for rednote-hilab/dots.tts.
> L24: - Dots TTS Load Model
> L25: - Dots TTS Generate
> L26: - Dots TTS Voice Clone
> L27: - Dots TTS Whisper Transcribe

## 星数曲线

```mermaid
xychart-beta
    title "Saganaki22/Dots-TTS-ComfyUI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-30 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a1338773be7d` · [字段定义](../../DATASET.md)*
