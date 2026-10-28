# bio-ontology-research-group/deepgo

⭐ 88 · Python · 推送 2026-10-01 · [GitHub](https://github.com/bio-ontology-research-group/deepgo) · [官网](http://deepgo.bio2vec.net) · 组织维护

**蛋白质功能预测模型：从序列与 PPI 网络预测 GO 功能**

DeepGO 通过深度神经网络从蛋白质序列和蛋白质-蛋白质交互（PPI）网络中学习特征，并按基因本体（GO）层次结构进行分类，预测蛋白质功能；PPI 网络特征采用神经符号方法学习知识图谱表示。仓库提供模型构建、训练与评估脚本（含仅序列版与序列+网络嵌入版），运行预测需下载提供的数据包并在系统安装 diamond 程序，结果输出到 results.tsv。面向生物信息学研究人员，附 2017 年 Bioinformatics 论文引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度神经网络学习序列与 PPI 网络特征
- 按基因本体（GO）层次结构进行功能分类
- 提供训练、数据准备与性能评估（FFPred/GOFDR/BLAST）脚本
- predict_all.py 对输入 FASTA 文件输出预测结果

## 适用场景

- 根据蛋白质序列预测其基因本体功能
- 复现论文中的模型训练与性能评估
- 对比 DeepGO 与 FFPred、GOFDR、BLAST 的预测效果

## 场景标签

 · 领域:生物信息学/计算生物学

## 证据(README 行号)

> L3: DeepGO is a novel method for predicting protein functions using protein sequences and protein-protein interaction (P
> L33: Maxat Kulmanov, Mohammed Asif Khan, Robert Hoehndorf; DeepGO: Predicting protein functions from sequence and intera

## 星数曲线

```mermaid
xychart-beta
    title "bio-ontology-research-group/deepgo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 87 --> 89
    line [88, 88]
```

2026-10-18 88 → 2026-10-28 88（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4b4c1d58fa1a` · [字段定义](../../DATASET.md)*
