# chadwittman/typeroid

⭐ 27 · Swift · MIT · 推送 2026-10-20 · [GitHub](https://github.com/chadwittman/typeroid) · [官网](https://typeroid.xyz) · 个人维护

**macOS 菜单栏听写与 AI 文本改写工具**

Swift/AppKit 菜单栏应用：按住 fn 键本地 Whisper 听写并粘贴到光标处；输入两字符触发词调用所配置的模型完成文本修正（//）、提问（??）、翻译（;;）、数学换算（==）、总结回复草稿（\）与改写（||），>> 模式将提示词加全屏截图发给视觉模型并原位替换文本。支持 OpenAI、Anthropic、Google、Groq 或本地 Ollama，需自带 API key；API key 存入 macOS 钥匙串，无遥测、无账号，需 macOS 14+ 与辅助功能权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- fn 键本地 Whisper 听写，松开即粘贴到光标处
- 7 个两字符触发词：修文/提问/翻译/数学/总结/改写/屏幕提问
- 可接 OpenAI、Anthropic、Gemini、Groq 或本地 Ollama（无需 API key）
- 无遥测无账号，API key 加密存于钥匙串，敏感信息（SSN/卡号等）发送前拦截

## 适用场景

- 在任意应用里按键听写、直接落到光标位置
- 随手修正错字连发的随手消息或翻译、换算
- 对着屏幕截图提问，让 AI 看图并原位给出答案
- 复制长讨论后一键生成摘要与回复草稿

## 场景标签

`语音识别` `AI 写作` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: Hold fn, talk, release. What you said pastes at the cursor. Ums come out. The words stay yours.
> L119: 1. typeROID runs as a menu bar app (look for the `//` icon)
> L122: 4. Sends text, local transcript, or explicit screen context to your AI provider with a focused system prompt

## 星数曲线

```mermaid
xychart-beta
    title "chadwittman/typeroid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e6da598e5886` · [字段定义](../../DATASET.md)*
