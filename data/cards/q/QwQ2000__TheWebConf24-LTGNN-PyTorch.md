# QwQ2000/TheWebConf24-LTGNN-PyTorch

⭐ 21 · Python · Apache-2.0 · 推送 2026-05-22 · [GitHub](https://github.com/QwQ2000/TheWebConf24-LTGNN-PyTorch) · 个人维护

**LTGNN 论文官方 PyTorch 实现：线性时间 GNN 做可扩展推荐**

TheWebConf'24 论文 Linear-Time Graph Neural Networks for Scalable Recommendations 的 PyTorch 官方代码，代码库改编自 LightGCN-pytorch。提供 main.py 训练入口，支持 yelp2018、alibaba-ifashion 等数据集，可调 layer、recdim、appnp_alpha、num_neighbors 等超参数；Amazon-Large 数据集通过 Google Drive 提供，也可按论文 4.1 节从 Amazon Review Data 自行构建。理论分析（邻居采样方差缩减、前向过程收敛到 PPNP）见作者硕士论文。面向科研复现人群。

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

- LTGNN 图神经网络推荐模型的官方实现
- 支持 yelp2018 / alibaba-ifashion 等多个数据集与超参数配置
- Amazon-Large 数据集可直接下载或按论文说明自建

## 适用场景

- 复现 TheWebConf'24 LTGNN 论文实验结果
- 在 Yelp/Alibaba 等数据集上运行 GNN 推荐训练
- 基于 LightGCN 代码库做推荐系统研究扩展

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L3: This is the Pytorch implementation for our TheWebConf'24 paper "**Linear-Time Graph Neural Networks for Scalable Rec
> L18: ` cd code && python main.py --decay=2e-4 --lr=0.0015 --layer=1 --seed=2020 --dataset="yelp2018" --topks="[20]" --re

## 星数曲线

```mermaid
xychart-beta
    title "QwQ2000/TheWebConf24-LTGNN-PyTorch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `9b952de1aff1` · [字段定义](../../DATASET.md)*
