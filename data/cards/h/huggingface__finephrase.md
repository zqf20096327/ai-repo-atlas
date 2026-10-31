# huggingface/finephrase

⭐ 44 · Python · 推送 2026-06-05 · [GitHub](https://github.com/huggingface/finephrase) · 组织维护

**486B token 合成预训练数据集及其改写/训练流水线**

Hugging Face 维护的合成预训练数据项目：通过对网页语料（FineWeb-Edu 等）做 LLM 改写生成 486B token 数据集，附配套 CLI 流水线，覆盖数据筛选（HQ/LQ 过滤）、prompt 迭代、规模化改写、tokenize、基于 nanotron 的 Qwen 尺寸模型预训练（0.5b-6.2b）、lighteval 评测与基准结果导出。依赖 nanotron/lighteval/datatrove 的自定义分支并打补丁，训练通过 Slurm 提交，数据读取依赖 S3 与 HF Hub，适合有 GPU 集群的研究者复现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 486B token 数据集，90 次实验、1 万亿 token 生成、12.7 GPU 年的实验产出
- 数据改写流水线：筛选→prompt 迭代→LLM 改写→tokenize→训练→评测
- 多数据集混合权重训练与合成比例扫描（launch-experiments YAML 批量提交）
- N-gram 重叠的评测污染审计命令 audit-contamination

## 适用场景

- 为 LLM 预训练获取合成数据并复现配比实验
- 用自定 prompt 批量改写自有语料
- 审查训练数据与评测基准的重叠污染

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L8: We ran 90 experiments, generated over 1 trillion tokens, and spent 12.7 GPU years to find the best recipe for synthe
> L58: - `rephrase` - Rephrase datasets using LLM inference
> L171: Now kick off pretraining on the tokenized data. This submits a Slurm job that trains Qwen-size models (`0.5b`, `1.

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/finephrase 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 42 --> 45
    line [43, 44, 44]
```

2026-10-18 43 → 2026-10-31 44（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `adaf76f8c22d` · [字段定义](../../DATASET.md)*
