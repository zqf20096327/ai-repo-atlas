# FareedKhan-dev/long-running-agent

⭐ 50 · Python · MIT · 推送 2026-06-03 · [GitHub](https://github.com/FareedKhan-dev/long-running-agent) · [官网](https://medium.com/@fareedkhandev/building-a-week-long-running-agentic-system-2ad79f8190bb) · 个人维护

**可运行数周的长时程 agent 框架：持久执行+确定性验证**

一个分阶段实现的开源 agent 框架（当前处于 Phase 0 早期阶段），目标是让 agent 执行持续数天到数周的软件任务并自我改进。机制上：以 git 仓库与结构化进度日志为外部事实源，agent 循环运行在 Temporal 工作流中以支持崩溃后恢复；完成判定以真实测试/lint/build 通过为准而非模型自述。采用单线程 Lead Engineer 加只读/评审 agent 扇出的组织结构；模型层可插拔（Ollama 本地、免费云端或 Claude API）。通过 uv 安装运行，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Temporal 持久工作流，崩溃/重启后从中断点恢复且不重复消耗 token
- 外部化状态：git 仓库 + 进度/清单/决策日志，每周期重读
- 确定性验证门槛：测试/lint/build 通过才算完成
- 模型层可插拔：Ollama 本地、OpenAI 兼容免费云端、Claude

## 适用场景

- 构建需要数天到数周才能完成的长期软件任务 agent
- 研究崩溃恢复与上下文外部化等长时程自主性工程问题
- 在本地（Ollama）以零成本跑真实 agent 任务

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L29: - **Durable execution.** The agent loop runs inside a Temporal workflow.
> L33: - **Deterministic verification.** A checklist item is only "done" when **real tests/lint/build/

## 星数曲线

```mermaid
xychart-beta
    title "FareedKhan-dev/long-running-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-27 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a50381e1ead5` · [字段定义](../../DATASET.md)*
