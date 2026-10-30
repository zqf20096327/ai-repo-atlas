# RakeshBabuGajula/real-time-voice-translator

⭐ 16 · Python · NOASSERTION · 推送 2026-10-16 · [GitHub](https://github.com/RakeshBabuGajula/real-time-voice-translator) · 个人维护

**实时语音翻译 Web 应用：语音识别→翻译→合成语音回放**

基于 Streamlit 的端到端语音翻译应用：麦克风采集语音后经 Google ASR 识别为文本，对印度语言先做罗马拼音到原生文字的转写（google-transliteration-api），再用 deep-translator 做神经翻译（15+ 语言），经 gTTS 合成音频回放；支持人工在线校对文本、语音停止指令与 CSV 语料导出。另有 Tkinter 桌面客户端与 cx-Freeze 打包的 Windows exe。需联网使用云端识别/翻译/TTS 服务，v3.0 计划支持本地离线推理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ASR→转写→翻译→TTS 四段式管线，15+ 语言含多种印度语言
- 人工在环（HITL）：识别与译文均可实时编辑
- 一键导出带时间戳与语言标注的 CSV 语料数据集
- 双架构：Streamlit Web 应用与 Tkinter 桌面客户端（可打包 exe）

## 适用场景

- 跨语言实时对话时把我的语音翻译成目标语言并朗读
- 人工校对识别/译文后再合成与导出
- 收集并导出多语言语音平行语料用于研究

## 场景标签

`语音识别` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L25: **Real-Time Voice Translator** is a production-grade, end-to-end speech translation and synthesis application engin
> L93: |**Acoustic Ingest & ASR**|**SpeechRecognition + PyAudio**|Microphone audio stream ingest, energy thresholding, and
> L94: |**Neural Machine Translation**|**deep-translator**|RESTful translation wrapper supporting Google Neural Machine Tr

## 星数曲线

```mermaid
xychart-beta
    title "RakeshBabuGajula/real-time-voice-translator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `39d83aa9e06a` · [字段定义](../../DATASET.md)*
