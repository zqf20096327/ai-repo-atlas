# Chamanrajragu/claude-multi

⭐ 17 · JavaScript · MIT · 推送 2026-09-13 · [GitHub](https://github.com/Chamanrajragu/claude-multi) · [官网](https://purffle.com/claude-multi/) · 个人维护

**单窗口多账号运行 Claude Code 的桌面客户端，限额自动切换**

面向 Claude Pro/Max 订阅用户的免费开源桌面应用（Windows/macOS/Linux）：在一个窗口内添加最多 20 个 Claude 账号，账号触达 5 小时用量限制时自动切换到下一个可用账号并延续对话、重新下发被中断的指令；账号经 CLAUDE_CONFIG_DIR 目录隔离。支持 24/7 自动轮询循环、并行会话、实时冷却倒计时、上下文 token 检查器、@文件补全、内置约 40MB 离线语音模型听写。无需 API key，使用订阅登录，数据本地留存。运行前提为已安装 Node.js 18+ 与 Claude Code CLI。

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

- 账号达限额自动切换并延续对话、重新下发指令
- 最多 20 个账号经 CLAUDE_CONFIG_DIR 隔离，24/7 自动轮询
- 上下文检查器逐项显示 token 占用，含 auto-compact 与预算上限
- 内置约 40MB 离线语音转文字，无需联网与 API key

## 适用场景

- 我有多个 Claude Pro/Max 账号，想在同一窗口轮换使用而不用切换浏览器
- 让 Claude 在长任务上 24/7 连续运行，睡醒后查看结果
- 同时开多个项目的并行会话，各自独立账号与会话
- 查看上下文窗口里每个文件、工具、对话轮的 token 消耗

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L23: **Claude Multi** is a **free, open-source desktop app** for Windows, macOS, and Linux that lets you run **Claude Co
> L95: **Prerequisites:** Node.js 18+ and Claude Code CLI must be installed on your machine.
> L240: Each account gets its own `~/.claude-accounts/<id>/` directory — the officially documented `CLAUDE_CONFIG_DIR` mec

## 星数曲线

```mermaid
xychart-beta
    title "Chamanrajragu/claude-multi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b684f558ddc3` · [字段定义](../../DATASET.md)*
