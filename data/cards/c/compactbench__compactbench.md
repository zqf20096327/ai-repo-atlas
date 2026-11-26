# compactbench/compactbench

⭐ 10 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/compactbench/compactbench) · [官网](https://compactbench.github.io/compactbench/) · 组织维护

**LLM 上下文压缩方法的评测基准：测量压缩后保留了什么**

CompactBench 是一个评测 LLM agent 上下文压缩方法的开源基准：给被测压缩器一段长对抗性对话，随对话推进反复压缩，每轮后由固定 reader 模型就幸存信息提问并机械评分（选项字母或精确值，无 LLM judge）。内置 6 种基线方法及 Anthropic、Codex CLI、LangChain 的压缩实现，支持自定义压缩器与 OpenAI 兼容端点。公开 starter/practice 套件用于开发，排名来自每次运行新生成的隐藏 Elite 集；0.3 版重写了案例生成与评分，分数不与 0.2 互通。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多轮压缩漂移评测：压缩器只能基于自身上轮产物继续，规则、决策、归属随对话变化
- 无 LLM judge，答案为选项字母或精确值，机械评分并给出置信区间
- 内置 naive-summary、hybrid-ledger 等方法及 Anthropic/Codex CLI/LangChain 压缩的复现实现
- 提供 --controls 对照：全文（上限）与空内容（下限）同题评分

## 适用场景

- 给自己的上下文压缩方法跑分并提交排行榜
- 在 CI 中检查压缩方法分数是否低于保存的基线
- 为 Claude Code/Codex/LangChain 等生成基于证据的压缩指令

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L12: Long-running LLM agents compact their history — summarize it, extract state, keep a ledger — and then carry on with
> L16: - **It measures the compaction layer, not the model.** The reader only ever sees your artifact.
> L22: - **Hidden ranked set.** Public Starter and Practice suites for development; ranked scores come from a hidden Elite


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `177bd093aab5` · [字段定义](../../DATASET.md)*
