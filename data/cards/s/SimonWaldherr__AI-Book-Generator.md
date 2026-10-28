# SimonWaldherr/AI-Book-Generator

⭐ 64 · JavaScript · GPL-3.0 · 推送 2026-03-16 · [GitHub](https://github.com/SimonWaldherr/AI-Book-Generator) · [官网](https://simonwaldherr.github.io/AI-Book-Generator/) · 个人维护

**浏览器端 AI 图书生成器：多模型自动写整本书**

纯浏览器运行的图书生成工具：接入 OpenAI GPT、Anthropic Claude、Google Gemini 多家模型，支持一键 Agent 模式自主生成书名、概念、章节大纲与全部章节内容，或分步手动控制（概念→大纲→章节）。附 OpenAI Images API 封面生成，导出 TXT/HTML/Markdown/JSON/PDF 格式。API key 存于浏览器 localStorage（base64 编码），仅发送至对应提供商。本地用 python http.server 或 npm start 运行，无额外依赖；仓库自述为 proof of concept。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多 LLM 支持：OpenAI GPT、Anthropic Claude、Google Gemini
- Agent 模式一键自动生成整本书（书名/概念/大纲/章节）
- 章节逐字流式生成（OpenAI Chat API）
- 导出 TXT/HTML/Markdown/JSON/PDF，项目自动保存至浏览器本地存储

## 适用场景

- 用 AI 从零生成完整书稿初稿
- 分步控制概念、大纲与章节的写作过程
- 生成书籍配图封面并多格式导出

## 场景标签

`AI 写作` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L6: - **Multi-LLM Support** — OpenAI GPT (4o, o4-mini, GPT-5), Anthropic Claude (3.5 Sonnet, 3.5 Haiku, Opus, Sonnet 4.5
> L7: - **Agent Mode** — One-click "Generate Complete Book" button that autonomously generates title suggestions, book con

## 星数曲线

```mermaid
xychart-beta
    title "SimonWaldherr/AI-Book-Generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-28 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7bb566e9ad10` · [字段定义](../../DATASET.md)*
