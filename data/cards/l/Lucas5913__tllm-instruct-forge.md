# Lucas5913/tllm-instruct-forge

⭐ 53 · HTML · 推送 2026-10-25 · [GitHub](https://github.com/Lucas5913/tllm-instruct-forge) · 个人维护

**面向团队的 LLM 指令微调训练库，含数据治理与评估**

tllm 是一个用于大语言模型指令微调的开源 Python 训练库，面向团队与独立研究者。功能包括可组合的训练配方（损失函数、调度器、适配器）、数据集治理套件（去重、长度分桶、毒性过滤）、LoRA/QLoRA/前缀微调适配器、流式训练遥测、确定性检查点与 YAML 实验清单，并配本地单页仪表盘展示运行时间线、损失曲线与数据集健康面板。架构分摄取、治理、建模、训练、评估五层，各层可替换。采用 MIT 许可。README 未给出具体安装命令与依赖清单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LoRA/QLoRA/前缀微调为一等公民的适配器优先设计
- 数据集治理套件：去重、长度分桶、毒性过滤、提示-回复平衡
- 每次实验输出可复现的 YAML manifest 与确定性检查点
- 本地单页仪表盘：运行时间线、损失曲线、数据集健康面板

## 适用场景

- 对开源大模型做指令微调并保证实验可复现
- 在训练前清洗与平衡指令数据集
- 对比不同检查点在相同提示上的表现

## 场景标签

`微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: tllm is an opinionated training library built for teams and solo researchers who want to shape large language models
> L46: - 🧠 **Adapter‑first design** — LoRA, QLoRA, and prefix tuning are first‑class citizens, not afterthoughts.

## 星数曲线

```mermaid
xychart-beta
    title "Lucas5913/tllm-instruct-forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-26 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `461d5411ad7d` · [字段定义](../../DATASET.md)*
