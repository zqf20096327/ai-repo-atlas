# riscy/machine_learning_linear_models

⭐ 18 · Python · MIT · 推送 2025-12-23 · [GitHub](https://github.com/riscy/machine_learning_linear_models) · 个人维护

**线性回归、降秩回归与线性系统辨识的教学演示代码**

一个 Python 演示项目：对观测向量 X 到结果向量 Y 的映射，比较三种线性模型——多元线性回归、降秩回归（RRR）与基于子空间方法的线性系统辨识。示例展示当数据为低秩或来自线性动态系统时，匹配数据假设的模型能取得更低的测试误差。兼容 Python 2.7 与 3+，运行 python demo.py 即可在满秩、低秩、线性系统三类合成数据上输出训练/测试误差对比。作者为博士生个人，实现参考 Tijl De Bie 2005 年的子空间系统辨识讲演。

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

- 三种线性模型实现：多元回归、降秩回归（rank 可设）、线性动态系统辨识
- 三类合成数据（满秩/低秩/线性系统）上的误差对比演示
- 兼容 Python 2.7 与 3+

## 适用场景

- 学习不同线性模型适用的数据假设
- 作为降秩回归或系统辨识的参考实现
- 课堂或自学中复现模型误差对比实验

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L11:  This small demo showcases a few simple but different linear models for mapping
> L21:  system identification technique (~system_identifier.py~) can result in big

## 星数曲线

```mermaid
xychart-beta
    title "riscy/machine_learning_linear_models 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a9b23b6ba39a` · [字段定义](../../DATASET.md)*
