# scDataset/scDataset

⭐ 52 · Jupyter Notebook · MIT · 推送 2026-01-30 · [GitHub](https://github.com/scDataset/scDataset) · 组织维护

**大规模单细胞组学深度学习的数据加载库**

scDataset 是一个 PyTorch IterableDataset 库，用于大规模单细胞组学数据集的可扩展数据加载：支持 AnnData、HuggingFace Datasets、NumPy 数组等数据源，通过块采样与批量获取优化随机访问，处理数十亿样本而无需全部载入内存。v0.2.0 采用策略式 API（Streaming、BlockShuffling、加权采样、类别均衡采样），支持动态划分训练/验证/测试集、多模态 MultiIndexable，以及 fetch/batch 阶段的自定义回调。配套 arXiv 论文（2506.01883），MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 AnnData/HuggingFace Datasets/NumPy 数组等多种数据源
- 块采样与批量获取优化大规模数据随机访问，无需全量载入内存
- 策略式采样：流式、块混淆、加权、类别均衡
- fetch/batch 阶段自定义回调转换

## 适用场景

- 在数十亿样本的单细胞数据集上训练 PyTorch 模型
- 不复制数据或重写文件的情况下动态划分训练/验证/测试集
- 多模态单细胞数据（如 RNA+蛋白）联合索引加载

## 场景标签

 · 领域:生物信息学/单细胞组学

## 证据(README 行号)

> L14: **scDataset** is a flexible and efficient PyTorch `IterableDataset` for large-scale single-cell omics datasets. It 
> L18: - **Flexible Data Source Support**: Integrates seamlessly with AnnData, HuggingFace Datasets, NumPy arrays, PyTorch

## 星数曲线

```mermaid
xychart-beta
    title "scDataset/scDataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-26 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `87aaaa211cdb` · [字段定义](../../DATASET.md)*
