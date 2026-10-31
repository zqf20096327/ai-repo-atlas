# ROOT94-MAX/DiscordAITranslator

⭐ 28 · JavaScript · GPL-2.0 · 推送 2026-09-19 · [GitHub](https://github.com/ROOT94-MAX/DiscordAITranslator) · 个人维护 · 中文 README

**Discord 频道级 AI 翻译插件：收发消息与历史消息自动翻译**

BetterDiscord 平台的 Discord 翻译插件，需搭配 BDFDB Library 运行，以单文件 .plugin.js 安装。功能覆盖频道级自动翻译（每频道可设语言并覆盖主供应商）、发送前翻译、历史消息补翻、手动翻译单条消息、转发快照/回复/embed/线程标题翻译，以及术语与代码式文本的原文保护。翻译由外部供应商完成：默认 Google Free 免密钥，另支持 Google Cloud、Azure、DeepL、DeepSeek、Gemini、百度及自定义 OpenAI 兼容端点（含 Ollama 协议）。已知限制：依赖 Discord 非公开内部结构，客户端更新后可能需重新适配。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 频道级翻译控制，每频道可独立设置语言与主供应商
- 支持 8 类翻译供应商及自定义 OpenAI 兼容端点（含 Ollama、Gemini、Anthropic 协议）
- 历史消息批量补翻与主备供应商切换
- 原文保护机制保留术语、代码、剧透等文本

## 适用场景

- 在跨语言 Discord 社区里自动翻译收到的频道消息
- 发送消息前翻译成目标语言并可附带原文
- 回看频道历史时按范围批量补翻已加载消息

## 场景标签

 · 领域:聊天工具/翻译

## 证据(README 行号)

> L12: 一款 BetterDiscord 翻译插件，支持频道级收到消息翻译、发送前翻译、历史补翻、手动操作、转发消息和受保护文本。
> L64: |`deepseek`|DeepSeek|API Key|支持 AI 翻译、批量和决策模式|
> L65: |`gemini`|Google Gemini|API Key|原生 `generateContent` 接口|

## 星数曲线

```mermaid
xychart-beta
    title "ROOT94-MAX/DiscordAITranslator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4927b1eabe51` · [字段定义](../../DATASET.md)*
