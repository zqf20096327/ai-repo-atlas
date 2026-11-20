# liuyao12/ConvNets-PDE-perspective

⭐ 20 · Jupyter Notebook · MIT · 推送 2026-11-13 · [GitHub](https://github.com/liuyao12/ConvNets-PDE-perspective) · 个人维护

**研究者协作项目：从偏微分方程视角解释并改进卷积网络**

开放协作研究项目，探讨卷积网络的 PDE（偏微分方程）视角：论证 3x3 卷积可视为二阶微分算子，ResNet 的恒等跳跃连接相当于用前向欧拉法数值求解非线性 PDE，训练则对应反问题。基于该视角提出架构调整建议，如 Neumann 边界条件（reflect padding）、双曲系统正则化、可变系数卷积（附 torchvision ResNet Bottleneck 代码示例）。以 README 形式邀请任何人在讨论区批评、提问、提交代码或结果，采用类 Polymath 的开放协作模式，无明确既定目标，也无可运行完整代码或安装说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 论证 3x3 卷积+跳跃连接等价于数值求解非线性 PDE
- 给出 ConvNet 与 PDE 概念的逐项对照表
- 提出可变系数、Neumann 边界条件等架构改进思路
- 类 Polymath 开放协作模式，接受任何人的讨论与 PR

## 适用场景

- 寻找 ConvNet 架构设计的理论解释框架
- 参与开放协作讨论或贡献实验代码与结果
- 了解深度学习与微分方程结合的相关文献和 workshops

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: # ConvNets from the PDE perspective
> L5: * Everyone is invited to **open a discussion**, to offer criticisms, ask for clarifications, suggest or develop new 
> L48: The training of a ConvNet would be an **inverse problem**: we know the solutions (dataset), and look for the PDE th

## 星数曲线

```mermaid
xychart-beta
    title "liuyao12/ConvNets-PDE-perspective 星数(近 2 点)"
    x-axis ["2026-11-13", "2026-11-20"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-11-13 20 → 2026-11-20 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `1fd3d473a5d2` · [字段定义](../../DATASET.md)*
