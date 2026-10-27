# thiswillbeyourgithub/Voice2Anki

⭐ 30 · Python · AGPL-3.0 · 推送 2025-12-16 · [GitHub](https://github.com/thiswillbeyourgithub/Voice2Anki) · 个人维护

**用 LLM 修正语音转录并批量生成 Anki 抽认卡的工具**

面向 Anki 用户的语音制卡工具：读取语音录制，经 TTS 模型转写后由 LLM 纠正与格式化，生成抽认卡并通过 AnkiConnect 导入 Anki，支持任意语言与科目。Few-Shot Learning 机制利用用户纠正过的卡片作为示例（配合 embedding 与关键词检索），使后续卡片措辞贴合个人风格。支持 ChatGPT、GPT-4、Replicate 与 OpenRouter 模型（经 litellm），提供 Gradio 界面、多 Profile、OCR 处理及实验性 CLI。需 Python 3.11+、AnkiConnect 插件与 LLM API key；作者声明重构后可能存在 bug 且维护投入将减少。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 修正 TTS 转写文本后生成 Anki 卡片，经 AnkiConnect 直接导入
- Few-Shot Learning：以用户纠正的卡片为示例（embedding+关键词检索）适配个人措辞风格
- 多 LLM 接入：ChatGPT、GPT-4、Replicate、OpenRouter（经 litellm）
- 多 Profile 系统与图片 OCR（保留格式）处理

## 适用场景

- 我口述内容，让工具批量生成并导入 Anki 抽认卡
- 长录音按 STOP 分段后批量制卡
- 让生成的卡片逐渐采用我惯用的措辞与格式

## 场景标签

`语音识别` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: * Voice2Anki is a tool that leverages the power of LLMs (think ChatGPT) to correct the transcription of TTS (text to
> L12:  * **Multiple LLMs**: Supports ChatGPT, GPT-4, replicate models, and openrouter models via litellm

## 星数曲线

```mermaid
xychart-beta
    title "thiswillbeyourgithub/Voice2Anki 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `833c838063e0` · [字段定义](../../DATASET.md)*
