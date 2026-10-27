# zhenyi4/ssa

⭐ 32 · Python · MIT · 推送 2026-05-07 · [GitHub](https://github.com/zhenyi4/ssa) · 组织维护

**论文 SSA 官方实现：用全/稀疏注意力对齐做高效预训练框架**

ICML 2026 论文 SSA（Sparse Sparse Attention）的官方代码库：一个混合稀疏与全注意力的预训练训练框架，通过双向注意力输出对齐同时缓解 Attention Gap 与 Capability Gap，可调节稀疏度而无需重训。提供 4 个在 100B SmolLM 数据集上预训练的 1B 检查点（SSA/FullAttn/MoBA/NSA），支持 lm-eval 系评测与 LongBench/NIAH 长上下文评测。依赖 PyTorch 2.6.0、CUDA 12.4 与 FlashAttention 2.7.3，需克隆仓库并替换 NSA 库文件后运行；稀疏注意力推理尚不支持 KV cache。面向从事 LLM 高效注意力研究的科研人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每步随机选择稀疏/全注意力双流训练并做双向输出对齐
- 提供 SSA-1B 及 FullAttn/MoBA/NSA 三个基线 1B 检查点（HuggingFace）
- 推理可切换 sparse/full 模式并按预算调节稀疏度，无需重训
- 支持 RoPE scaling 将 8k 预训练模型外推到 32k 做长上下文评测

## 适用场景

- 复现论文的稀疏注意力预训练与评测结果
- 在自有数据上训练带对齐目标的稀疏注意力 LLM
- 比较 SSA 与 MoBA/NSA 稀疏注意力方法的性能

## 场景标签

`模型训练` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: This is the official implementation of the paper: SSA: Sparse Sparse Attention by Aligning Full and Sparse Attentio
> L20: We propose **SSA (Sparse Sparse Attention)**, a training framework that integrates both sparse and full attention w

## 星数曲线

```mermaid
xychart-beta
    title "zhenyi4/ssa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `52247a540e15` · [字段定义](../../DATASET.md)*
