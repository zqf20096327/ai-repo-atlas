# kyegomez/Open-AF3

⭐ 808 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/kyegomez/Open-AF3) · [官网](https://discord.gg/7VckQVxvKk) · 个人维护

**AlphaFold 3 论文的 PyTorch 开源复现，预测生物分子结构**

由个人开发者维护的 AlphaFold 3（DeepMind 论文）PyTorch 实现项目，与 Google/DeepMind 无关联。提供 pip 安装的 alphafold3 包，包含 GeneticDiffusion 模块与完整模型前向传播示例；Notes 部分梳理了 Pairformer、扩散模块、置信度头等论文机制。Todo 清单显示输入嵌入、模板模块、MSA 嵌入、recycling 等组件尚未完成，训练数据集也待推送到 Hugging Face，属于进行中的复现工作。

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

- pip 可安装的 AlphaFold 3 PyTorch 实现包
- 提供 GeneticDiffusion 与完整模型前向传播代码示例
- Notes 梳理 Pairformer（48 blocks）、扩散去噪、置信度头等论文机制

## 适用场景

- 学习 AlphaFold 3 论文的架构与扩散机制实现
- 跟踪 AlphaFold 3 开源复现的进展
- 在 PyTorch 中实验蛋白质结构预测模块

## 场景标签

 · 领域:计算生物学/AI

## 证据(README 行号)

> L1: # Open-AlphaFold
> L3: Open source Implementation of Alpha Fold from the paper: "Accurate structure prediction of biomolecular interactions
> L102: # Todo

## 星数曲线

```mermaid
xychart-beta
    title "kyegomez/Open-AF3 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 807 --> 809
    line [808, 808]
```

2026-10-18 808 → 2026-10-28 808（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `6452b00b1354` · [字段定义](../../DATASET.md)*
