# lucidrains/rigidformer

⭐ 32 · Python · MIT · 推送 2026-08-11 · [GitHub](https://github.com/lucidrains/rigidformer) · 个人维护

**RigidFormer 论文的 PyTorch 实现：用 Transformer 学习刚体动力学**

MIT 与 Meta 合作的 RigidFormer（Learning Rigid Dynamics using Transformers）的第三方 PyTorch 实现，提供 Rigidformer 模型类，可用 torch 导入并在数据上训练，学习刚体动力学并做轨迹 rollout 预测。附带 Box2D 合成数据示例（摩擦滑动与碰撞接触两种动力学），运行后输出训练损失图、held-out rollout 对比图与相对匀速基线的 rollout 误差图。通过 pip 安装，示例用 uv 运行。实现自论文引用条目推断为 2026 年发表的最新研究工作。

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

- Rigidformer 模型的 PyTorch 实现，可 import 后自行训练
- Box2D 合成数据示例覆盖平滑摩擦与尖锐接触两类动力学
- 输出训练损失、held-out rollout 对比与相对匀速基线的误差图

## 适用场景

- 复现 RigidFormer 论文的刚体动力学学习方法
- 在 Box2D 合成数据上验证刚体轨迹预测
- 作为刚体动力学学习研究的代码基础

## 场景标签

 · 领域:机器学习/物理仿真

## 证据(README 行号)

> L5: Implementation of RigidFormer, Learning Rigid Dynamics using Transformers, out of MIT and Meta
> L16: import torch
> L24: Train on a synthetic Box2D dataset of boxes sliding on the ground under friction and coming to rest, and save `exam

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/rigidformer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-31 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1e07f24c108d` · [字段定义](../../DATASET.md)*
