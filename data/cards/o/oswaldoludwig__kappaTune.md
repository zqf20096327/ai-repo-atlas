# oswaldoludwig/kappaTune

⭐ 13 · Python · Apache-2.0 · 推送 2026-03-13 · [GitHub](https://github.com/oswaldoludwig/kappaTune) · 个人维护

**PyTorch 优化器包装：按条件数选择性微调以缓解灾难性遗忘**

面向持续学习场景的 PyTorch 优化器包装库：计算模型权重张量的条件数 κ，排序并仅更新各向异性最低（条件数最小）的参数子集，以保留预训练知识、缓解灾难性遗忘，同时附带降低计算量。可与任意标准 PyTorch 优化器集成，支持按维度数与最大维度过滤张量并缓存条件数。另提供 Hugging Face PEFT 集成，可自动选择条件数最小的 N 个模块挂载 LoRA 适配器；README 将其与 LoRA 对比，称 LoRA 本身不含防遗忘策略。要求 Python 3.8+，示例涉及 TinyLlama-1.1B 与 ag_news。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按张量条件数 κ 排序，仅更新最不重要/各向异性最低的参数子集
- 可与任意标准 PyTorch 优化器集成
- 条件数缓存与按维度/尺寸的灵活过滤
- Hugging Face PEFT 集成：自动选择 N 个模块应用 LoRA 适配器

## 适用场景

- 持续学习/领域适应中微调 LLM 并保留预训练知识
- 自动决定 LoRA 应挂载到哪些模块，避免手动猜测
- 在 ag_news 等数据集上做选择性微调实验

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: A PyTorch-based optimizer wrapper for continual learning via selective fine-tuning, guided by the condition number (
> L18: * **Selective Fine-Tuning:** Integrates with any standard PyTorch optimizer, ensuring only the selected parameters 

## 星数曲线

```mermaid
xychart-beta
    title "oswaldoludwig/kappaTune 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `d0b698625937` · [字段定义](../../DATASET.md)*
