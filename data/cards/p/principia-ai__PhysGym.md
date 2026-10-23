# principia-ai/PhysGym

⭐ 101 · Python · MIT · 推送 2026-01-06 · [GitHub](https://github.com/principia-ai/PhysGym) · 组织维护

**评估 LLM 交互式物理科学推理的基准套件**

NeurIPS 2025 Datasets and Benchmarks Track 收录的基准套件：提供 97 个源自 PHYBench 的可执行物理仿真环境，核心机制是通过 L1-L4 四级先验知识控制（从完整描述到完全匿名变量）区分记忆与机制推断；设 100 次实验预算限制，以符号化与 LLM 等价性判定成功率，辅以 R²、MSE 等一致性指标，并记录完整实验历史。面向科研人员评测 OpenAI、Anthropic、Google、DeepSeek 及经 Ollama/vLLM 本地部署的模型。通过 git clone 源码安装，API key 经环境文件配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- L1-L4 四级先验知识控制，区分记忆与真实推断
- 97 个 PHYBench 物理问题带可执行仿真与实验预算限制
- 符号化（SymPy）+ LLM 双通道方程等价性评估
- 支持 Ollama/vLLM 本地模型与 OpenRouter 等多提供商

## 适用场景

- 评测不同 LLM 在受控先验条件下的科学发现能力
- 研究智能体的实验设计与归纳推理策略
- 对比推理型与非推理型模型的探索行为

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L8: A novel benchmark suite and simulation platform for rigorously assessing LLM-based scientific reasoning in interacti
> L38: - **Interactive Physics Environments**: 97 curated physics problems from PHYBench, each with executable simulations

## 星数曲线

```mermaid
xychart-beta
    title "principia-ai/PhysGym 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-23 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d5f54aacb6be` · [字段定义](../../DATASET.md)*
