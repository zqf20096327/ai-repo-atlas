# Hamza-Abili/opencode-telegram-notify

⭐ 3 · TypeScript · MIT · 推送 2026-11-19 · [GitHub](https://github.com/Hamza-Abili/opencode-telegram-notify) · [官网](https://www.npmjs.com/package/@hamzaabili/opencode-telegram-notify) · 个人维护

**OpenCode 的 Telegram 通知插件：手机上点按钮批权限**

面向使用 OpenCode 编码代理的开发者的 Telegram 通知插件，同时兼容 OpenCode v1（legacy 入口）与 v2（{id, setup} 入口）。提供权限请求的仅点击内联按钮（Allow once/Always allow/Reject，映射 client.permission.reply）、v2 表单问题的按钮作答、完成/失败/取消等生命周期通知（v2 附 token 与费用用量）、/start /status /setup /stop /help 命令菜单。声明零运行时依赖、单轮询文件锁、事件去重与 token 脱敏；支持 en/it/zh 通知语言。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 权限请求以 tap-only 内联按钮呈现，声明从不自动批准
- 兼容 OpenCode v1 与 v2 两种插件契约，共享同一核心
- 零运行时依赖，单轮询锁与事件去重支持多实例
- 通知语言支持 en/it/zh，token 脱敏与隐藏命令参数选项

## 适用场景

- 在服务器或工作站上运行 OpenCode，手机上通过 Telegram 批准权限请求
- 会话完成或失败时在 Telegram 收到通知与用量摘要
- 静默后台/定时任务会话的通知，只保留交互会话的消息

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: Telegram notifications for [OpenCode][] — **v1 and v2** — with **tap-only
> L87: - OpenCode **v2** (tested on 2.3.2; the 2.0.x line is also supported) or **v1.18+**

## 星数曲线

```mermaid
xychart-beta
    title "Hamza-Abili/opencode-telegram-notify 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-15 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `4f60229e500f` · [字段定义](../../DATASET.md)*
