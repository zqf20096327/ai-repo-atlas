# suryanshsk/Python-Voice-Assistant-Suryanshsk

⭐ 56 · Jupyter Notebook · MIT · 推送 2026-03-05 · [GitHub](https://github.com/suryanshsk/Python-Voice-Assistant-Suryanshsk) · 个人维护

**调用 Gemini AI 的 Python 语音助手，含天气/新闻/音乐等功能**

基于 Python 的虚拟助手项目，通过 google-generativeai SDK 接入 Gemini AI，实现语音识别（SpeechRecognition/pyaudio）、文本转语音（gTTS）、天气查询、新闻获取、笑话、维基百科检索、音乐管理与问答，并附带带动画的交互式 Web 界面。需在代码中手动替换 Gemini、新闻、天气三个 API key 后运行主脚本。项目以源码形式安装（clone 后 pip 安装依赖），参与 GSSoC'2024 与 Hacktoberfest 2024 开源活动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音识别与 gTTS 文本转语音
- 接入 Gemini AI 回答用户问题
- 天气/新闻/维基百科/音乐管理等聚合功能
- 附带带动画的交互式 Web 界面

## 适用场景

- 本地运行一个能听会说的生活助手
- 用语音查询天气、新闻和维基百科信息
- 在其上扩展自定义语音指令功能

## 场景标签

`语音 Agent` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3:  A Python-based virtual assistant using Gemini AI. This assistant is capable of voice recognition, text-to-speech, f
> L38: # Virtual Assistant with Gemini AI
> L110:      genai.configure(api_key="Your_Own_API_KEY_FOR_GEMINI_AI")  # Replace with your actual API key

## 星数曲线

```mermaid
xychart-beta
    title "suryanshsk/Python-Voice-Assistant-Suryanshsk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-29 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3cdc93c9f5ba` · [字段定义](../../DATASET.md)*
