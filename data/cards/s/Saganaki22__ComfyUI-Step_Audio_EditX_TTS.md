# Saganaki22/ComfyUI-Step_Audio_EditX_TTS

⭐ 63 · Python · Apache-2.0 · 推送 2025-12-04 · [GitHub](https://github.com/Saganaki22/ComfyUI-Step_Audio_EditX_TTS) · [官网](https://huggingface.co/stepfun-ai/Step-Audio-EditX) · 个人维护

**Step-Audio-EditX 零样本语音克隆与音频编辑的 ComfyUI 节点集**

为 ComfyUI 提供的纯 Python 原生节点集，封装 stepfun-ai 的 Step-Audio-EditX 模型：Clone 节点从 3-30 秒参考音频做零样本语音克隆并合成任意文本语音，支持长文本分块拼接；Edit 节点在保留音色的前提下修改情绪、风格、语速、副语言效果并降噪，输入音频限 0.5-30 秒。需手动下载约 10GB 的模型与 Tokenizer，VRAM 需求随量化档位约 9-18GB，系统需安装 FFmpeg。面向在 ComfyUI 中构建语音工作流的用户，经 ComfyUI Manager 或 git clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零样本语音克隆（3-30 秒参考音频，支持长文本分块拼接）
- 音频编辑：8 种情绪、6 种风格、语速、副语言效果与降噪
- 量化档位（none/int8/int4/int4_awq）与多种注意力机制控制 VRAM 占用
- 纯 Python 实现，无需 JavaScript

## 适用场景

- 在 ComfyUI 中克隆参考音色并合成任意文本语音
- 为游戏/动画角色或配音生成一致的语音
- 对 30 秒以内的录音修改情绪、风格或加笑声等效果

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L18: Native ComfyUI nodes for **Step Audio EditX** - State-of-the-art zero-shot voice cloning and audio editing with emo
> L24: - **⚡ Native ComfyUI Integration**: Pure Python implementation - no JavaScript required

## 星数曲线

```mermaid
xychart-beta
    title "Saganaki22/ComfyUI-Step_Audio_EditX_TTS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-25 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `538326349b1a` · [字段定义](../../DATASET.md)*
