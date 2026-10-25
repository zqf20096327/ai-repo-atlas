# SMACY2017/InterPilot

⭐ 141 · Python · 推送 2026-09-23 · [GitHub](https://github.com/SMACY2017/InterPilot) · 个人维护 · 中文 README

**Windows AI 面试助手：捕获音频、本地转写并调用 LLM 生成回答**

面向 Windows 用户的 PyQt5 桌面工具，由录音、转写、LLM 回答三个模块组成：通过 wasapi loopback 捕获扬声器或麦克风音频，保存为 WAV；基于 Whisper 模型本地转写（默认 base 规格可选 tiny 到 turbo）；将文本拼接默认提示词后调用 OpenAI 兼容 API（默认推荐硅基流动上的 DeepSeek-R1-Distill-Qwen-7B），流式返回并支持 Markdown 渲染。README 说明内测用户反映可在面试场景辅助，并声明禁止用于面试作弊。系统依赖 FFmpeg，源码运行，无桌面安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- wasapi loopback 捕获系统扬声器音频并保存 WAV
- Whisper 本地转写，支持 tiny/base/small/medium/large/turbo 多种规格
- 调用 OpenAI 兼容 LLM API，流式返回并支持 Markdown 渲染
- 提供 GUI（main.py）与终端（main_cmd.py）两种运行方式

## 适用场景

- 在会议或学习场景中捕获音频并实时获得 AI 回答辅助
- 录制系统声音后本地转写为文字
- 通过修改默认提示词适配不同问答场景

## 场景标签

`语音识别` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L15: 本项目是一个基于 AI 的助手工具，能够从windows的输入输出设备中捕获音频，将音频转为文字后，再调用 LLM（大语言模型） API 给出回答。项目主要包括录音、转写和 AI 回答三个模块，**旨在为个人的正当学习、工作、科研
> L17: 部分内测用户反映，本工具可能可以在面试、会议、学习等场景中提供一定的帮助，比如在在线会议软件中作为AI面试工具辅助面试：获取面试官的音频然后得到回答，但是请注意：**本工具仅供学习交流使用，不得用于任何不正当用途**。
> L37:  基于 Whisper 模型在**本地进行音频转写**，支持多种模型规格（默认使用 `base` 模型）。

## 星数曲线

```mermaid
xychart-beta
    title "SMACY2017/InterPilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 140 --> 142
    line [141, 141]
```

2026-10-18 141 → 2026-10-25 141（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e635144413a5` · [字段定义](../../DATASET.md)*
