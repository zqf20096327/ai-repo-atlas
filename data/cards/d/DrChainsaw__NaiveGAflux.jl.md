# DrChainsaw/NaiveGAflux.jl

⭐ 44 · Julia · MIT · 推送 2026-04-11 · [GitHub](https://github.com/DrChainsaw/NaiveGAflux.jl) · 个人维护

**用遗传算法为 Flux 模型做神经架构搜索的 Julia 库**

面向 Julia 深度学习框架 Flux 的神经架构搜索库：生成多个不同超参数的候选模型种群，训练若干轮后评估适应度，选择高适应度个体并施加随机变异（增删神经元/层），循环迭代直至产出满足适应度的模型。提供 AutoFlux 应用与简单 fit API（如对 CIFAR10 数据），但 README 指出多数非玩具场景需构建专用应用，库本身提供相关组件。通过 Julia 包管理器安装。

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

- 基于种群的进化式架构搜索：训练-评估-选择-变异循环
- 随机变异支持增删神经元/层
- AutoFlux 应用提供 fit API，可直接对 CIFAR10 训练数据搜索模型

## 适用场景

- 自动搜索 Flux 神经网络的架构与超参数，替代手动调参
- 在训练时长与进化速度之间做权衡控制
- 基于库组件构建定制化的 AutoML 应用

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L6: Neural architecture search for Flux models using genetic algorithms.
> L16: The basic idea is to create not just one model, but a population of several candidate models with different hyperpa

## 星数曲线

```mermaid
xychart-beta
    title "DrChainsaw/NaiveGAflux.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-28 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0af67ac3e13b` · [字段定义](../../DATASET.md)*
