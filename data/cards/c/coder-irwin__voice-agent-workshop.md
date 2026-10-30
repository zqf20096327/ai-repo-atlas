# coder-irwin/voice-agent-workshop

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/coder-irwin/voice-agent-workshop) · 个人维护

**本地开源语音 agent 工作坊：语音对话并执行浏览器操作**

面向学习者的工作坊起始项目：用 faster-whisper 做语音转文字，Ollama 本地 LLM 选择工具，Playwright 驱动浏览器执行操作（打开 YouTube、搜索、滚动、截图），Kokoro TTS 语音回复，全程本地运行、无需 API key。核心练习是向 app/tools/ 添加自定义 @tool 函数（约 300 行代码）。要求 Python 3.11/3.12、Ollama、ffmpeg、espeak-ng，约 8 GB 空闲内存，Windows 需 WSL2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- faster-whisper + Ollama + Playwright + Kokoro 全本地语音-行动管线
- 用 @tool 装饰器三步添加自定义工具，支持任意支持工具调用的本地模型
- 麦克风/语音文件/文字三种输入方式，同一管线
- 可配置 Chromium/Chrome/Edge/Firefox/WebKit 及持久化登录 profile

## 适用场景

- 学习如何搭建语音驱动的本地 AI agent
- 用语音命令控制浏览器播放音乐、搜索、截图
- 教学场景中让学生以添加一个工具作为首个 PR

## 场景标签

`语音 Agent` `浏览器自动化` `语音识别` `语音合成` · 领域:效率与自动化

## 证据(README 行号)

> L26: A normal voice assistant is **ears → brain → voice**. This one adds **hands**.
> L30:     U([🎤 You speak<br/>or upload / type]) --> E[👂 EARS<br/>faster-whisper<br/>speech → text]
> L31:     E --> B{🧠 BRAIN<br/>Ollama LLM<br/>+ list of tools}

## 星数曲线

```mermaid
xychart-beta
    title "coder-irwin/voice-agent-workshop 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-28 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `35cba6041c9d` · [字段定义](../../DATASET.md)*
