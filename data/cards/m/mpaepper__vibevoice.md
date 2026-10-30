# mpaepper/vibevoice

⭐ 157 · Python · 推送 2026-05-15 · [GitHub](https://github.com/mpaepper/vibevoice) · [官网](https://www.paepper.com/blog/posts/vibe-coding-with-vibevoice-fast-speech-to-text-for-any-app/) · 个人维护

**本地语音转文字听写工具，可在任意应用中输入语音文本**

基于 faster-whisper 本地 Whisper 模型的系统级听写工具：按住右 Ctrl 键说话、松开后将转写文本自动输入光标所在位置，适用于编辑器、浏览器、聊天等任何可输入的场景。另提供 AI 语音命令模式：按住 Scroll Lock 键说出指令，转录文本连同当前屏幕截图发送给本地 Ollama 多模态模型，回答流式键入系统。通过 git clone 源码运行，需 Python 3.13+，推荐 CUDA GPU，CPU 模式可在代码中启用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- faster-whisper 本地模型转写，无需 OpenAI API 付费
- 按住快捷键说话、松开即转写并自动输入任意应用
- AI 命令模式：语音+当前屏幕截图交由 Ollama 多模态模型处理并流式键入回答
- 通过环境变量配置激活键、模型与截图行为

## 适用场景

- 在任意应用中用语音代替键盘输入文字
- 通过语音向本地 LLM 提问并获取结合屏幕上下文的回答
- 本地离线语音听写，不依赖云端服务

## 场景标签

`语音识别` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L10: Simply run `cli.py` and start dictating text anywhere in your system:
> L14: 4. Watch as your spoken words are transcribed and automatically typed!
> L22: 3. The LLM receives your transcribed text and a screenshot of your current view

## 星数曲线

```mermaid
xychart-beta
    title "mpaepper/vibevoice 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 156 --> 158
    line [157, 157]
```

2026-10-18 157 → 2026-10-30 157（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `7bd1d3b80bba` · [字段定义](../../DATASET.md)*
