# harnexa/nexa-gauge

⭐ 40 · Python · MIT · 推送 2026-08-03 · [GitHub](https://github.com/harnexa/nexa-gauge) · [官网](https://www.harnexa.dev/nexa-gauge/docs/introduction) · 个人维护

**面向 LLM/RAG 输出的图式评估框架，带成本预估与缓存**

Python 包与 CLI 工具，通过确定性节点图评估 LLM、RAG 与 agentic 系统的生成输出：覆盖相关性、事实溯源（grounding）、红队安全评分、GEval/LLM-as-a-judge、参考答案匹配（BLEU/METEOR/ROUGE）与嵌入语义对齐六类指标。执行前可预估未缓存的调用成本，缓存键包含输入、标准、模型路由与提示版本；支持按节点配置模型与回退模型，输出逐案例 JSON 报告。输入支持 JSON/JSONL/CSV/文本与 Hugging Face 数据集（可选依赖）。

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

- 六类评估指标节点：relevance/grounding/redteam/geval/refmatch/refalign
- estimate-first 执行：LLM 调用前预估未缓存成本
- 确定性的路由感知缓存，避免重复 LLM 支出
- 逐节点模型路由与回退模型、温度配置

## 适用场景

- 对 RAG 回答做相关性与上下文支持度评估
- 提示词迭代与回归测试中量化输出质量
- 发布前作为质量与安全门禁跑红队评分
- CI 流水线中生成结构化逐案例评估报告

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L26: `nexa-gauge` is a Python package and command-line toolkit for evaluating generated outputs from LLM, RAG, and agent
> L28: It is designed for prompt iteration, benchmark runs, regression testing, release gates, and production evaluation w

## 星数曲线

```mermaid
xychart-beta
    title "harnexa/nexa-gauge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-27 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `71b64426c2ab` · [字段定义](../../DATASET.md)*
