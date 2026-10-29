# alleyxd/SecondThought

⭐ 20 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/alleyxd/SecondThought) · 个人维护

**小型本地模型工具调用的置信度门控推理方法（研究代码）**

面向小参数量模型（Qwen3 1.7B/4B/8B，vLLM 部署）工具调用场景的研究代码：先以 no-think 模式直接调用并读取 token 对数概率，若均值低于阈值则重跑 thinking 模式；若模型选择不调用则保持拒绝。无需训练、不引入额外模型，仅使用推理服务器已返回的数值。附 BFCL 单轮评测结果（1,398 项）与论文 PDF。局限：单一模型族、贪心解码、仅单轮 BFCL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于均值 token log-probability 的门控，仅在低置信时触发 thinking
- 无需训练与额外模型，复用服务器返回的 log-probs
- BFCL 评测：门控 30% 思考保留 66-70% 的 thinking 增益，token 约减半
- 首个 token 是否为工具调用的概率可预测是否需要调用（AUROC 0.96-0.98）

## 适用场景

- 降低小型模型工具调用场景的推理 token 开销
- 复现论文中 BFCL 评测与十二项单因子干预实验
- 研究置信度估计在推理门控中的应用

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L6: Thinking before a tool call makes small models more accurate, but it costs six to seven times the output tokens and
> L9: Make the normal no-think tool call with log-probabilities on. If its mean token log-probability is low, rerun with
> L10: thinking. If the model declined to call, keep the decline. No training, no extra model: it uses numbers the server

## 星数曲线

```mermaid
xychart-beta
    title "alleyxd/SecondThought 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-26 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `79d240a81251` · [字段定义](../../DATASET.md)*
