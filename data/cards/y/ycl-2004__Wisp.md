# ycl-2004/Wisp

⭐ 169 · Swift · MIT · 推送 2026-11-20 · [GitHub](https://github.com/ycl-2004/Wisp) · 个人维护 · 中文 README

**macOS 菜单栏 AI 助手：按需读取屏幕与浏览器上下文回答问题**

常驻菜单栏的原生 macOS 应用，按快捷键唤起面板前先记录前台应用，可截取当前窗口或全屏，并从支持的浏览器读取 URL、标题、选中文本与页面正文，免去跨应用复制上下文。模型连接由用户自选：OpenAI 兼容端点、本地 Ollama 或 Agent CLI（Codex、Antigravity、Claude Code）。附带实时字幕（Apple 本地识别或 Soniox）、Quick Ask/Ask About Screen、屏幕共享隐藏等功能。分发为 Universal 2 zip 包，未公证，需手动放行；要求 macOS 26.0+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 按需截屏并读取 9 种浏览器页面的 URL、标题、选中文本与正文
- 三种模型接入：OpenAI 兼容端点（SSE 流式）、本地 Ollama、Agent CLI
- 会议实时字幕只听系统音频，支持 Quick Ask 与 Ask About Screen
- 本地优先：对话与页面快照存于本机，界面支持英文与简体中文

## 适用场景

- 写代码或看文档时直接就当前窗口内容向模型提问
- 会议中开启字幕，对方提问时按键结合屏幕内容快速得到可口头回答的答案
- 不愿把对话记录交给云服务时用本地 Ollama 运行

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5:  A native macOS AI assistant that reads your current screen and browser context when you ask.
> L31: It is a local-first desktop shell around the model provider you choose:
> L216: - **Cloud endpoint:** sends `chat/completions` requests with SSE streaming and

## 星数曲线

```mermaid
xychart-beta
    title "ycl-2004/Wisp 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-26"]
    y-axis "stars" 168 --> 170
    line [169, 169]
```

2026-11-08 169 → 2026-11-26 169（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `0c968ffd4ad8` · [字段定义](../../DATASET.md)*
