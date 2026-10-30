# THU-KEG/DeepPrune

⭐ 21 · Python · MIT · 推送 2026-04-20 · [GitHub](https://github.com/THU-KEG/DeepPrune) · [官网](https://deepprune.github.io/) · 组织维护 · 中文 README

**并行推理冗余剪枝方法：推理前剪除语义重复的推理链**

ACL 2026 Findings 论文的官方代码库。LLM 并行生成多条推理链以提升答案可靠性时，链间常存在语义冗余；DeepPrune 通过监督微调训练模型（基于 Qwen3-4B-Instruct-2507 骨干、Llama-Factory 框架并修改支持 Focal Loss）在完整执行前识别并剪除冗余推理链，以降低推理成本。流程含准备成对比较微调数据、离线训练（实验报告 AUROC > 0.83）、在线推理时贪心聚类剪枝，并提供阈值调节成本与性能的权衡。数据集因体积仅部分提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 训练模型在执行前识别语义冗余推理链（实验 AUROC > 0.83）
- 在线阶段按相似度分数贪心聚类并剪枝，阈值可调成本/性能权衡
- 以 Qwen3-4B-Instruct-2507 为骨干，经 Llama-Factory 微调（需补丁支持 Focal Loss）
- 提供初步分析 notebook（答案一致性分布、冗余检测 ROC 对比）

## 适用场景

- 降低 LLM 并行多链推理的计算与推理成本
- 研究并行扩展中链间冗余的度量与剪除
- 在保持共识准确率的前提下缩减执行的推理链数量

## 场景标签

 · 领域:LLM 推理优化/科研代码

## 证据(README 行号)

> L13: **DeepPrune** addresses this by learning to identify and prune semantically redundant traces *before* full executio
> L29: ⚠️ We use `Qwen/Qwen3-4B-Instruct-2507` as the backbone LLM for DeepPrune. You can download it from Qwen/Qwen3-4B-I

## 星数曲线

```mermaid
xychart-beta
    title "THU-KEG/DeepPrune 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `dfc3cdfd86c3` · [字段定义](../../DATASET.md)*
