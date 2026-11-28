# ranajahanzaib/longcontext-eval

⭐ 3 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/ranajahanzaib/longcontext-eval) · 个人维护

**面向研究者的长对话 LLM 上下文能力评测平台**

用于评测 LLM 与上下文管理系统在长多轮对话中保留、追踪、推理信息的基准平台：内置 16 种上下文策略（BM25、稠密/混合检索、滚动摘要、结构化记忆等）、7 类任务分类体系（事实检索、约束追踪、时序排序、消歧等），提供多赛道排行榜、失败归因分析与交互式可视化观测台。强调前缀边界与数据划分的污染控制，通过 FastAPI 后端、Next.js 前端、CLI 与 Python SDK 运行。

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

- 16 种内置上下文管理策略的统一评测接口
- 7 类任务分类体系与多赛道排行榜（含 95% bootstrap 置信区间）
- Retrieval Omission / Reasoning Error 的失败归因分析
- 前缀边界与同会话同划分的污染控制机制

## 适用场景

- 研究模型在数百轮对话中的信息遗忘与衰减规律
- 在等价 token 预算下比较检索与截断策略
- 诊断评测失败源于检索缺失还是推理错误

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L12: **A rigorous open-source scientific benchmarking platform for evaluating how Large Language Models and context-mana
> L22: Existing LLM evaluation benchmarks (such as RULER, Needle-in-a-Haystack, or generic question-answering leaderboards


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `00f84a4a0da4` · [字段定义](../../DATASET.md)*
