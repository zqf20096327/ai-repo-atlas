# tlaplus/TLAiBench

⭐ 37 · Python · MIT · 推送 2026-02-06 · [GitHub](https://github.com/tlaplus/TLAiBench) · 组织维护

**评估 LLM 在 TLA+ 形式规约任务上的数据集与基准套件**

TLA+ 社区维护的评测数据集：以逻辑谜题（过河、Die Hard）与并发、算法、博弈等真实场景的自然语言题目为输入，用 GenAIScript 驱动 LLM 生成 TLA+ 规约，自动执行语法检查与 TLC 模型检测，并对照 gold standard 规约从反例、精化检查、行为等价、性质满足四个维度评分。面向形式化方法与 AI 研究者、AI 辅助规约工具开发者及教学场景。运行需 VSCode（TLA+ MCP 服务器）、Node.js 24+、tla2tools.jar 与 CommunityModules-deps.jar。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言谜题→TLA+ 规约生成的自动化基准流程
- 基于反例/精化/行为等价/性质满足的四维评分
- GenAIScript 运行时支持多种 LLM 提供商及 Ollama 本地模型
- 题目按逻辑谜题、并发、算法、博弈、数学、仿真六类组织

## 适用场景

- 对比不同 LLM 在形式规约生成任务上的表现
- 为 AI 辅助 TLA+ 开发工具提供参考基准
- 通过带 gold standard 的实例学习 TLA+

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A dataset and benchmark suite for evaluating Large Language Models (LLMs) on TLA+ formal specification tasks, featur
> L16: - **Consistent LLM Evaluation**: Objective comparison of language model performance on formal specification tasks

## 星数曲线

```mermaid
xychart-beta
    title "tlaplus/TLAiBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6982a8ca0fc9` · [字段定义](../../DATASET.md)*
