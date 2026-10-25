# elbruno/ElBruno.QwenTTS

⭐ 43 · C# · MIT · 推送 2026-09-29 · [GitHub](https://github.com/elbruno/ElBruno.QwenTTS) · 个人维护

**在 C#/.NET 中本地运行 Qwen3-TTS 语音合成的 ONNX 管线库**

将 Qwen3-TTS 导出为 ONNX 并通过 ONNX Runtime 在本地 C#/.NET 环境做文本转语音，推理时无需 Python。提供 0.6B 与 1.7B 两种模型变体（首次运行自动从 HuggingFace 下载，约 5.5–10 GB），支持 9 个预置音色、自然语言风格指令控制、3 秒样本语音克隆、CUDA/DirectML 可选 GPU 加速，输出 24 kHz WAV。以 NuGet 包、CLI、文件批处理工具与 Blazor Web UI 形式提供，并集成 Microsoft.Extensions.AI 的 ITextToSpeechClient 契约。需 .NET 8/10 SDK，模型缓存于 %LOCALAPPDATA%。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ONNX Runtime 本地推理，推理时无需 Python，模型首跑自动下载
- 0.6B/1.7B 双变体，1.7B 支持自然语言 instruct 风格控制
- 3 秒音频样本语音克隆（ElBruno.QwenTTS.VoiceCloning 包）
- Microsoft.Extensions.AI ITextToSpeechClient 适配与流式 WAV 输出

## 适用场景

- 在 .NET 应用中本地生成多语言语音而无需部署 Python 服务
- 用 3 秒参考音频克隆音色并合成语音
- 批量将文本或 SRT 字幕文件转换为音频

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L11: Run **Qwen3-TTS** text-to-speech locally from C# using ONNX Runtime — no Python needed at inference time. Models ar
> L22: - **Local TTS Inference** — Run Qwen3-TTS entirely on your machine using ONNX Runtime

## 星数曲线

```mermaid
xychart-beta
    title "elbruno/ElBruno.QwenTTS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4aa06daaa0b7` · [字段定义](../../DATASET.md)*
