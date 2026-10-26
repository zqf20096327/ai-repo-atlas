# dmis-lab/Outlier-Safe-Pre-Training

⭐ 40 · Python · 推送 2025-11-04 · [GitHub](https://github.com/dmis-lab/Outlier-Safe-Pre-Training) · [官网](https://www.arxiv.org/abs/2506.19697) · 组织维护

**面向 4-bit 量化鲁棒性的 LLM 预训练方法（ACL 2025）代码与模型**

ACL 2025 论文 Outlier-Safe Pre-Training（OSP）的官方仓库：通过 SSNorm（单标量 RMSNorm）与 EmbProj（嵌入空间正交投影）两项架构修改，在预训练阶段抑制激活离群值，使模型对 4-bit 量化鲁棒。在 1.4B 参数、1 万亿 token 规模上训练（遵循 SmolLM 配方），相比标准训练仅引入约 2% 减速，训练后投影矩阵可合并回权重、推理架构不变。仓库提供基于 JAX/Flax 的简化实现、WikiText-2 与 lighteval 评测脚本（RTN/GPTQ/Hadamard 旋转/QuaRot 等量化设置）、以及 TPU 上分布式 Muon 优化器实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SSNorm + EmbProj 在预训练阶段抑制离群激活，保持推理时架构兼容
- 1.4B 模型在 1 万亿 token 上训练，相比标准训练约 2% 减速并降低 GPU 内存
- 支持 RTN / FFN Hadamard / GPTQ / QuaRot 等多种量化评测路径
- 提供 TPU SPMD 分布式 Muon 实现（Newton-Schulz 并行正交化）

## 适用场景

- 从零训练对 4-bit 量化友好的基础模型
- 复现论文的困惑度与 10 项基准评测结果
- 研究 Muon 优化器在大规模分布式训练中的应用

## 场景标签

`模型训练` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L13: Our work, **Outlier-Safe Pre-Training (OSP)**, proposes a practical approach to training models that are robust to 
> L16: Prior methods for quantization-friendly pre-training are often limited to small-scale experiments (e.g., models und
> L18: 2. ⚡**Maintaining computational efficiency comparable to standard training**

## 星数曲线

```mermaid
xychart-beta
    title "dmis-lab/Outlier-Safe-Pre-Training 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-26 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `119d83cf9db5` · [字段定义](../../DATASET.md)*
