# lgalke/text-clf-baselines

⭐ 29 · Python · MIT · 推送 2026-04-21 · [GitHub](https://github.com/lgalke/text-clf-baselines) · 个人维护

**论文实验代码：WideMLP 文本分类与 BoW/图/序列模型对比**

ACL 2022 论文《Bag-of-Words vs. Graph vs. Sequence in Text Classification》的实验代码库。实现 WideMLP 模型，在 20ng、R8、R52、ohsumed、mr 五个文本分类数据集上运行实验，与词袋、文本图（TextGCN）及序列（BERT/GloVe）方法对比。使用需手动从 TextGCN 仓库下载数据到 ./data，修改脚本中的静态路径，并通过 pip install -r requirements.txt 安装依赖；主入口为 run_text_classification.py，experiments 目录含论文实验的 bash 脚本。

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

- models.py 中提供 WideMLP 实现
- 支持 20ng/R8/R52/ohsumed/mr 五个数据集
- 提供 GloVe 分词器实现，其他模型用 BERT tokenizer
- experiments 目录含论文实验所用 bash 脚本

## 适用场景

- 复现论文中的文本分类对比实验
- 在标准基准数据集上运行 WideMLP 模型
- 研究文本图方法与简单 MLP 的效果差异

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # Bag-of-Words vs. Graph vs. Sequence in Text Classification: Questioning the Necessity of Text-Graphs and the Surpr
> L26: - In `models.py`, you find our implementation of the WideMLP.

## 星数曲线

```mermaid
xychart-beta
    title "lgalke/text-clf-baselines 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fed0754c78e6` · [字段定义](../../DATASET.md)*
