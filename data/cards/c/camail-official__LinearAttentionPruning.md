# camail-official/LinearAttentionPruning

⭐ 15 · Python · 推送 2026-09-25 · [GitHub](https://github.com/camail-official/LinearAttentionPruning) · [官网](https://arxiv.org/abs/2602.04852) · 个人维护

**线性注意力模型的结构化剪枝工具：基于秩的 Q/K 降维**

论文 The Key to State Reduction in Linear Attention: A Rank-based Perspective 的官方代码库。对 DeltaNet 与 Gated DeltaNet 模型做结构化 Q/K 维度缩减（如 DRRQR 将 key 维度减半），以提升效率；剪枝后可通过 LoRA 微调恢复性能，并附带基准评测、推理速度/显存对比与递归状态秩利用分析脚本。通过 git clone 源码并以 uv 安装依赖，使用 bash 脚本驱动训练、剪枝、微调与评测流程，支持从 Hugging Face Hub 直接读取模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 DeltaNet/Gated DeltaNet 做结构化 Q/K 维度缩减
- 剪枝后 LoRA 微调恢复性能
- 推理速度与显存对比的基准测试脚本
- 递归状态有效秩分析工具

## 适用场景

- 压缩线性注意力模型以降低推理开销
- 复现论文中的秩剪枝实验
- 分析模型递归状态对隐空间的利用程度

## 场景标签

 · 领域:机器学习/模型压缩

## 证据(README 行号)

> L8: This is the main repository accompanying the paper The Key to State Reduction in Linear Attention: A Rank-based Pers
> L35: We provide several structural pruning methods. You can prune either a local checkpoint or a model directly from the

## 星数曲线

```mermaid
xychart-beta
    title "camail-official/LinearAttentionPruning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1566fdbb1f2e` · [字段定义](../../DATASET.md)*
