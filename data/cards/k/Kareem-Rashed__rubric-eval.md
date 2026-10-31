# Kareem-Rashed/rubric-eval

⭐ 14 · Python · MIT · 推送 2026-06-12 · [GitHub](https://github.com/Kareem-Rashed/rubric-eval) · [官网](https://rubriceval.vercel.app) · 个人维护

**面向 LLM 应用与 agent 的本地行为评测框架**

Python 编写的 LLM 与 AI agent 评测框架，以 agent 运行行为（工具调用、参数、调用顺序、trace、延迟、成本）为核心测试对象，而非仅评分最终输出。从 LangGraph 或任意 OpenAI 格式消息列表提取数据，也可加载 LangFuse/LangSmith 导出的 trace。内置 ToolCallAccuracy、TraceQuality、幻觉评分等指标，LLM-judge 指标可搭配任意 callable（OpenAI/Anthropic/Ollama）并支持波动性检测。提供 CLI、pytest 集成、自包含 HTML 报告与 GitHub Action 基线对比。零必需依赖、全本地运行、MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以工具调用/trace/延迟为核心的 agent 行为指标（9 项）
- 支持任意 OpenAI 格式消息、LangFuse/LangSmith trace 导入
- CLI 基线对比与 GitHub Action 在 PR 上报告回归
- 零必需依赖、全本地运行，LLM-judge 支持波动性检测

## 适用场景

- 在 CI 中拦截 prompt 改动导致的 agent 行为回归
- 对 agent 的工具调用正确性与禁止工具规避做断言
- 本地生成带 trace 明细的 HTML 评测报告

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3:  Agent behavior testing for LLM apps.
> L15: Rubric tests the **behavior**: which tools were called, with what arguments, in what order, whether forbidden tools
> L144: - **CI-native.** Baseline diffing, PR comments, and exit codes are built in, not a paid add-on.

## 星数曲线

```mermaid
xychart-beta
    title "Kareem-Rashed/rubric-eval 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `140a1d5b6cfc` · [字段定义](../../DATASET.md)*
