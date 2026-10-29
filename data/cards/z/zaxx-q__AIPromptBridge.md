# zaxx-q/AIPromptBridge

⭐ 19 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/zaxx-q/AIPromptBridge) · 个人维护

**系统级 AI 助手托盘应用：全局热键编辑文本、截屏识别、音频转写、TTS**

Windows/Linux 系统托盘应用，通过全局热键在任意应用中调用 AI：选中文本做解释/校对/改写/自定义 Prompt，截屏区域做 OCR、描述、代码解释与图像对比，录制麦克风或系统音频做带时间戳与说话人识别的转写，并用 Gemini TTS 模型生成语音（30 种预置音色）。支持 Gemini、Claude、OpenAI、OpenRouter、xAI、Mistral、Cohere 及 OpenAI 兼容端点，提供连接配置、密钥轮换与批量文件处理。限制：Linux 仅适配 niri/Sway/Hyprland 等 Wayland 组合，不支持 KDE/GNOME/X11。

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

- Ctrl+Space 在任意应用中对选中文本执行校对/改写/问答等操作
- 截屏 OCR 与分析、音频录制转写（带说话人识别）
- Gemini TTS 生成语音，30 种音色、双说话人、WAV 导出
- 多 provider 连接配置与 API key 自动轮换重试

## 适用场景

- 在浏览器、IDE、Word 等任意应用中快捷润色或解释文本
- 截取屏幕区域做 OCR 提取或代码讲解
- 录制会议音频转成带说话人标记的转写与摘要
- 把文本批量转成语音导出 WAV

## 场景标签

`AI 助手` `语音合成` `语音识别` `OCR` · 领域:对话与助手

## 证据(README 行号)

> L3: **AIPromptBridge** is a system-wide app that brings AI assistance to your fingertips. Use global hotkeys to edit tex
> L103: - **Multi-provider support** - Google Gemini, Anthropic Claude, OpenAI, OpenRouter, xAI (Grok), Mistral, Cohere, a

## 星数曲线

```mermaid
xychart-beta
    title "zaxx-q/AIPromptBridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `1be0b6282398` · [字段定义](../../DATASET.md)*
