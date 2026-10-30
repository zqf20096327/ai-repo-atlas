# GobbyAI/gobby

⭐ 22 · Python · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/GobbyAI/gobby) · 个人维护

**本地守护进程：把任务交给多个 AI 编码 CLI，自主跑完产出 PR**

面向使用 Claude Code、Codex、Gemini CLI、Qwen CLI、Factory Droid 等编码 CLI 的开发者的本地守护进程（Python 3.13+，PostgreSQL 作为运行时枢纽，HTTP/Web UI/WebSocket 本地端口 + stdio MCP 服务器）。核心机制：确定性阶段清单调度（ideation 到 merge 的固定阶段流，由规则引擎在 mutex 下执行单一动作）、工具调用级的 hook 时间规则（可阻断/改写/注入上下文）、渐进式 MCP 发现、worktree/clone 隔离与阶段化审查门，最终以提交关联收尾形成 PR。声明本仓库由其自身构建流程生成（5K+ 提交）。配套 Rust 工具链（gobby-cli）需单独安装。Apache 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性阶段清单调度：心跳扫描任务，规则引擎在每任务 mutex 下执行单一有界动作
- hook 时间规则引擎：turn_start/before_tool/after_tool/turn_end 处可阻断、改写、注入上下文
- 跨 CLI 共享会话、任务账本、记忆与规则：任务可在 Claude Code 起始、Codex 认领、Droid 完成
- 渐进式 MCP 代理：仅在工具实际调用时拉取 schema
- 本地优先：数据库、转录、规则均留在本机，配套 Web UI 与 trace 查看器

## 适用场景

- 把一个任务（如 issue 编号或计划文件）交给系统，走开后拿回一个 PR
- 同时使用多个编码 CLI 时保持会话、任务与审查状态一致
- 在真实代码库上对 agent 输出设置强制的规则边界与审查门
- 对本地模型（LM Studio、Ollama）跑与云端模型相同的工作流

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L41: Gobby is a local daemon that sits underneath the AI coding CLIs you already use
> L47: It is **not another agent.** It is the control plane the agents you already
> L52: A Python 3.13+ daemon you run locally. PostgreSQL is the runtime hub database,

## 星数曲线

```mermaid
xychart-beta
    title "GobbyAI/gobby 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `31221be944e7` · [字段定义](../../DATASET.md)*
