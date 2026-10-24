# bleeeet/TermiPet

⭐ 85 · Swift · Apache-2.0 · 推送 2026-09-16 · [GitHub](https://github.com/bleeeet/TermiPet) · [官网](https://github.com/bleeeet/TermiPet/releases/tag/v0.1) · 个人维护 · 中文 README

**macOS 终端桌宠：陪伴 Claude Code 并查看状态与用量**

以 Swift 编写的 macOS 菜单栏桌面宠物应用，面向终端用户与 AI 编程工具用户。功能包括：识别 7 种终端并显示窗口标题与输出摘要的终端预览、内置并可自定义的 Claude Code 快捷指令面板、通过 Claude Code Hook 接收思考/工具调用/等待授权等状态并在卡片上显示 Allow/Deny、读取 Claude Code/Codex/GitHub Copilot 轻量用量、番茄钟，以及支持本地 Ollama 或 OpenAI/Gemini/兼容 API 的宠物聊天。隐私上密钥存 macOS 钥匙串，Hook 事件只发本机 127.0.0.1。终端读取与自动输入依赖 macOS 辅助功能权限。提供 zip 安装包、一行脚本、Homebrew cask 与源码构建四种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude Code Hook 同步思考/工具调用/授权状态，卡片内可直接 Allow/Deny
- 读取 Claude Code / Codex / GitHub Copilot 轻量用量信息
- 宠物聊天支持本地 Ollama 及 OpenAI/Gemini/OpenAI-compatible API，密钥存钥匙串
- 识别 7 种终端；支持导入 Petdex/Codex 兼容宠物资源包

## 适用场景

- 写代码时通过悬浮宠物查看 Claude Code 当前状态与等待授权的调用
- 一键向终端发送常用 Claude Code 命令或切换项目目录
- 用本地 Ollama 模型和桌面宠物聊天，不依赖外部 API

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L37: TermiPet 是一个悬浮在 macOS 桌面上的宠物助手。它面向终端用户和 AI 编程工具用户，帮你**查看终端状态**、**发送常用命令**、**观察 Claude Code / Codex / GitHub Copilot
> L41: 它不是单纯的桌面装饰，而是一个**轻量的工作流入口**：平时安静待在屏幕边缘，需要时展开工具栏、状态卡片、快捷命令、番茄钟和聊天窗口。
> L66: TermiPet 会把 Claude Code 等 AI 编程工具的状态整理成悬浮卡片，显示当前项目、执行动作、工作目录和 Hook 来源。遇到需要授权的 Bash 或工具调用时，也可以在卡片里直接看到 Allow / Deny 

## 星数曲线

```mermaid
xychart-beta
    title "bleeeet/TermiPet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 83 --> 86
    line [84, 85, 85]
```

2026-10-18 84 → 2026-10-24 85（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e20d110fea19` · [字段定义](../../DATASET.md)*
