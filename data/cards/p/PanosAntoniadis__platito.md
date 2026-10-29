# PanosAntoniadis/platito

⭐ 28 · Jupyter Notebook · MIT · 推送 2026-10-12 · [GitHub](https://github.com/PanosAntoniadis/platito) · [官网](https://panosantoniadis.github.io/platito/) · 个人维护

**蛋白质生成式分子动力学模型：用 pLM 嵌入提升泛化的转移算子**

PLaTITO 是蛋白质生成式分子动力学（GenMD）开源模型：以可迁移的隐式转移算子（TITO）学习粗粒度转移密度，结合蛋白质语言模型 ESMC 嵌入作为条件信号，从起始 PDB 结构迭代采样生成分子的长程粗粒度轨迹（Cα 坐标，可存为 PDB/DCD）。提供 4 个预训练检查点（3M–36M 参数）、端到端 notebook、采样与训练脚本；推理/训练需先经 EvolutionaryScale Forge API（需 API token）抽取 ESMC 序列嵌入，训练数据为 mdCATH 数据集，默认用 W&B 记录日志。面向计算生物学/机器学习科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从单个 PDB 起始结构并行生成多达 1000 条轨迹（默认 1 ns 步长、可配置温度与 ODE 求解器）
- 以 ESMC 300M/6B 蛋白语言模型嵌入作为条件，提升分布外蛋白质泛化
- 提供 4 个 HuggingFace 预训练检查点（TITO-3M 至 PLaTITO-36M）
- 支持多 GPU DDP 训练（mdCATH 数据集）与论文结果复现流程

## 适用场景

- 为快折叠等分布外蛋白质生成平衡采样轨迹与自由能面分析
- 研究折叠过渡动力学而无需昂贵的传统 MD 模拟
- 基于 mdCATH 数据训练/微调自己的可迁移转移算子模型

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L23: Molecular dynamics (MD) is a central computational tool in physics, chemistry, and biology, enabling quantitative p
> L104: To generate trajectories for any protein, PLaTITO takes as input a starting structure in PDB format and follows Al

## 星数曲线

```mermaid
xychart-beta
    title "PanosAntoniadis/platito 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-29 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `00ddc9b82295` · [字段定义](../../DATASET.md)*
