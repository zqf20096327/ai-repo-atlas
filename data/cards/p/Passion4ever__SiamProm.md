# Passion4ever/SiamProm

⭐ 30 · Python · MIT · 推送 2026-09-29 · [GitHub](https://github.com/Passion4ever/SiamProm) · [官网](https://doi.org/10.1093/bib/bbae193) · 组织维护

**用孪生网络对比学习识别蓝藻启动子的深度学习模型**

基于孪生网络对比学习与新型非启动子生成策略（PHANTOM 采样）的蓝细菌启动子识别工具：输入 81bp DNA 序列，输出预测标签与置信度（CSV）。提供 Google Colab 免安装推理、本地 conda 环境与 CLI 推理/训练流程，支持 CPU 或 GPU、可调分类阈值，训练提供 phantom/random/cds/partial 四种负采样策略，参数管理基于 Hydra。附论文引用信息，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 孪生网络对比学习架构识别蓝藻启动子
- PHANTOM 等四种负采样策略用于从头训练
- 输入 81bp FASTA，输出含预测与置信度的 CSV
- Colab 免安装推理与本地 conda/CLI 两种使用方式

## 适用场景

- 预测蓝细菌基因组的启动子序列
- 在自己的数据集上从头训练启动子分类模型
- 免费 Colab GPU 上快速试跑推理

## 场景标签

 · 领域:生物信息学/基因组学

## 证据(README 行号)

> L3: **Cyanobacterial promoter identification with Siamese network-based contrastive learning**
> L17: Predict promoters from pasted or uploaded 81 bp sequences on a free Colab GPU, no installation needed.

## 星数曲线

```mermaid
xychart-beta
    title "Passion4ever/SiamProm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2216cc1c4536` · [字段定义](../../DATASET.md)*
