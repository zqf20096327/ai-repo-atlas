# aromanro/MachineLearning

⭐ 27 · C++ · GPL-3.0 · 推送 2026-09-26 · [GitHub](https://github.com/aromanro/MachineLearning) · 个人维护

**从线性回归到多层感知机的 C++ 机器学习从零实现**

C++ 实现的机器学习教学/实验项目，不依赖机器学习库，仅使用 Eigen 做线性代数。内容从简单线性回归、广义线性模型、多项式回归、逻辑回归、Softmax 逐步推进到多层感知机，附带多种随机梯度下降求解器（momentum、Nesterov、AdaGrad、RMSProp、Adam、AdamW）。使用 Gnuplot 显示图表，加载 Iris 与 EMNIST 数据集；EMNIST 训练默认参数下需要至少 32GB 内存，x64 Release 启用 OpenMP 与 AVX2。作者可能后续扩展卷积网络，README 声明部分增强项列在 Issues 中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从线性回归到多层感知机的渐进式 C++ 实现，不使用现成机器学习库
- 多种梯度下降求解器：momentum、Nesterov、AdaGrad、RMSProp、Adam、AdamW
- Gnuplot 图表输出与 Iris/EMNIST 数据集加载
- x64 Release 启用 OpenMP 与 AVX2，可用环境变量限制 Eigen 线程数

## 适用场景

- 学习线性回归到神经网络各模型的底层实现原理
- 参考多种梯度下降求解器的实现细节
- 在 Iris/EMNIST 数据集上运行并查看训练图表

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L11: I've seen plenty of misconceptions about neural networks on some reddit groups and on some forums and although the 
> L21: The goal of this project is to build models starting from a very simple one and making them more complex up to a ne
> L118: Here it is, the goal I estabilished when I started this project (I might go further in the future, but for now it 

## 星数曲线

```mermaid
xychart-beta
    title "aromanro/MachineLearning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e562cba922d6` · [字段定义](../../DATASET.md)*
