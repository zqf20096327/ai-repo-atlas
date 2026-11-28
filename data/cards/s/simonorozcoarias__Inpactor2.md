# simonorozcoarias/Inpactor2

⭐ 30 · Jupyter Notebook · GPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/simonorozcoarias/Inpactor2) · 个人维护

**用深度学习检测并分类基因组中 LTR 逆转录转座子的工具**

Inpactor2 接收基因组组装的 FASTA 文件，使用多个神经网络（Inpactor2_Detect/Filter/Class）检测 LTR 逆转录转座子、过滤片段与嵌套插入，并分类到 lineage/family 级别，输出 fasta 格式的半策展文库与包含各网络预测概率的表格文件。可选通过 RepeatMasker 进行注释。基于 conda 环境安装，需先组装的基因组（不支持短读长），支持 1-5 个分析周期与多线程执行，附带的 Inpactor2_utils 提供 k-mer 计数与分类网络重训练工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 神经网络检测 LTR-RT 并分类至 lineage/family 级别
- 输出各神经网络的预测概率表供可靠性核查
- 可选集成 RepeatMasker 注释
- 附 Inpactor2_utils：k-mer 频率计算与 Class 网络物种特化重训练

## 适用场景

- 植物基因组组装后的 LTR 逆转录转座子检测与分类
- 生成可后续注释用的 LTR-RT 文库
- 按 lineage 计算核酸序列 k-mer 频率

## 场景标签

 · 领域:生物信息学/基因组分析

## 证据(README 行号)

> L1: # Inpactor2: LTR retrotransposon detector and classificator using Deep Learning
> L6: Inpactor2 was designed and developed to detect reference LTR retrotransposons (LTR-RTs), filtering out those element
> L10: Inpactor2 receives as input a genomic assembly and generates a library of semi-curated and classified LTR-RTs (in f


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `7a71f7171a6a` · [字段定义](../../DATASET.md)*
