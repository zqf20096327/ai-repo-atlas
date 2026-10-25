# lperezmo/real-time-translator

⭐ 45 · Python · GPL-3.0 · 推送 2026-08-30 · [GitHub](https://github.com/lperezmo/real-time-translator) · 个人维护

**实时语音翻译 Web 应用：Whisper 转录翻译，gTTS 播放译文**

基于 Streamlit 的 Web 应用，面向需要即时语音翻译的用户：从麦克风或音频文件录制语音，调用 Whisper API 完成转录，将任意语言翻译为英文并以文字显示，随后用 Google Text-to-Speech（gTTS）合成并播放译文。依赖 Python 3.7+，通过 git clone 克隆源码、pip 安装依赖后以 streamlit run 本地运行，同时提供线上 Demo（translator.streamlit.app）。翻译目标语言固定为英文，采用 GPL-3.0 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从麦克风或音频文件转录语音
- 任意语言翻译为英文并显示文字结果
- gTTS 将译文合成语音播放
- 提供线上 Demo 与本地运行两种方式

## 适用场景

- 跨语言对话中即时听懂外语语音并听到英文译文
- 将录制的音频文件转录并翻译为英文
- 不部署服务直接使用托管 Demo 完成快速翻译

## 场景标签

`语音识别` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L10: A web app to translate speech in real time using the Whisper API for transcribing and translating recorded audio, a
> L14: - Transcribe speech from microphone or audio file
> L16: - Translate speech or text into English from any language
> L20: - Translation synthesized as speech by Google text-to-speech module (gTTS).

## 星数曲线

```mermaid
xychart-beta
    title "lperezmo/real-time-translator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-25 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7bffd1777830` · [字段定义](../../DATASET.md)*
