# TrustifAI/typed_evals

⭐ 16 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/TrustifAI/typed_evals) · 个人维护

**面向 LLM/RAG/Agent 的类型化评测与工具调用防护框架**

Python 评测工具包：输入请求、回答与证据，通过指标面板输出类型化分数、阈值与通过判定。提供 response/rag/agent 三种预设，指标含忠实度、答案相关性、上下文相关性等 11 个内置指标；支持在工具函数执行前做策略检查（ToolSafety 守卫，违规抛 GuardrailViolation）。评测后端可切换（Jev 默认、OpenAI Decisions、SystemOne），并提供 LangChain/CrewAI/Microsoft Agent Framework 适配器。校准模块用 Venn–Abers 或 isotonic 方法将分数拟合到人工标注。限制：需 Python>=3.12，openai 与 crewai extras 依赖冲突需分环境安装。

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

- RAG 预设覆盖忠实度、答案相关性/完整性、上下文相关性与充分性等 5 项检查
- guard_tool 在函数执行前做策略检查，失败抛 GuardrailViolation
- 校准支持 Venn–Abers（<2000 标注行）与 isotonic（≥2000）拟合人工标签
- LangChain/CrewAI/Microsoft Agent Framework 适配器接入 guard_tool

## 适用场景

- 为 RAG 问答系统检查回答是否被上下文支持
- 评估 agent 运行是否完成任务并如实报告工具结果
- 在工具调用执行前拦截不合规操作
- 用人工标注校准指标分数以估计人类接受率

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L4:  A Python toolkit for checking LLM answers, evaluating agent runs, and reviewing tool calls before execution
> L17:  Know what passed. Decide what runs. Typed Evals takes your evidence through a metric panel and returns typed score

## 星数曲线

```mermaid
xychart-beta
    title "TrustifAI/typed_evals 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2155698e72b8` · [字段定义](../../DATASET.md)*
