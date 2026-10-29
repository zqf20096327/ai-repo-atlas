# emreyilmaz46/clicky_windows

⭐ 25 · C# · MIT · 推送 2026-04-10 · [GitHub](https://github.com/emreyilmaz46/clicky_windows) · 个人维护

**Windows 11 语音 AI 屏幕助手：说话提问，蓝点指向屏幕元素**

Farzaa macOS 版 Clicky 的 Windows 移植，用 .NET 8 + WPF 从零重实现。按住热键说话后，应用截取屏幕、经 AssemblyAI 实时转写，发送给 Claude，用 Computer Use API 定位所询问的屏幕元素，蓝色圆点以贝塞尔弧线飞至该位置，并通过 ElevenLabs TTS 语音回答；保留最近 10 轮对话上下文。无窗口无 UI，仅托盘图标与悬浮圆点。需 Anthropic、ElevenLabs、AssemblyAI 三个 API key。提供单文件 exe 预构建二进制，也可 dotnet build 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude Computer Use API 像素级定位屏幕元素并以蓝点指示
- AssemblyAI 流式语音转写 + ElevenLabs TTS 语音回答
- 可配置全局热键（默认 Ctrl+Shift+Space）的按键说话交互
- 单文件 .exe，无需安装器，多显示器感知

## 适用场景

- 按住热键用语音询问屏幕上的元素并获得指向与语音回答
- 在 Windows 11 上以悬浮蓝点形式获得后台 AI 伴随助手

## 场景标签

`语音 Agent` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L11: Hold a hotkey, speak a question or command. Clicky captures your screen, transcribes your voice, sends everything t
> L13: - **Points to the exact element** on screen you asked about — a blue dot flies there with a smooth easing animation
> L29: - **Precision pointing** using Claude's Computer Use API — the dot flies to the detected element with a smooth bezi

## 星数曲线

```mermaid
xychart-beta
    title "emreyilmaz46/clicky_windows 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24", "2026-10-29"]
    y-axis "stars" 22 --> 26
    line [23, 24, 25, 25]
```

2026-10-18 23 → 2026-10-29 25（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `87f2625c5ce6` · [字段定义](../../DATASET.md)*
