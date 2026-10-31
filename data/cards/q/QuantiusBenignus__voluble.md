# QuantiusBenignus/voluble

⭐ 16 · JavaScript · GPL-3.0 · 推送 2026-07-16 · [GitHub](https://github.com/QuantiusBenignus/voluble) · [官网](https://extensions.gnome.org/extension/6849/voluble/) · 个人维护

**朗读 GNOME 通知与选中文本的扩展，附本地 LLM 摘要/翻译/校对**

GNOME Shell 扩展加配套 zsh 脚本：拦截桌面通知或鼠标选中文本，经 fasttext 检测语言后用 Piper 神经 TTS 以对应语言语音模型读出。AI 功能通过本地 LLM 实现（Gemma 等 GGUF 模型，优先走 localhost 的 OpenAI 兼容服务器，失败回退 llama-completion CLI），支持摘要、翻译、解释与校对模式（校对结果写入剪贴板并语音播报简报）。面向 Linux 桌面用户，需手动安装系统依赖、Piper 语音模型与推理引擎，配置位于脚本内 USER BLOCK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通知与选中文本经 fasttext 语言检测后自动切换 Piper 语音模型
- 本地 LLM 摘要/翻译/解释/校对，优先本地服务器、回退 CLI
- 校对模式返回 JSON，改正文本入剪贴板、简报语音播报
- 可选 sox / Speech-Dispatcher 音频后端与 Joplin 任务播报

## 适用场景

- 不看屏幕时用语音接收桌面通知内容
- 选中外文文本让本地 LLM 翻译或摘要后读给我听
- 选中段落做校对并把修正文本粘贴回原文

## 场景标签

`语音合成` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L13: |**Human‑like voice for GNOME notifications**|Uses the lightweight neural TTS engine **Piper** for good-quality (fo
> L18: |**Summarise selected text** (`voluble -s`)|Sends the highlighted text to a local LLM (Gemma 4‑E4B, Gemma 3‑4B, etc
> L118: 1. **Voluble GNOME extension** intercepts a notification or a mouse‑selection and writes the text to `$XDG_RUNTIME

## 星数曲线

```mermaid
xychart-beta
    title "QuantiusBenignus/voluble 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e5bb165aed8b` · [字段定义](../../DATASET.md)*
