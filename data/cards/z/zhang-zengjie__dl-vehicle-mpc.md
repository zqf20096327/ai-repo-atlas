# zhang-zengjie/dl-vehicle-mpc

⭐ 15 · MATLAB · BSD-3-Clause · 推送 2026-09-12 · [GitHub](https://github.com/zhang-zengjie/dl-vehicle-mpc) · [官网](https://arxiv.org/abs/2310.02843) · 组织维护

**深度学习轨迹预测驱动的自动驾驶 MPC 演示代码**

作者论文配套的 MATLAB 演示：在高速场景中，用带 LSTM 的循环神经网络根据目标车辆历史轨迹预测其未来轨迹，再基于预测轨迹以模型预测控制（MPC）实现自车避碰的纵向机动。目标车当前版本采用硬编码 'S' 形样条。运行需 MATLAB（R2022b 测试）与 Deep Learning Toolbox，CUDA 与 Parallel Computing Toolbox 为可选项。运行 main.m 即可训练预测器并保存结果与图像。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LSTM 循环神经网络预测目标车辆轨迹
- 基于预测轨迹的 MPC 控制自车安全避让
- 对应 ArXiv 论文的可复现演示代码

## 适用场景

- 复现论文中的 DL-MPC 高速切入避碰场景
- 研究轨迹预测与 MPC 结合的自动驾驶控制方法

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: A demonstration of controlling an ego autonomous vehicle incorporating the target vehicle trajectory predicted by a 
> L11: This demonstration considers a highway scenario where an agent-driving ego vehicle moves along the central lane whi

## 星数曲线

```mermaid
xychart-beta
    title "zhang-zengjie/dl-vehicle-mpc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ff2b33b7c060` · [字段定义](../../DATASET.md)*
