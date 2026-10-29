# KarryViber/Orb

⭐ 65 · JavaScript · MIT · 推送 2026-05-14 · [GitHub](https://github.com/KarryViber/Orb) · 个人维护

**包裹 Claude Code CLI 的多配置消息外壳：路由、记忆与 Slack 集成**

Orb 是围绕 Claude Code CLI 的消息路由层：从平台适配器（当前仅 Slack Socket Mode）接收消息，按配置文件路由，为每个线程启动或复用一个 Claude Code CLI 会话并回传结果，不替换其运行时。提供多配置隔离（独立 scripts/workspace/data 目录）、本地 SQLite 全息长期记忆（事实抽取、信任评分、衰减）、FTS5 文档全文检索、每配置 cron 调度、MCP 权限审批中继与四层 CLAUDE.md 提示架构。自进化 cron 拆为机械/LLM/渲染三阶段流水线。需 Node.js 18+、Python 3.11+、已认证的 Claude Code CLI 与 Slack 应用。v0.6 移除了 WeChat 适配器，其他平台尚未实现。

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

- 多配置隔离，每配置独立 scripts/workspace/data 目录
- 本地 SQLite 全息长期记忆：事实抽取、信任评分、矛盾处理
- DocStore 全文检索（SQLite FTS5）与项目 slug 推断
- MCP 权限中继：将 Claude Code 审批请求转到 Slack 卡片

## 适用场景

- 在 Slack 中与 Claude Code 会话并保持每线程会话复用
- 为不同用途隔离多个 Claude 工作配置与记忆
- 定时运行 cron 任务并把结果回传到 Slack

## 场景标签

`Agent 记忆` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: > A multi-profile messaging shell around Claude Code CLI.
> L9: Orb receives messages from a platform adapter, routes them to the right profile, starts or resumes a per-thread Clau
> L21: - Orb stays outside the agent runtime. It handles message routing, context assembly, profile boundaries, cron orche

## 星数曲线

```mermaid
xychart-beta
    title "KarryViber/Orb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-29 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7fa8ef88e1a5` · [字段定义](../../DATASET.md)*
