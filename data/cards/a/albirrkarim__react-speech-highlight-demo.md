# albirrkarim/react-speech-highlight-demo

⭐ 190 · JavaScript · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/albirrkarim/react-speech-highlight-demo) · [官网](https://react-speech-highlight.vercel.app) · 个人维护

**网页端 TTS 朗读与逐词/逐句高亮同步的前端库**

面向 Web 开发者的付费（一次性买断）TypeScript 库，提供 React、Vanilla JS 与 React Native 三个版本。核心功能是在网页中播放文本转语音并实时高亮正在朗读的词与句子：既可使用浏览器内置 Web Speech Synthesis，也可回退或优先使用任意 TTS API 生成的音频文件（mp3/wav 等），词句时间戳在客户端检测，无需专门后端。附加能力包括 SSR、口型（viseme）状态输出、YouTube 转录高亮、LLM 发音纠正、实时通话字幕等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 客户端检测音频中词句的朗读时间并驱动高亮
- 支持 Web Speech Synthesis 与音频文件双引擎（prefer/fallback）
- 输出当前 viseme 状态，可用于 3D 头像口型同步
- 支持非拉丁字母（中日韩俄文）多字符与 SSR

## 适用场景

- 给长文章加朗读按钮并显示阅读进度
- 为语言学习应用做真人录音的逐词高亮朗读
- Web AI 头像/NPC 的语音与口型同步
- 视频播放时自动生成并高亮双语字幕

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L93: How can you automatically get the audio file for some text? you can use ElevenLabs, Murf AI, Open AI, Amazon Polly,
> L97: How does this package know the timing of spoken words or sentences in played audio? This package can detect the spo

## 星数曲线

```mermaid
xychart-beta
    title "albirrkarim/react-speech-highlight-demo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 188 --> 191
    line [189, 190, 190]
```

2026-10-18 189 → 2026-10-31 190（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `5e7b092594c6` · [字段定义](../../DATASET.md)*
