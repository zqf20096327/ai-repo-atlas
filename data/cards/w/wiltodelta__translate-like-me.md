# wiltodelta/translate-like-me

⭐ 18 · Swift · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/wiltodelta/translate-like-me) · [官网](https://wiltodelta.com/projects/translate-like-me/) · 个人维护

**macOS 菜单栏应用：快捷键原位翻译/改写文本并本地听写**

面向 Mac 用户的菜单栏工具：按住快捷键在光标处本地听写（Whisper/Qwen3-ASR，离线可用、无需账号），选中文本按快捷键原位改写（按用户写作风格）或翻译（最多三个语言对，自动检测方向）。翻译与改写可选用应用内 MLX 本地模型（Gemma 系列），或通过官方 CLI 接入 Claude Code、Codex、Grok Build、Antigravity 并使用用户已有订阅。文本默认本地处理，应用无服务器与遥测。要求 macOS 15+ Apple silicon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地听写（Whisper/Qwen3-ASR），离线可用，无需账号或 API key
- 选中文文原位改写与翻译，按语言对自动检测方向，最多三对
- 翻译引擎可选应用内 MLX 本地模型或 Claude Code/Codex/Grok Build/Antigravity 官方 CLI
- 写作风格可自定义并可贯穿改写与翻译；应用无服务器、无遥测

## 适用场景

- 在任何应用中选中文本快捷键原位翻译或润色
- 按住快捷键语音听写并随后改写成完整消息
- 在无账号/API key 条件下离线完成听写与翻译

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L90: Dictation runs locally with Whisper or Qwen3-ASR, with no account or API key.
> L91: For translation and Rewrite, choose a local model or use Claude Code, Codex,

## 星数曲线

```mermaid
xychart-beta
    title "wiltodelta/translate-like-me 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `17ccd008843c` · [字段定义](../../DATASET.md)*
