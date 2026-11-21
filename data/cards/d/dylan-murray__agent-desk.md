# dylan-murray/agent-desk

⭐ 5 · Python · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/dylan-murray/agent-desk) · 个人维护

**给开发者的本地编码 agent 工作台：并排运行与审查多个 agent**

本地工作区，用于在浏览器或 macOS 桌面上并排运行编码 agent：真实终端里运行 Claude Code、Codex、Grok、OpenCode、Pi、Cortex Code 及自定义 CLI，最多 16 个可调布局窗格；coordinator 可将任务拆分给多个 agent 并在统一收件箱回收结果；支持按 desk 隔离项目、模型路由按任务分配 worker、UI 上点选批注发给 agent、跨 agent 共享 skills，以及定时自动化运行。依赖 Python 3.11+ 与 Node.js 18+，仅支持 macOS/Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 并排终端运行多家编码 agent CLI，最多 16 窗格布局
- coordinator 拆分任务给多个 agent 并统一收件箱追踪
- UI 批注可直接发送给对应 agent，diff 审查内嵌窗格
- macOS 桌面应用与浏览器两种运行形态

## 适用场景

- 同时跑多个 Claude Code/Codex 会话管理不同项目
- 让 coordinator 把一项改动拆给多个 agent 并集中审查
- 通过批注对 agent 的 diff 提意见并回传
- 为周期性任务配置定时自动化运行

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: Agent Desk is a local workspace for coding agents. Run any coding agent side by
> L23: - 🧭 **Coordinators** that hand work to agents and track what comes back

## 星数曲线

```mermaid
xychart-beta
    title "dylan-murray/agent-desk 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-22", "2026-11-21"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-19 4 → 2026-11-21 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ff24075144c2` · [字段定义](../../DATASET.md)*
