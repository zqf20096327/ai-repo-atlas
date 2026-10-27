# 0pen-Sourcer/Hearth

⭐ 32 · Python · MIT · 推送 2026-08-28 · [GitHub](https://github.com/0pen-Sourcer/Hearth) · [官网](https://get-hearth.vercel.app/) · 个人维护

**本地优先的 AI 助手框架，可实际操作你的 Windows 电脑**

本地优先的 AI harness，内置助手 JARVIS。它控制真实的 Windows PC：读写文件、运行 PowerShell、打开应用、驱动可观看的真实浏览器会话、通过无障碍快照点击和输入桌面元素，并提供跨会话记忆、语音、提醒、Telegram/Discord 手机接入、可分享的 skill 系统与子 agent 团队。模型侧自带 llama.cpp 服务器，或自动检测 LM Studio/Ollama 等 OpenAI 兼容端点。当前 v0.7.5-preview，Windows 为支持平台，macOS/Linux 从源码运行且桌面控制暂限 Windows。

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

- 桌面控制：无障碍快照精确读取按钮/菜单并按名称操作，动作前逐项询问
- 自包含记忆：按事实存储、自动归档冷事实、召回后回热
- skill 一行命令安装/分享（/skill install owner/repo）
- 四种接口：CLI、桌面/Web 应用、headless bridge、MCP server

## 适用场景

- 在本机用自然语言让 AI 代为整理文件、操作浏览器和桌面应用
- 数据不出本机的前提下运行带记忆的私人助手
- 通过 Telegram/Discord 从手机指挥电脑上的 agent

## 场景标签

`GUI 自动化` `浏览器自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L3:  A local JARVIS that actually runs your computer.
> L22: **Hearth is the fourth.** A local-first operator that runs on the model you already have and controls your actual W
> L26: Reach it however you work: a terminal **CLI**, a desktop/web **app**, a headless **bridge**, or an **MCP server**.

## 星数曲线

```mermaid
xychart-beta
    title "0pen-Sourcer/Hearth 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `f1db49bd3e3b` · [字段定义](../../DATASET.md)*
