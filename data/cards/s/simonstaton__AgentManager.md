# simonstaton/AgentManager

⭐ 28 · TypeScript · MIT · 推送 2026-06-03 · [GitHub](https://github.com/simonstaton/AgentManager) · 个人维护

**面向开发者的 Claude Code 多 agent 编排与安全管控平台**

AgentManager 运行多个 Claude Code CLI 进程作为自治编码 agent，每个 agent 拥有隔离 workspace 与完整工具访问（文件编辑、bash、git、MCP）。平台提供 6 层紧急 kill switch（进程终止、token 轮换、GCS 远程终止等）、按 agent 的 token/成本统计、agent 间消息总线、任务图编排器、父子弹出与销毁、cgroup 内存监控、Git worktree 管理。状态同步至 GCS，Cloud Run 缩容到零后 agent 可恢复。仅支持 Docker 部署，可本地运行或经 Terraform 部署到 GCP Cloud Run。

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

- 6 层紧急 kill switch：全局停止、进程终止、token 轮换、生成限制、命令黑名单、GCS 远程终止
- 最多 100 个并发 agent，各有隔离 workspace 与完整 Claude Code 能力
- agent 间消息总线（task/result/question/interrupt）与共享上下文（GCS 同步）
- 按 agent 的 token 计数与 USD 成本估算，支持 Opus/Sonnet/Haiku 选型

## 适用场景

- 组建多个 agent 团队并行协作开发同一功能
- 运行长期 PR 监控 agent 定时审查代码并留言
- 在 agent 失控时通过多层 kill switch 紧急停止并审计损害

## 场景标签

`Agent 框架` `多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L12: AgentManager runs Claude Code CLI processes. Each agent is a real Claude Code session with full tool access (file e
> L25: The SDK gives you chat completions with tool calling. Claude Code gives you a complete coding agent with file editi
> L130: Browser (React SPA)  ->  Express API (/api/*)  ->  Claude CLI processes

## 星数曲线

```mermaid
xychart-beta
    title "simonstaton/AgentManager 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-27 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `526e59aae2c1` · [字段定义](../../DATASET.md)*
