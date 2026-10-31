# giulio-leone/harness-os

⭐ 24 · TypeScript · NOASSERTION · 推送 2026-05-17 · [GitHub](https://github.com/giulio-leone/harness-os) · [官网](https://www.giulioleone.com) · 个人维护

**自主 AI agent 的执行层：持久化、生命周期与编排框架**

TypeScript 编写的 agent 运行时基础设施：以 SQLite 为唯一事实源，管理任务状态机（pending→ready→in_progress→done/failed）、租约、检查点与不可变事件日志；自动解析任务依赖并提升队列，可选接入 mem0-mcp 提供跨会话语义记忆（不可用时降级运行）。提供 MCP 服务器注册、cron 调度注入器、Symphony 式多 agent 扇出编排（隔离 worktree、证据门）与 Next.js 仪表盘。自身不负责 LLM 推理与工具实现，宣称 agent 无关、支持 Codex/Copilot CLI 等宿主。要求 Node.js 22+，v2 旧库不迁移、打开即失败。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SQLite 规范状态层：租约/检查点/事件/任务状态，ACID 合规
- 任务状态机 + 依赖链自动提升 + 陈旧租约自动恢复
- Symphony 式多 agent 编排：每 issue 独立 worktree 与确定性证据门，无人工检查点
- 可选 mem0-mcp 语义记忆，不可用时优雅降级不污染规范状态

## 适用场景

- 让自主 agent 在崩溃后从检查点恢复并保留全部工作状态
- 多 agent 之间用租约与依赖链协调任务、避免重复认领
- 为团队的工作队列提供可审计的编排与健康监控仪表盘

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L25: A **Harness** is the missing execution layer. It is the infrastructure that wraps around AI agents to give them:
> L46: **HarnessOS** provides the foundational execution framework for advanced autonomous agents. It focuses strictly on 

## 星数曲线

```mermaid
xychart-beta
    title "giulio-leone/harness-os 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-31 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4d65dd193d8a` · [字段定义](../../DATASET.md)*
