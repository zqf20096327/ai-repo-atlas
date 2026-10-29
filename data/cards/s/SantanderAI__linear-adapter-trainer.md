# SantanderAI/linear-adapter-trainer

⭐ 30 · Python · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/SantanderAI/linear-adapter-trainer) · [官网](https://github.com/SantanderAI) · 组织维护

**训练线性适配器对齐检索查询嵌入，免重建索引提升 RAG 召回**

面向 RAG 检索优化的 Python 库：不重训嵌入模型，仅学习一个作用于查询侧的线性变换矩阵（初始为恒等），使查询嵌入更靠近相关 chunk、远离无关 chunk，向量索引保持不变。由两个模块组成：数据集生成器从知识库产出 (query, positive, negative) 三元组，支持语义相反/困难/随机/混合四种负样本挖掘；训练器用 triplet loss 训练适配器，并以 precision@k、recall@k、MRR、nDCG 报告检索增益。提供 Python API、CLI（TOML 配置驱动）与离线示例；核心依赖仅 numpy/torch/safetensors/tqdm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 查询侧线性变换，无需重建向量索引且可逆
- 四种负样本挖掘策略与防泄漏 train/val 划分
- 以 precision@k / recall@k / MRR / nDCG 报告 base vs adapted 增益
- 模型选择含恒等基线，适配器不会低于原始嵌入效果

## 适用场景

- RAG 检索质量不佳时，在不重训嵌入模型的前提下对齐查询嵌入
- 从自有知识库自动生成 triplet 训练集并量化检索提升
- 在 CI 或离线环境跑通完整流程（哈希嵌入器+模板查询）

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L13: > **AI / machine learning** Python library for retrieval-augmented generation
> L14: > (RAG): it trains linear embedding adapters with triplet loss to align your
> L19: LinearAdapterTrainer fine-tunes retrieval **without retraining your embedding

## 星数曲线

```mermaid
xychart-beta
    title "SantanderAI/linear-adapter-trainer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-29 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e065174e1b7c` · [字段定义](../../DATASET.md)*
