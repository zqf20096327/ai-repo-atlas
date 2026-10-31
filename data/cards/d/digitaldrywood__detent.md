# digitaldrywood/detent

⭐ 16 · Go · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/digitaldrywood/detent) · [官网](https://digitaldrywood.com) · 组织维护

**基于看板的编码代理工作流编排器：让 agent 在自管机器上执行并合入 issue**

以单一 Go 二进制（detent）交付的工程流程编排工具：监视项目看板上的 issue，由用户登记的 Runner 机器认领任务，在隔离的 Git worktree 中启动编码代理（Codex CLI、Claude Code，或经 Ollama 的本地模型），执行仓库定义的 gate 命令校验，再经串行化合并队列逐一落地变更；支持人工审查门与 Web/终端面板。Hub 可用 Detent Cloud 或自托管（免费、无需账号），并通过 MCP 暴露看板与变更数据。许可证为 FSL-1.1-ALv2（两年后转 Apache 2.0），禁止前两年将其作为竞争性商业产品提供。

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

- 看板驱动的 issue 分发：Runner 认领后在隔离 Git worktree 中运行编码代理
- 配置即代码：detent.yaml 定义 lane/gate/审查策略，WORKFLOW.md 定义代理行为契约
- 串行化合并队列：一次落地一个变更，失败自动退回 Rework
- Hub 支持 Detent Cloud 或自托管，并通过 MCP 暴露看板、issue、变更与运行历史

## 适用场景

- 把 GitHub Projects/看板上的 issue 交给编码代理在自有机器上自动完成并通过验证门合入
- 团队以并行 worktree 同时运行多个代理任务并串行落地变更
- 通过 MCP 让自有代理提交 issue、读取运行历史并审查 Change Request

## 场景标签

`工作流自动化` `编码 Agent` · 领域:效率与自动化

## 证据(README 行号)

> L9: Detent runs your engineering process with coding agents. You write issues on a board; Detent hands each ready issue 
> L62: 1. **You put an issue in `Todo`.** A runner that holds the project claims it, creates an isolated worktree, and sta
> L103: - OpenAI Codex CLI, through `codex app-server`.

## 星数曲线

```mermaid
xychart-beta
    title "digitaldrywood/detent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `153a63b1dc51` · [字段定义](../../DATASET.md)*
