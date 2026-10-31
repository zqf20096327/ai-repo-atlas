# microsoft/sc-AR

⭐ 14 · Jupyter Notebook · MIT · 推送 2026-09-30 · [GitHub](https://github.com/microsoft/sc-AR) · 组织维护

**单细胞数据的自适应重采样训练方法与代码库**

Microsoft 研究团队发布的论文配套代码库，实现 Adaptive Resampling（AR）：基于模型学到的潜在空间结构，在训练过程中在线计算各训练样本的重采样权重，以缓解单细胞转录组数据的类别不平衡与分布外问题。提供 scGen（扰动响应预测）与 scVI（细胞类型分类、基因表达重构）的训练/预测/评估 bash 脚本，数据与模型检查点托管于 Zenodo。另提供可独立集成的 AR 模块 calculate_resampling_weights()，可接入其他机器学习流程或基于基础模型嵌入在训练前一次性计算权重。安装通过 conda 环境文件，Python 3.10.13。

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

- 基于潜在空间的在线自适应重采样，与模型训练同步进行
- 提供 scGen 扰动响应预测与 scVI 分类/重构的完整训练与评估脚本
- AR 模块可集成到其他机器学习流程（calculate_resampling_weights()）
- 模型检查点与数据集公开于 Zenodo

## 适用场景

- 复现论文中单细胞不平衡数据集上的训练与评估结果
- 在自己的单细胞建模流程中加入自适应重采样
- 训练前基于基础模型嵌入调整训练数据分布

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains the code that accompanies our paper, "Adaptive resampling for improved machine learning in 
> L116: We provide an Adaptive Resampling (AR) module that can be integrated into other machine learning pipelines aiming 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/sc-AR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3dd9963e25b1` · [字段定义](../../DATASET.md)*
