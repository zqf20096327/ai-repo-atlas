# scienceetonnante/eleusis-llm-benchmark

⭐ 14 · Python · MIT · 推送 2026-02-16 · [GitHub](https://github.com/scienceetonnante/eleusis-llm-benchmark) · [官网](https://huggingface.co/spaces/huggingface/eleusis-benchmark) · 个人维护

**用 Eleusis 纸牌游戏评测 LLM 归纳推理能力的基准**

基于 Robert Abbott 1956 年 Eleusis 纸牌游戏改编的 LLM 评测基准：每轮加载一条秘密规则（接受/拒绝卡牌的 Python 函数），模型从 12 张手牌中逐张出牌并观察接受与否，可随时猜测规则但错误猜测会扣分，猜对或达回合上限即结束，按 max_turns - turn_used - 罚分计分。支持 anthropic/openai/google/xai/huggingface 五类模型提供商，提供单模型与并行多模型评测脚本、结果分析图表生成，规则库由自然语言经 LLM 编译为可执行 Python。面向研究者的归纳推理评测工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 秘密规则+出牌反馈机制模拟科学假设检验过程
- 支持 anthropic/openai/google/xai/huggingface 五类提供商
- 并行多模型评测与结果图表分析脚本
- 自然语言规则经 LLM 编译为可执行 Python 规则库

## 适用场景

- 评测不同 LLM 的归纳推理与模式发现能力
- 对比多个模型在同一规则库上的表现并生成图表报告
- 研究 LLM 在假设检验式交互任务中的行为

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A benchmark for evaluating Large Language Models on **inductive reasoning and pattern discovery**, using an adaptati
> L5: A secret rule determines which cards are accepted. The model must discover the rule by playing cards and observing t
> L79: Supported providers: `anthropic`, `openai`, `google`, `xai`, `huggingface`.

## 星数曲线

```mermaid
xychart-beta
    title "scienceetonnante/eleusis-llm-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c0ef5dc0c658` · [字段定义](../../DATASET.md)*
