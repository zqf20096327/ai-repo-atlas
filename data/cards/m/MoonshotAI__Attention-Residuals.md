# MoonshotAI/Attention-Residuals

⭐ 3,538 · 推送 2026-03-17 · [GitHub](https://github.com/MoonshotAI/Attention-Residuals) · 组织维护 · 中文 README

**Transformer 残差连接的注意力替换方法（AttnRes）官方仓库**

MoonshotAI/Kimi Team 的 Attention Residuals 论文官方仓库：提出用逐层学习到的 softmax 注意力取代 Transformer 中固定权重的标准残差累加，使每层可选择性聚合此前所有层的表示；并给出 Block AttnRes 分块变体，将内存从 O(Ld) 降至 O(Nd)。README 提供方法概述、PyTorch 风格伪代码、Kimi Linear 48B 上的基准测试结果与引用信息，未提供安装命令或可运行代码。

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

- 以逐层学习的伪查询 softmax 注意力替换标准残差连接
- Block AttnRes 将内存从 O(Ld) 降至 O(Nd)，约 8 个分块即可接近全量效果
- 作为残差连接的 drop-in 替换，边际开销较小
- 在 Kimi Linear 48B（1.4T tokens 训练）上报告 MMLU/GPQA/HumanEval 等基准结果

## 适用场景

- 研究更深 Transformer 架构中的表示聚合方式
- 训练大模型时替换标准残差连接以缓解 PreNorm 稀释问题
- 参考论文基准结果与伪代码复现方法

## 场景标签

 · 领域:深度学习架构研究

## 证据(README 行号)

> L17: This is the official repository for **Attention Residuals (AttnRes)**, a drop-in replacement for standard residual 
> L31: Full AttnRes is straightforward but requires O(Ld) memory at scale. **Block AttnRes** partitions layers into N bloc

## 星数曲线

```mermaid
xychart-beta
    title "MoonshotAI/Attention-Residuals 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 3525 --> 3539
    line [3526, 3538]
```

2026-10-18 3,526 → 2026-10-22 3,538（+12）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 high · 依据 README sha `7a61113b79a7` · [字段定义](../../DATASET.md)*
