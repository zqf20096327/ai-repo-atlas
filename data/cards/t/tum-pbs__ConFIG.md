# tum-pbs/ConFIG

⭐ 124 · Python · MIT · 推送 2026-06-01 · [GitHub](https://github.com/tum-pbs/ConFIG) · [官网](https://tum-pbs.github.io/ConFIG/) · 组织维护

**多损失项优化的无冲突梯度方向方法库（ICLR2025 Spotlight）**

慕尼黑工业大学 Physics-based Simulation 组的 ConFIG 方法官方实现：面向含多个损失项的优化问题（多任务学习、持续学习、物理信息神经网络 PINNs），通过计算损失梯度矩阵的逆得到无冲突更新方向，使最终更新与每个损失梯度的点积恒正且相等，避免优化陷入单一损失的局部极小。提供基于动量的加速变体以降低多损失梯度计算开销。以 Python 包 conflictfree 发布，可几行代码替换标准 PyTorch 训练循环，附文档与论文复现实验。

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

- 通过梯度矩阵求逆获得无冲突更新方向，各损失点积恒正且相等
- momentum-based 变体可降低计算开销至接近标准优化流程
- pip 安装，几行代码接入现有 PyTorch 训练循环
- 论文实验代码可在 experiments 文件夹复现

## 适用场景

- 训练物理信息神经网络（PINNs）时处理初边值与物理方程损失的冲突
- 多任务学习中避免各任务梯度方向冲突
- 持续学习等多损失项场景的优化改进

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L17: ​	The conFIG method is a generic method for optimization problems involving **multiple loss terms** (e.g., Multi-ta
> L93: This project is part of the physics-based deep learning topic in **Physics-based Simulation group** at TUM.

## 星数曲线

```mermaid
xychart-beta
    title "tum-pbs/ConFIG 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 122 --> 125
    line [123, 124, 124]
```

2026-10-18 123 → 2026-10-31 124（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `bd455445c514` · [字段定义](../../DATASET.md)*
