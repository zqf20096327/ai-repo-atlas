# danilop/micro-gpt-and-beyond

⭐ 46 · Python · MIT · 推送 2026-08-25 · [GitHub](https://github.com/danilop/micro-gpt-and-beyond) · [官网](https://karpathy.ai/microgpt.html) · 个人维护

**面向学习者的 GPT 从零构建渐进式实验课程（24 个 lab，8 章）**

受 Karpathy microGPT 启发的教学实验系列：24 个 lab 从纯 Python 标量 autograd 起，逐步用 NumPy、PyTorch、JAX、MLX 表达同一字符级 transformer，在同一约 3.2 万人名数据集上训练；随后扩展 BPE、RoPE、GQA、KV cache、LoRA、INT8 量化、推测解码、PagedAttention、文本扩散、自改进等主题。每 lab 用 uv run 或 python 运行，数据集首跑自动下载。明确列出未覆盖主题（DPO、MoE、SwiGLU、连续批处理）与刻意排除项。面向 ML 学生、工程师、从业者与研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 24 个 lab 按 8 章组织，从零依赖纯 Python 到 PyTorch/JAX/MLX 三框架对比
- 覆盖现代架构与推理优化：BPE、RoPE、GQA、KV cache、推测解码、PagedAttention、解耦服务
- 每 lab 训练同一架构（4,192 参数级 transformer），差异仅来自框架语义与硬件
- 提供交互式网页教程（逐行讲解与 Mermaid 图）及 run_lab.py 辅助脚本

## 适用场景

- 从第一性原理学习 transformer 的构建、训练与部署
- 对比 PyTorch、JAX、MLX 三种框架的实现差异
- 学习 KV cache、推测解码、PagedAttention 等推理优化技术
- 了解文本扩散、soft thinking 等非自回归生成范式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: A progressive series of labs exploring tiny language models, inspired by Andrej Karpathy's microGPT, a GPT trained a
> L5: **Interactive Web Tutorial** — browse the code with line-by-line explanations, Mermaid diagrams with per-line node h
> L105: - **ML students** learning transformers from first principles. Start with pure Python, see the full algorithm, the

## 星数曲线

```mermaid
xychart-beta
    title "danilop/micro-gpt-and-beyond 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-26 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c09148463fe3` · [字段定义](../../DATASET.md)*
