# duanecilliers/openclaw-admin

⭐ 35 · TypeScript · 推送 2026-02-05 · [GitHub](https://github.com/duanecilliers/openclaw-admin) · 个人维护

**管理 OpenClaw 多 agent Discord 机器人的本地 Web 管理面板**

面向本地单用户的 Web 管理面板，用于管理运行 Discord 机器人 agent 的 OpenClaw 实例。功能包括：用 CodeMirror 6 编辑每个 agent 工作区文件（SOUL.md/USER.md 等）、按 agent 安装与移除技能（工作区/共享/内置三层优先级）、从 Discord API 拉取头像与频道名并显示账号到频道路由、cron 任务管理、只读配置查看（敏感字段掩码）与网关控制。后端直接读写 ~/.openclaw/openclaw.json，采用临时文件→备份→原子重命名的写入方式。无鉴权，仅限本地使用，需 Node.js 20+ 与已配置的 OpenClaw。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 agent 编辑工作区文件（SOUL.md 等 5 类），下次 agent 轮次生效
- 三层技能优先级（workspace/shared/bundled）浏览与安装移除
- Discord 头像/频道名拉取与账号→频道路由可视化
- 原子配置写入并保留 10 份时间戳备份

## 适用场景

- 统一管理多个 Discord persona bot 的工作区与技能
- 查看与调度各 agent 的 cron 定时任务
- 监控 OpenClaw 网关连接状态并重启

## 场景标签

 · 领域:AI agent 运维/管理工具

## 证据(README 行号)

> L5: Web-based admin dashboard for managing an OpenClaw instance with multiple agents. Built for local, single-user use.
> L11: - **Agent Management** — View all agents defined in `agents.list[]`. Edit per-agent workspace files (SOUL.md, USER.

## 星数曲线

```mermaid
xychart-beta
    title "duanecilliers/openclaw-admin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e5e133b2d356` · [字段定义](../../DATASET.md)*
