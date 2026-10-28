# e3nn/e3nn-jax

⭐ 235 · Python · Apache-2.0 · 推送 2026-04-01 · [GitHub](https://github.com/e3nn/e3nn-jax) · 组织维护

**JAX 实现的 E(3) 等变神经网络库**

e3nn 的 JAX 版本库，提供三维欧几里得群等变神经网络构建模块，用于处理 3D 点云等旋转平移等变任务。与 PyTorch 版本的主要差异是引入 IrrepsArray 类，将不可约表示与数据数组绑定在一起。README 给出基于 MACE 模型在 RTX A5000 上的训练速度对比，并提示查阅 CHANGELOG 关注破坏性变更。通过 pip 安装发布版或 GitHub 源码版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 E(3) 等变神经网络构建模块的 JAX 实现
- IrrepsArray 类将 irreps 与数据数组绑定
- 提供 pip 安装发布版与 GitHub 源码版两种途径

## 适用场景

- 构建处理 3D 点云的旋转平移等变模型
- 在 JAX 生态中复用 e3nn 的等变层
- 科学计算中需要等变性约束的神经网络研究

## 场景标签

 · 领域:科学计算/几何深度学习

## 证据(README 行号)

> L34: The main difference is the presence of the class `IrrepsArray`.
> L35: `IrrepsArray` contains the irreps (`Irreps`) along with the data array.

## 星数曲线

```mermaid
xychart-beta
    title "e3nn/e3nn-jax 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 233 --> 236
    line [234, 235, 235]
```

2026-10-18 234 → 2026-10-28 235（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c488c80377a8` · [字段定义](../../DATASET.md)*
