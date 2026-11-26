# dzotyara/aukalo

⭐ 3 · JavaScript · 推送 2026-11-25 · [GitHub](https://github.com/dzotyara/aukalo) · 个人维护 · 中文 README

**用 Discord/Telegram 远程批准并引导 Claude Code/Codex 会话**

Aukalo 是一个 Claude Code 插件与本地后台服务的组合：当 Claude Code 或 Codex 会话触发权限请求、选择题或需要用户输入时，把请求以按钮消息转发到 Discord 频道或 Telegram 话题，用户点按 Allow/Deny 或直接回复文本即可让会话继续；每个会话对应独立频道/话题，可远程接收会话发送的文件，并有 Boss 会话在主频道拆分任务、启动后台会话。全部在本地运行，无独立服务器与账号；在场检测仅支持 macOS，其他系统视为离开。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 权限请求以 Allow/Deny 按钮送达 Discord/Telegram，聊天回复可唤醒会话
- Boss 会话在主频道拆分任务并启动后台会话（claude -p）
- 本地运行，无服务器与账号，bot token 不离开本机
- 支持多设备在线状态汇总与 Codex 会话计数

## 适用场景

- 离开电脑时用手机批准 Claude Code 的命令执行请求
- 在 Telegram 话题里回复文本继续某个代码会话
- 用 Boss 把大任务拆给多个后台会话并行执行

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5:  Aukalo turns Discord and Telegram into the control room for Claude Code.
> L69:   A["Claude Code / Codex session"] -- "needs you" --> B["Aukalo hooks"]
> L76: Everything runs on your machine: a small background service and the plugin's hooks. There is no Aukalo server and n


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `621c696ebb6a` · [字段定义](../../DATASET.md)*
