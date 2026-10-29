# HiPerSimLab/PECANN

⭐ 26 · Jupyter Notebook · MIT · 推送 2026-03-30 · [GitHub](https://github.com/HiPerSimLab/PECANN) · 组织维护

**物理与等式约束神经网络：用增广拉格朗日法求解正/逆 PDE 问题**

科研代码库，实现 Physics and Equality Constrained Artificial Neural Networks（PECANN）方法：将 PDE 求解表述为约束优化问题，用增广拉格朗日法（ALM）施加 PDE 与边界条件及高保真数据约束，支持正问题、逆问题与多保真度数据融合。代码以自包含 Jupyter notebook 形式提供，依赖 PyTorch、numpy、scipy、matplotlib。README 声明已有后续工作 PECANN-CAPU 与并行版本。发表于 J. Comput. Phys.，由 NSF 资助、爱达荷大学/匹兹堡大学相关人员维护。

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

- 增广拉格朗日法将 PDE 与边界条件表述为硬约束
- 支持正问题与逆问题及多保真度数据融合
- 自包含 Jupyter notebook 形式提供代码

## 适用场景

- 求解偏微分方程的正问题与逆问题
- 在物理约束神经网络中融合多保真度数据
- 科研复现与对比 PINN 类方法实验

## 场景标签

 · 领域:科学机器学习/计算物理

## 证据(README 行号)

> L1: ## PECANNs: Physics and Equality Constrained Artificial Neural Networks: Application to Forward and Inverse Problems
> L9: Physics-informed neural networks (PINNs) have been proposed to learn the solution of partial differential equations 

## 星数曲线

```mermaid
xychart-beta
    title "HiPerSimLab/PECANN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7195166617af` · [字段定义](../../DATASET.md)*
