# Nhqvu2005/AntibridgeTelegram

⭐ 19 · JavaScript · MIT · 推送 2026-07-25 · [GitHub](https://github.com/Nhqvu2005/AntibridgeTelegram) · 个人维护 · 中文 README

**通过 Telegram 远程控制 Antigravity IDE 内 AI Agent 的工具**

基于 Node.js 的桥接工具：通过 Telegram Bot 向 Antigravity IDE 内的 AI Agent 发送消息并接收回复，借助 Chrome DevTools Protocol 注入命令，无需抢占鼠标或最小化窗口。支持查看 Claude/Gemini/GPT 模型配额及变化历史、切换模型、截图、切换会话、浏览文件打开项目、运行 workflows 与 skills、远程结束进程等功能。需 Node.js v18+ 与开启调试端口的 Antigravity IDE 配合使用，为非官方工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Telegram 与 Antigravity 双向聊天，更新合并在单条消息中
- 通过 CDP 注入命令，不抢占鼠标、不最小化窗口
- 配额监控（Claude/Gemini/GPT）与每 5 分钟自动检测、变化记录
- 远程切换模型/会话、浏览文件打开项目、运行 workflows 与 skills

## 适用场景

- 在手机上通过 Telegram 与 Antigravity IDE 内的 AI Agent 对话
- 远程查看和管理 AI 模型配额使用情况
- 不在电脑前时远程打开项目、运行 workflow 并监控日志

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: > Control Antigravity IDE remotely via Telegram — Chat with AI, monitor quotas, manage projects, and more.
> L13: |🔧 **CDP Injection**|Commands via Chrome DevTools Protocol — no mouse stealing, no window minimizing|

## 星数曲线

```mermaid
xychart-beta
    title "Nhqvu2005/AntibridgeTelegram 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e2e4cabe0748` · [字段定义](../../DATASET.md)*
