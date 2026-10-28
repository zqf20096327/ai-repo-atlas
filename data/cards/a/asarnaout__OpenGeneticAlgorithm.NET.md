# asarnaout/OpenGeneticAlgorithm.NET

⭐ 54 · C# · MIT · 推送 2026-02-14 · [GitHub](https://github.com/asarnaout/OpenGeneticAlgorithm.NET) · 个人维护

**.NET 遗传算法库：用进化计算求解优化问题**

面向 .NET 的类型安全遗传算法库，通过继承 Chromosome<T> 定义解的表示、适应度、变异与修复，以流式 API 配置并运行进化求解。内置 6 种父代选择、4 种交叉、7 种幸存者选择与 4 种终止策略，支持自定义策略扩展，并提供 Adaptive Pursuit 算子自适应选择。给出 TSP、背包、装箱基准测试结果。经 NuGet 以 dotnet add package 安装，需 .NET 运行环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Chromosome<T> 抽象类定义解表示与适应度/变异/修复
- 6 种父代选择、4 种交叉、7 种幸存者选择、4 种终止策略
- Adaptive Pursuit 按运行表现自适应调整算子选择概率
- 继承基类即可注册自定义策略

## 适用场景

- 求解排班、路径规划、资源分配等组合优化问题
- 做神经架构搜索、超参数调优与特征选择
- 作为进化计算研究的实验与算法对比平台

## 场景标签

 · 领域:优化算法/进化计算

## 证据(README 行号)

> L12: OpenGA.Net is a high-performance, type-safe genetic algorithm library that makes evolutionary computation accessibl
> L24: A **Chromosome** in OpenGA.Net represents a potential solution to your optimization problem. It contains **genes** 

## 星数曲线

```mermaid
xychart-beta
    title "asarnaout/OpenGeneticAlgorithm.NET 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-28 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d8a22e8b3000` · [字段定义](../../DATASET.md)*
