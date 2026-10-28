# amazon-science/synthesizrr

⭐ 19 · Python · Apache-2.0 · 推送 2026-04-04 · [GitHub](https://github.com/amazon-science/synthesizrr) · 组织维护

**论文官方实现：用检索增强的 LLM 生成多样化合成文本数据集**

论文 "SynthesizRR: Generating Diverse Datasets with Retrieval Augmentation"（arXiv:2405.10040）的代码实现：通过检索增强方式从多个 LLM 合成多样、贴近真实分布的文本数据集，供下游训练使用。仓库提供实验复现代码（expts/），运行需自行下载数据集与语料、在源码中设置目录变量，并建议在 AWS Deep Learning AMI 上以 Conda 环境安装依赖、用 Ray 集群执行；语料构建步骤声明需要数百 GB 内存的大型头节点。Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检索增强的 LLM 合成数据集生成（论文 Algorithm 1 的实现）
- 提供复现论文实验的完整流程脚本（data.py/corpus.py/main.py）
- 基于 Ray 集群与 Dask-on-Ray 的分布式执行

## 适用场景

- 复现论文中的合成数据集实验
- 为下游 NLP 任务生成多样化训练数据
- 研究检索增强对合成数据多样性的影响

## 场景标签

 · 领域:NLP/合成数据生成

## 证据(README 行号)

> L1: # SynthesizRR: Generating Diverse Datasets with Retrieval Augmentation
> L3: This repository contains the implementation of the paper "SynthesizRR: Generating Diverse Datasets with Retrieval Au

## 星数曲线

```mermaid
xychart-beta
    title "amazon-science/synthesizrr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `6cdc1724085f` · [字段定义](../../DATASET.md)*
