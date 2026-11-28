# ynymhrb/long-horizon-runtime

⭐ 20 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/ynymhrb/long-horizon-runtime) · 个人维护 · 中文 README

**DeepSeek Harness 的长任务插件：计划、确认、跟踪并跨会话恢复任务**

以插件形式挂在 DeepSeek Harness 上的长任务运行时：把研究、开发、排障、资料整理类工作拆成分步骤计划，经用户确认后执行；任务步骤、依赖与状态在 Task Area 面板展示，中断或换会话后可继续同一任务。支持修改目标保留已完成工作、操作者暂停不被代理撤销、本地多 Worker 并发额度与自定义编排模板，可注册 Codex、Claude Code 及自定义可执行文件作为执行后端。依赖宿主 `dsh web` 正常运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 计划确认制：先出分步计划，确认后执行，Task Area 展示步骤、依赖与状态
- 跨会话恢复：暂停、改目标、换对话后继续同一任务，保留已完成工作
- 操作者暂停优先：`operator` 暂停不被代理或系统恢复覆盖，并留决策记录
- 可配置编排：多 Worker 并发额度、工作流/讨论模板、自定义 Worker 经 stdin/stdout JSON 协议接入

## 适用场景

- 长时间研究与资料整理任务，拆步骤推进且中断可续
- 开发/排障中需先审计划再放行执行
- 多模型/多 Worker 混合编排（如设计用 claude、开发用 coding 组）
- 多人或长会话中追踪任务进度与状态

## 场景标签

`工作流自动化` `编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: Long Horizon Runtime 是 DeepSeek Harness 的长任务插件。它适合研究、开发、排障、资料整理这类需要拆步骤、持续推进的工作：先看计划，确认后执行；过程随时可见，任务中断也能接着做。
> L88: 在 DSH Web 打开 **设置 → 长任务**，可以调整执行器和执行组、模型与工具额度，以及编排模板。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `e00f271eb365` · [字段定义](../../DATASET.md)*
