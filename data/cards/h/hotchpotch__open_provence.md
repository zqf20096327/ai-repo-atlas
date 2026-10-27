# hotchpotch/open_provence

⭐ 70 · Python · MIT · 推送 2025-11-22 · [GitHub](https://github.com/hotchpotch/open_provence) · 个人维护 · 中文 README

**开源上下文剪枝重排模型：为 RAG 删除无关上下文并打相关性分**

Provence 式 reranker–pruner 模型的开源实现：在检索增强生成流程中置于 LLM 之前，删除无关上下文句子并同时输出相关性分数，用于压缩 token 开销。提供 4 个 30M–310M 参数 checkpoint（ModernBERT 骨干，MIT 许可），覆盖英语和日语；30M xsmall 可在 CPU 上运行。附带训练 playbook（单卡 ≥16GB NVIDIA GPU 可复现）、数据集构建管线、评测 CLI 与 Gradio Web demo；MLDR 评测中在保持答案率的同时压缩 80–99% 文本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 删除约 99% 离题句子同时压缩 80–90% 相关文本（MLDR 评测）
- 4 个 30M–310M checkpoint（英语/日语）发布于 Hugging Face，MIT 许可
- 单张 ≥16GB NVIDIA GPU 即可复现全部 checkpoint 训练
- 提供数据集构建管线与数据集保留率/MLDR 评测 CLI

## 适用场景

- RAG / DeepResearch 流程中压缩检索上下文以降低 token 开销
- 延迟敏感场景用 30M xsmall 在 CPU 上做快速剪枝
- 用自己的领域数据构建 Provence 格式数据集并训练专属模型

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L10: OpenProvence is a fully open-source implementation of Provence-style reranker–pruner models. These models remove ir
> L14: - **Pruning power** – Drop ~99% of off-topic sentences while still compressing 80–90% of relevant text; MLDR evalua
> L15: - **Model zoo you can ship today** – Four checkpoints (30M–310M parameters) covering English and Japanese, each pub

## 星数曲线

```mermaid
xychart-beta
    title "hotchpotch/open_provence 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-27 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f850ba2ff817` · [字段定义](../../DATASET.md)*
