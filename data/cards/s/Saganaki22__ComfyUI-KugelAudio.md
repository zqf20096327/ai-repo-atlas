# Saganaki22/ComfyUI-KugelAudio

⭐ 34 · Python · 推送 2026-02-10 · [GitHub](https://github.com/Saganaki22/ComfyUI-KugelAudio) · [官网](https://huggingface.co/kugelaudio/kugelaudio-0-open) · 个人维护

**ComfyUI 的 KugelAudio 语音合成自定义节点：24 种欧洲语言 TTS 与声音克隆**

为 ComfyUI 提供的 KugelAudio 自定义节点集，封装 7B 参数的 AR + Diffusion 架构文本转语音模型：支持 24 种欧洲语言的单说话人 TTS、基于 5-30 秒参考音频的声音克隆、最多 6 说话人的对话生成（可配置说话人间停顿 0-2 秒）。输出音频内嵌 AudioSeal 不可闻水印，并附带水印检测节点。全精度约需 19GB VRAM，4-bit 量化（需 CUDA 与 bitsandbytes）降至约 8GB；支持 CUDA/MPS/CPU 设备选择。模型首次运行时自动下载到 ComfyUI/models 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 24 种欧洲语言的 TTS 与参考音频声音克隆
- 最多 6 说话人对话生成，停顿可配置
- 输出内嵌 AudioSeal 水印并附检测节点
- 4-bit 量化将 VRAM 从约 19GB 降至约 8GB

## 适用场景

- 在 ComfyUI 工作流中做多语言配音或旁白生成
- 用短参考音频克隆特定音色
- 生成多角色对话音频并检测音频是否由 KugelAudio 生成

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L26: - **Single Speaker TTS**: Convert text to speech
> L27: - **Voice Cloning**: Clone any voice from reference audio (5-30 seconds)
> L214: Clone any voice using a short reference audio sample (5-30 seconds recommended).

## 星数曲线

```mermaid
xychart-beta
    title "Saganaki22/ComfyUI-KugelAudio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-25 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ed357fbcbf7a` · [字段定义](../../DATASET.md)*
