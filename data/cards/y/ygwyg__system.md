# ygwyg/system

⭐ 297 · TypeScript · 推送 2026-01-31 · [GitHub](https://github.com/ygwyg/system) · [官网](https://system.surf) · 个人维护

**自托管 AI 助手：通过对话远程控制你的 Mac**

SYSTEM 是部署在自有基础设施上的 AI 助手，用自然语言操控 macOS：播放音乐、管理提醒/日历/备忘录、调节系统设置、运行 Apple 快捷指令与 Raycast 扩展、执行白名单 shell 命令。架构分三层：Cloudflare Workers 上运行 Claude 驱动的 Agent（含调度与记忆），Mac 本地 Bridge 执行命令，桌面 App 负责管理并常驻菜单栏。需 macOS、Anthropic API key；桌面版从 releases 下载安装，CLI 走 git clone + npm 流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言控制音乐/提醒/日历/系统设置/文件/快捷指令等
- Agent（Cloudflare Workers + Claude）+ 本地 Bridge + 菜单栏桌面 App 三层架构
- 端点认证、shell 命令白名单、可选 Cloudflare Access 零信任
- 需授予辅助功能、屏幕录制、自动化三项 macOS 权限

## 适用场景

- 出门在外通过对话远程操作家里的 Mac
- 用一句话完成提醒、日程、备忘和系统设置
- 让 AI 代跑 Apple 快捷指令和 Raycast 扩展

## 场景标签

 · 领域:桌面自动化/AI 助手

## 证据(README 行号)

> L5: SYSTEM is a self-hosted AI assistant that controls your Mac. Talk to it naturally—play music, manage reminders, run 
> L56: - **Agent** (brain): Cloudflare Worker with Claude AI, scheduling, memory

## 星数曲线

```mermaid
xychart-beta
    title "ygwyg/system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 296 --> 298
    line [297, 297]
```

2026-10-18 297 → 2026-10-23 297（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3511459ac4b5` · [字段定义](../../DATASET.md)*
