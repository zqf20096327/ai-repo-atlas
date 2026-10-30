# erdc/pynirom

⭐ 21 · Python · MIT · 推送 2026-01-31 · [GitHub](https://github.com/erdc/pynirom)

**面向 CFD/浅水流的 Python 非侵入式降阶建模工具库**

美国陆军工程兵团研究与发展中心（ERDC）发布的 Python 工具集，实现非侵入式降阶建模：POD 做线性降维，贪心 RBF 插值或基于 TensorFlow 的神经 ODE（NODE）演化潜空间系数，DMD 提取时空相干结构。附带圆柱绕流、浅水方程、2D Burgers 等基准算例的 Jupyter notebook 与高保真快照数据。依赖 Python 3.x 与 TensorFlow（1.15+/TF2），经 Python 3.7/3.8 测试，通过 conda 环境加 install.sh 安装。

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

- POD、贪心 RBF、TensorFlow 神经 ODE、DMD 四类降阶建模模块
- 圆柱绕流、浅水方程、2D Burgers 基准算例的 Jupyter notebook 示例
- 配套高保真快照数据与各方法对比可视化 notebook

## 适用场景

- 为流动类 PDE 问题构建数据驱动的降阶代理模型
- 对比 POD-RBF、DMD、POD-NODE 等方法在 CFD 算例上的预测
- 科研复现论文中的浅水方程降阶建模实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: A collection of Python implementations of non-intrusive reduced order modeling techniques. This repo provides module
> L6: 3. evolution of latent-space coefficients using a Tensorflow-based implementation of neural ordinary differential eq
> L11: [1] S. Dutta, M. W. Farthing, E. Perracchione, G. Savant, and M. Putti, “A greedy non-intrusive reduced order model

## 星数曲线

```mermaid
xychart-beta
    title "erdc/pynirom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `e59349baa9bd` · [字段定义](../../DATASET.md)*
