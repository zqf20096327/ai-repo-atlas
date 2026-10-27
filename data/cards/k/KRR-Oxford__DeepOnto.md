# KRR-Oxford/DeepOnto

⭐ 325 · Python · Apache-2.0 · 推送 2026-09-04 · [GitHub](https://github.com/KRR-Oxford/DeepOnto) · [官网](https://krr-oxford.github.io/DeepOnto/) · 组织维护

**面向本体工程的深度学习 Python 包：本体处理与匹配/推理工具**

牛津 KRR 组维护的 Python 库，通过 JPype 桥接 Java OWLAPI（4.5.22）进行本体加载、推理、剪枝、语言化、投影与规范化，并以 PyTorch 为深度学习框架。在此之上提供 BERTMap 本体匹配系统、Bio-ML 资源、BERTSubs 子归属预测、OntoLAMA 语言模型评测等工具。基础用法不依赖 GPU，高效模型训练需 CUDA 可用；OntoLAMA 的 openprompt 依赖在 macOS M1 存在冲突，设为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 OWLAPI+JPype 的本体加载、推理、剪枝、语言化、投影与 EL 规范化模块
- BERTMap/Bio-ML/BERTSubs/OntoLAMA 等本体匹配与子归属推断工具
- pip 安装，含 ontolama、bioregistry 可选依赖组

## 适用场景

- 构建与处理 OWL 本体并做推理、剪枝与子本体抽取
- 执行 BERT 类本体匹配（本体对齐）任务
- 用语言模型做本体子归属推断与评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L27: $\textsf{DeepOnto}$ aims to provide building blocks for implementing deep learning models, constructing resources, 
> L23:  A package for ontology engineering with deep learning.
> L111: - **BERTMap** [1] is a BERT-based ontology matching (OM) system originally developed in repo but is now maintained

## 星数曲线

```mermaid
xychart-beta
    title "KRR-Oxford/DeepOnto 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 322 --> 326
    line [323, 325, 325]
```

2026-10-18 323 → 2026-10-27 325（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e42198368018` · [字段定义](../../DATASET.md)*
