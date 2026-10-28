# NoRaincheck/TreeGrad

⭐ 21 · Jupyter Notebook · MIT · 推送 2026-08-22 · [GitHub](https://github.com/NoRaincheck/TreeGrad) · 个人维护

**把 LightGBM 树模型转为可微 torch 模型在线微调的 Python 库**

实现 Kontschieder 等人 Deep Neural Decision Forests 的扩展：fit 先训练 LightGBM 集成，partial_fit 将树转换为可微 torch 模型（节点层/路由层/叶层三层结构）并用 Adam 做在线微调，可重复调用持续训练。提供分类器与回归器（mse/huber 损失），树被打包为填充张量执行批量前向计算，支持 L1 正则、温度退火、余弦学习率、可选 torch.compile 及 cpu/cuda/mps 设备选择。依赖 lightgbm、scikit-learn、pytorch。面向需要树模型在线更新能力的开发与科研用户。

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

- LightGBM 集成转换为可微 torch 模型并用 Adam 微调
- partial_fit 支持重复调用的在线持续训练
- 批量张量前向计算，与逐树形式数值一致（~1e-16）
- 支持分类（BCE/交叉熵）与回归（mse/huber）及 cpu/cuda/mps

## 适用场景

- 已训练的 GBDT 模型在新数据上做在线微调
- 把树集成迁移为可梯度优化的神经网络
- 在 UCI 类基准数据上做梯度提升与神经决策森林对比实验

## 场景标签

 · 领域:机器学习库

## 证据(README 行号)

> L5: `TreeGrad` implements a naive approach to converting a Gradient Boosted Tree Model to an Online trainable model. It 
> L36: `fit` trains a LightGBM ensemble; `partial_fit` transfers those trees into a
> L43: mod = tgd.TGDClassifier(num_leaves=31, max_depth=-1, learning_rate=0.1, n_estimators=100)

## 星数曲线

```mermaid
xychart-beta
    title "NoRaincheck/TreeGrad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ae5f33e09386` · [字段定义](../../DATASET.md)*
