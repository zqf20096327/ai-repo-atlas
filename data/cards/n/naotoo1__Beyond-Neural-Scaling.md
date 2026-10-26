# naotoo1/Beyond-Neural-Scaling

⭐ 35 · Python · MIT · 推送 2025-10-30 · [GitHub](https://github.com/naotoo1/Beyond-Neural-Scaling) · 个人维护

**面向深度与原型模型的数据剪枝算法实现，超越幂律缩放**

论文《Beyond neural scaling laws: beating power law scaling via data pruning》(arXiv:2206.14486) 的实现，提供自监督学习度量进行数据剪枝的命令行脚本，覆盖深度模型（计算机视觉示例，dataprune.py）与原型模型（LVQ 示例，dataprune1.py）。README 说明最优剪枝算法可使缩放从幂律转变为指数律，并提及 TensorFlow 移动/边缘设备目标检测与 LVQ 的应用示例。依赖 Python 3.10、PyTorch 1.11、ProtoTorch 0.7.5，MIT 许可。未给出 pip 安装命令。

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

- 自监督学习度量的数据剪枝命令行工具
- 同时覆盖深度模型与 LVQ 原型模型
- 对应 arXiv:2206.14486 论文的实现

## 适用场景

- 复现数据剪枝论文实验
- 对计算机视觉数据集做剪枝实验
- 研究原型模型的数据剪枝效果

## 场景标签

 · 领域:机器学习/研究代码

## 证据(README 行号)

> L8:  Implementation of beyond neural scaling beating power laws through data pruning.
> L10: The implementation covers deep learning and prototype-based models and shows how the optimal pruning algorithm can 
> L31: arXiv preprint arXiv:2206.14486 (2022).

## 星数曲线

```mermaid
xychart-beta
    title "naotoo1/Beyond-Neural-Scaling 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-26 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `73c9781fe878` · [字段定义](../../DATASET.md)*
