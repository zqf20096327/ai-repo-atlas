# dlvu/vugrad

⭐ 33 · Python · MIT · 推送 2025-11-11 · [GitHub](https://github.com/dlvu/vugrad) · [官网](https://dlvu.github.io) · 组织维护

**教学用迷你自动微分库，基于 numpy 的张量反向传播**

面向深度学习教学的微型自动微分系统：以 numpy 为唯一依赖，所有操作面向 numpy 数组（张量值），采用动态图/eager 执行方式在运行时构建计算图，提供反向传播能力。明确声明不适合生产环境。为阿姆斯特丹自由大学 Deep Learning 课程而建，含 MNIST 加载器。与 micrograd/minigrad（标量值）和 minitorch（完整重实现 PyTorch API）等同类教学包相区分。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- numpy 为唯一依赖
- 张量值运算：所有操作基于 numpy 数组
- eager 执行：动态构建计算图

## 适用场景

- 深度学习课程中讲解自动微分与反向传播原理
- 阅读小型源码理解张量计算图的实现机制

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: ```vugrad``` is a miniature autodiff system. Think Pytorch or Tensorflow, but designed to be easy to understand (and
> L10: ```vugrad``` was built for the [Deep Learning course](http://dlvu.github.io) at the Vrije Universiteit Amsterdam.

## 星数曲线

```mermaid
xychart-beta
    title "dlvu/vugrad 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `84c8795f0a85` · [字段定义](../../DATASET.md)*
