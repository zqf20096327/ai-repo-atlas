# jianqingzheng/XBCR-net

⭐ 32 · Python · Apache-2.0 · 推送 2025-10-31 · [GitHub](https://github.com/jianqingzheng/XBCR-net) · [官网](https://www.nature.com/articles/s41422-022-00727-6) · 组织维护

**预测抗体-抗原结合的深度学习工具（XBCR-net）**

Cell Research 论文的官方代码实现：基于 TensorFlow/Keras 的 XBCR-net（Cross B-Cell Receptor network），输入 VH、VL 轻重链与 RBD 抗原氨基酸序列，经特征提取与多层感知机输出抗体对多抗原的结合概率，并给出 VH/VL/RBD 局部影响分数图。支持命令行单点与批量推理（结果输出 Excel），也提供可选的训练管线与 Colab notebook 演示。面向计算结构生物学与抗体研发相关研究者。依赖 TensorFlow 2.4.1、Numpy、Pandas，其他版本可能也可用。

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

- 输入 VH/VL 与抗原序列预测抗体-抗原结合概率
- 提供 VH/VL/RBD 局部直方图影响分数图
- 支持单点与批量推理，结果输出 Excel 文件
- 提供 Colab notebook 演示与用户手册

## 适用场景

- 预测抗体对 SARS-CoV-2 及 Omicron 变体 RBD 的结合
- 对我手头的轻重链序列做批量结合预测
- 用可选训练管线在自己的结合数据上重训模型

## 场景标签

 · 领域:计算生物学/抗体工程

## 证据(README 行号)

> L1: XBCR-net (Cross B-Cell Receptor network) for antibody-antigen binding prediction
> L21: 	The active features in the latent space were then processed by Multi-Layer Perceptron to predict the binding proba
> L108: python pred_bcr.py --heavy $HEAVY --light $LIGHT --antig $ANTIG --model_name XBCR_net --data_name binding --model_

## 星数曲线

```mermaid
xychart-beta
    title "jianqingzheng/XBCR-net 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b1d042a13f15` · [字段定义](../../DATASET.md)*
