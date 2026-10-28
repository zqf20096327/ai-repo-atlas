# weenable/openecho

⭐ 24 · TypeScript · MIT · 推送 2026-04-03 · [GitHub](https://github.com/weenable/openecho) · 个人维护 · 中文 README

**macOS 本地语音助手：快捷键语音转文字/翻译/问答/备忘**

面向 macOS（Apple Silicon）用户的桌面语音工具：按全局快捷键说话，本地运行的 Whisper 完成语音识别，文字经整理后粘贴到光标所在应用。提供五种模式：输入、翻译、语音提问（浮窗显示 AI 回答）、结构化备忘和语音合成（本地 Kokoro 或 OpenAI 兼容远程 TTS）。LLM 为可选配置，基础语音转文字可离线使用；音频不出设备。通过 Releases 页面的 .dmg 安装，也可用 Node.js 与 Rust 工具链从源码构建（Tauri）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 本地语音识别，音频不出设备
- 单一快捷键覆盖输入/翻译/提问/备忘/语音生成五种模式
- LLM 与远程 TTS 为可选，OpenAI 兼容 API 接入
- 本地 TTS 采用 Kokoro，可离线运行

## 适用场景

- 在任何应用中用语音输入整理后的文字
- 语音提问并即时获得 AI 回答浮窗
- 口述想法后生成可编辑的结构化备忘
- 将文字转为语音并保存音频文件

## 场景标签

`语音识别` `语音合成` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: OpenEcho is a macOS desktop app that turns your voice into polished text, translations, answers, and structured memo
> L29: - **Privacy first** — Whisper runs locally. Your voice stays on your Mac.
> L30: - **One shortcut, five modes** — Input, Translate, Question, Memo, Voice Generate. No app switching.

## 星数曲线

```mermaid
xychart-beta
    title "weenable/openecho 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `c8f5224cd7a5` · [字段定义](../../DATASET.md)*
