# qingpingwang/remote-claude-code

⭐ 35 · Python · 推送 2026-01-28 · [GitHub](https://github.com/qingpingwang/remote-claude-code) · [官网](https://wangqingping.top/blog/post/remoteClaudeCode) · 个人维护 · 中文 README

**将 Claude Code 接入飞书的本地电脑操作机器人**

通过飞书长连接 WebSocket 将 Claude Code（本地 CLI）接入飞书聊天，实现本地电脑助手：可读写文件、执行 Shell/Python 脚本、开关应用程序、执行 Git 与包管理操作。每个聊天窗口（私聊/群聊）拥有独立上下文，群聊成员共享同一上下文，SQLite 持久化会话，重启后可继续对话。基于 Python 与 claude-agent-sdk，模块化设计支持替换为其他 Agent 后端（OpenAI Assistants、LangChain、Ollama 等）。单文件即可运行，无需公网域名。

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

- 每个聊天窗口独立上下文，SQLite 持久化，群聊共享上下文
- 通过 Claude Code 执行本地命令、文件操作与 Git 等开发任务
- 飞书长连接 WebSocket，无需公网域名
- 实现 chat_sync 函数即可替换/扩展后端 Agent

## 适用场景

- 在飞书群聊中共享上下文使用本地电脑助手
- 通过 @机器人 远程执行本地脚本与文件操作
- 团队成员多人同时使用互不干扰的开发助手

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L3: 将 Claude Code 接入飞书，实现本地电脑助手功能。
> L22: - 文件读写、创建、删除
> L44: - 使用 Claude Code，可执行本地命令、操作文件

## 星数曲线

```mermaid
xychart-beta
    title "qingpingwang/remote-claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `412739749bc9` · [字段定义](../../DATASET.md)*
