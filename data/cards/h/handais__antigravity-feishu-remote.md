# handais/antigravity-feishu-remote

⭐ 5 · JavaScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/handais/antigravity-feishu-remote) · [官网](https://github.com/handais/antigravity-feishu-remote#readme) · 个人维护 · 中文 README

**通过飞书 WebSocket 远程控制本机 Antigravity 的插件**

Node.js 编写的 Antigravity（`agy` CLI）飞书远程控制插件：以 WebSocket 长连接桥接飞书机器人与本机守护进程，提供 CardKit 2.0 流式卡片输出、话题群多会话并发隔离、25+ 斜杠指令、云文档读写、PreToolUse 高危命令审批钩子与 MCP 工具集，并支持桌面与手机间会话接力及插件自身的远程热更新/回滚。凭证保存在用户主目录独立配置目录。macOS 完整实测，Linux/原生 Windows 为实验性支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 飞书 WebSocket 长连接守护进程，免公网 IP 与内网穿透
- CardKit 2.0 打字机流式卡片与话题群多任务并发隔离（默认上限 4）
- PreToolUse 高危命令飞书审批钩子，超时 Fail-Closed 拒绝
- 手机端远程修改插件源码，/reload 双检热重启与 /rollback 快照回滚

## 适用场景

- 出门在外用手机飞书指挥家里电脑上的 Antigravity 任务
- 高危 Shell 命令远程执行前在飞书里审批确认
- 在话题群里并行开多个独立会话跑不同任务
- 桌面任务完成后自动推送到飞书并可在手机上接力

## 场景标签

`AI 助手` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L13: > 通过飞书 **WebSocket 长连接**，让你在手机（安卓 / iOS）或桌面飞书里随时指挥本机 **Antigravity (`agy`)**——实时看 **CardKit 2.0 打字机流式卡片**、多话题并发执行、拦
> L167: 插件涵盖 **飞书 WebSocket 守护进程**、**25+ 飞书斜杠指令与交互卡片**、**`feishu-remote-tools` MCP 工具集** 以及 **`Stop` / `PreToolUse` 双生命周期 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `a4cd81aafdcd` · [字段定义](../../DATASET.md)*
