# frankbria/parallel-cc

⭐ 14 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/frankbria/parallel-cc) · 个人维护

**协调多 Claude Code 会话并行工作的 git worktree 工具**

面向同时运行多个 Claude Code 会话的开发者：自动为每个会话创建隔离 git worktree，通过 SQLite 跟踪会话、心跳检测与自动清理，并提供合并检测、冲突预检、文件独占/共享声明与 AST 语义冲突分析。另支持在 E2B 云沙箱中运行 Claude Code（单任务最长 1 小时，API key 或 OAuth 双认证），v2.1 起可多任务并行（默认并发 3），支持 Git Live 模式直接推送分支并用 gh CLI 创建 PR。需 Node.js 20+、gtr、jq，通过 git clone 源码脚本安装并构建 TypeScript。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动创建/清理 git worktree 隔离并行 Claude Code 会话
- SQLite 会话跟踪、心跳检测与合并/冲突管理（含 AST 语义冲突分析）
- E2B 云沙箱自主执行 Claude Code，单任务最长 1 小时
- v2.1 多任务并行沙箱执行（默认并发 3，可配置，支持 fail-fast）

## 适用场景

- 同一仓库开多个终端跑 Claude Code 而不互相冲突
- 把长任务交给 E2B 沙箱自主执行并自动建 PR
- 多任务并行沙箱批量执行后查看汇总报告

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: > Coordinate parallel Claude Code sessions using git worktrees + E2B cloud sandboxes for autonomous execution.
> L57: When you open multiple Claude Code sessions in the same repository, they can step on each other:
> L65: `parallel-cc` automatically detects when you're starting a parallel session and creates an isolated git worktree fo

## 星数曲线

```mermaid
xychart-beta
    title "frankbria/parallel-cc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `586d3ec39bff` · [字段定义](../../DATASET.md)*
