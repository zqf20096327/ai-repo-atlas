# dzotyara/ai-forge

⭐ 3 · JavaScript · 推送 2026-11-21 · [GitHub](https://github.com/dzotyara/ai-forge) · 个人维护 · 中文 README

**把 Claude Code/Codex 审批与问答转发到 Discord/Telegram 远程操作**

以 Claude Code 插件与 Codex 插件形式安装的工具，在本地运行一个后台服务，把 agent 会话中的权限请求、选择题与对话内容推送到 Discord 或 Telegram，用户通过按钮与回复远程批准、应答并驱动会话。支持每个会话独立频道/话题、Boss 多会话分发、多设备在席统计、免打扰时段与安全设置；token 仅存本地，无服务端与账号。需 Claude Code 与 Node.js 22+，在席检测仅 macOS 可用。

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

- 权限请求与问题以 Allow/Deny 按钮送达 Discord/Telegram，一键批准
- 每个会话对应私有频道或 forum topic，文本回复唤醒会话
- Boss 会话将任务拆分到多个后台会话并汇报结果
- 全部本地运行：无服务端、无账号，bot token 不离开本机

## 适用场景

- 给 Claude Code 布置大任务后离开电脑，在手机上批准命令继续运行
- 在 Discord/Telegram 里远程回答 agent 的提问并驱动会话
- 用 Boss 把一个任务拆给多个后台会话并行执行
- 多台设备上统计并查看 Claude Code/Codex 会话的运行状态

## 场景标签

 · 领域:开发者工具/AI 编程辅助

## 证据(README 行号)

> L5:  AI Forge turns Discord and Telegram into the control room for Claude Code.
> L74: Everything runs on your machine: a small background service and the plugin's hooks. There is no AI Forge server and
> L99: claude plugin marketplace add dzotyara/ai-forge


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `89c355ef0edf` · [字段定义](../../DATASET.md)*
