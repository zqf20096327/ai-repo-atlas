# Ike-li/claude-chat-mobile

⭐ 46 · JavaScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/Ike-li/claude-chat-mobile) · [官网](https://ike-li.github.io/claude-chat-mobile/) · 个人维护 · 中文 README

**自托管手机 Web UI：远程驾驶本机的 Claude Code CLI**

手机通过 PWA/浏览器经 Socket.io 连接本机 CCM Server，再经 Claude Agent SDK 驱动本机 claude CLI，复用同一份 CLAUDE.md、MCP、skills、登录与权限规则。提供工具审批卡、AskUserQuestion、锁屏推送、会话列表与续接、文件改动预览、/rewind 回退、额度用量查看等。支持任意网关/API key/Bedrock/Vertex 等 CLI 现有配置；单用户、单驾驶端，服务与数据留在本机。需 Node ≥ 20 与已可用的 claude CLI，从源码安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Agent SDK 驱动本机 claude CLI，复用 CLAUDE.md/MCP/skills/登录
- 工具审批、提问交互、后台任务完成无条件推送到锁屏
- 支持第三方网关、API key、Bedrock/Vertex 等现有 CLI 配置
- 设备信任审批、AUTH_TOKEN 启动前提、工作区显式放行的安全边界

## 适用场景

- 离开电脑时用手机继续驾驶终端里的 Claude Code 会话
- 在手机上处理工具审批与 AI 提问，避免任务空等
- 会把话记录与审计留在自己机器上的自托管远程访问

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L103: 手机 PWA / 浏览器 ↕ Socket.io ↕ CCM Server（本机） ↕ Claude Agent SDK ↕ 本机 claude CLI
> L31: * **手机上驱动的就是你电脑上那个 claude。** 通过 Agent SDK 驱动本机的 `claude` CLI，同一份 CLAUDE.md、MCP、skills、登录和权限规则。目标是终端里能做的事，手机上都能做。

## 星数曲线

```mermaid
xychart-beta
    title "Ike-li/claude-chat-mobile 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-31 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `37978ecf4dc0` · [字段定义](../../DATASET.md)*
