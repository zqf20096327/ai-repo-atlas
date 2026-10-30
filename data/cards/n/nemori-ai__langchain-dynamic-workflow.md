# nemori-ai/langchain-dynamic-workflow

⭐ 18 · Python · MIT · 推送 2026-06-12 · [GitHub](https://github.com/nemori-ai/langchain-dynamic-workflow) · 组织维护 · 中文 README

**面向 deepagents 的确定性可恢复多智能体编排框架**

Claude Code Dynamic Workflows 的社区移植版，构建在 LangGraph 持久执行之上：由确定性脚本持有循环、分支与扇出控制流，叶子 agent() 调用委托给 LangChain deepagents，各自在隔离且用后即弃的上下文中运行，仅最终结果回传调用方。提供 content-hash 日志实现零模型成本恢复、共享 token 预算、parallel/pipeline/race 扇出、reduce 聚合、沙箱与 git worktree 集成、AST 门控的 meta 层（宿主 agent 运行时编写脚本）。状态标注 alpha 0.3.0-dev，未发布 PyPI，需 Python 3.12+ 从克隆安装；默认离线后端不执行真实 shell，真实子进程后端为危险的可选项且非安全沙箱。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 确定性脚本持有控制流，叶子调用运行于隔离上下文，仅最终结果回传
- content-hash 日志使恢复运行以零模型成本重放已完成叶子
- parallel()/pipeline()/race() 扇出与 survives/dedup/reconcile/corroborate 归约
- AST 门控 meta 层：宿主 agent 运行时编写并受限 exec 编排脚本

## 适用场景

- 扇出密集的多角度研究、候选评审类任务
- 长链多步任务避免轨迹撑爆上下文
- 需要确定性恢复与多子 agent 共享 token 预算的流水线
- 让宿主 agent 通过 workflow 工具后台驱动与编排运行

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L12: > Deterministic, scripted, resumable multi-agent orchestration for LangChain `deepagents` — a community port of Cla
> L54: - **Layer 1 — orchestration runtime**: the primitives — `agent()`, `parallel()` (barrier), `pipeline()` (no barrier
> L57: Leaf `agent()` calls resolve a named deepagent from a **registry (roster)** and invoke it as a `@task`, reusing dee

## 星数曲线

```mermaid
xychart-beta
    title "nemori-ai/langchain-dynamic-workflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `429057904e66` · [字段定义](../../DATASET.md)*
