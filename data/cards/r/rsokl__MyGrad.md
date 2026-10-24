# rsokl/MyGrad

⭐ 216 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/rsokl/MyGrad) · [官网](https://rsokl.github.io/MyGrad/) · 个人维护

**为 NumPy 补充反向自动微分的轻量张量库**

轻量 Python 库，唯一依赖为 NumPy，通过反向传播计算标量值函数的梯度。API 刻意贴近 NumPy 的行为与语义：支持 ufunc 自动微分（含原地操作与布尔掩码）、视图语义、基础与高级索引。附带 mygrad.nnet 模块提供 N 维卷积、池化与门控循环单元等函数，并可用 Graphviz 渲染计算图。面向希望在 NumPy 生态中直接做反向传播的开发者与教学场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 唯一依赖是 NumPy，pip 一条命令安装
- 支持 ufunc、视图语义、基础/高级索引的反向传播
- mygrad.nnet 提供 N 维卷积、池化、GRU
- 可用 Graphviz 渲染计算图并在 Jupyter 中显示

## 适用场景

- 在 NumPy 代码中直接计算标量损失的梯度
- 机器学习教学示例中演示反向传播
- 检查与可视化计算图结构

## 场景标签

 · 领域:机器学习/科学计算库

## 证据(README 行号)

> L11: MyGrad is a lightweight library that adds automatic differentiation to NumPy – its only dependency is NumPy! It is 
> L20: MyGrad's primary goal is to make automatic differentiation accessible and easy to use across the Python/NumPy ecosy

## 星数曲线

```mermaid
xychart-beta
    title "rsokl/MyGrad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 215 --> 217
    line [216, 216]
```

2026-10-18 216 → 2026-10-24 216（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `11adc8af1bdb` · [字段定义](../../DATASET.md)*
