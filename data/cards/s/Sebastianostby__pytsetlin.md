# Sebastianostby/pytsetlin

⭐ 22 · Python · MIT · 推送 2025-12-02 · [GitHub](https://github.com/Sebastianostby/pytsetlin) · 个人维护

**Coalesced Tsetlin Machine 的纯 Python 实现库，供实验与研究**

用纯 Python 编写的 Coalesced Tsetlin Machine（一种机器学习模型）低代码实现，定位为易用、便于对照论文理解理论概念，而非追求速度或功能完备。部分函数兼容 Numba 编译以提升性能。支持从 TsetlinMachine 对象直接考察 TM 结构、训练中或训练后保存/加载状态并用其做预测。提供 MNIST、IMDB 等数据加载示例；输入须为二值数据（特征 uint8、标签 uint32）。

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

- 纯 Python 实现的 Coalesced Tsetlin Machine，代码可对照论文理论
- 部分函数兼容 Numba 编译
- 支持保存/加载 TM 状态并用于预测
- 可从对象层面直接考察 TM 结构

## 适用场景

- 快速实验 Tsetlin Machine 的新想法
- 对照论文理解 TM 内部结构与记忆
- 在 MNIST/IMDB 等二值数据上训练与预测

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: A low-code, feature-POOR, Pythonic implementation of a Coalesced Tsetlin Machine. This is not intended to be a featu
> L4: TMU](https://github.com/cair/tmu) and green-tsetlin for that. However, it's intended to be an easy-to-use TM program

## 星数曲线

```mermaid
xychart-beta
    title "Sebastianostby/pytsetlin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `71c1c2a93de0` · [字段定义](../../DATASET.md)*
