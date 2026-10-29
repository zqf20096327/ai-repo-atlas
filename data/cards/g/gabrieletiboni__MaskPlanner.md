# gabrieletiboni/MaskPlanner

⭐ 32 · 推送 2026-06-25 · [GitHub](https://github.com/gabrieletiboni/MaskPlanner) · [官网](https://gabrieletiboni.github.io/MaskPlanner/) · 组织维护

**从 3D 点云生成多路径长时程轨迹的深度学习模型（机器人喷涂）**

MaskPlanner 是面向以物体为中心运动生成（OCMG）的深度学习方法：输入自由形态 3D 物体的点云，单次前向同时预测局部路径片段并推断“路径掩码”将片段分组为多条路径，覆盖喷涂、焊接等工业场景。论文被 IEEE T-RO 接收，真实 6-DoF 喷涂机器人验证显示生成路径可直接执行。限制：任务不可知、不显式优化涂料沉积。注意：本仓库仅承载项目网站，训练与推理代码已迁移至 vandal-lab/MaskPlanner 仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 3D 点云直接预测多条长时程路径（单次前向）
- 通过“路径掩码”机制同时捕捉局部几何与全局任务需求
- 未见物体覆盖率达 99% 以上（论文报告）
- 真实 6-DoF 喷涂机器人上可直接执行

## 适用场景

- 为自由形态物体自动规划机器人喷涂路径
- 替代人工示教生成多条长时程覆盖轨迹
- 作为下游轨迹优化方法的互补输入

## 场景标签

 · 领域:机器人/3D 深度学习

## 证据(README 行号)

> L1: # MaskPlanner: a Framework for 3D Learning-Based Object-Centric Motion Generation and Applications to Robotic Spray 
> L9: *Abstract:* Object-Centric Motion Generation (OCMG) plays a key role in a variety of industrial applications—such as

## 星数曲线

```mermaid
xychart-beta
    title "gabrieletiboni/MaskPlanner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-29 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `abb0bf2b756d` · [字段定义](../../DATASET.md)*
