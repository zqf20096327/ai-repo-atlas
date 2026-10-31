# binghuang2018/aqml

⭐ 26 · Python · MIT · 推送 2025-11-04 · [GitHub](https://github.com/binghuang2018/aqml) · 组织维护

**基于 amon 片段的量子机器学习包，用于量子化学能量预测**

由巴塞尔大学团队维护的 Python/Fortran/C++ 混合包：将大分子拆解为基本构建块（amons），自动采样最具代表性的训练集，配合 SLATM/BAML 等分子表示与 KRR、多保真 KRR 方法预测分子总能量等量子化学性质。支持对接 G09、ORCA4、MOLPRO、CASINO 生成参考数据，提供命令行 genamon 与 Python API，仅支持 Linux/macOS，源码编译安装，oechem 为可选（需许可，可用 RDKit 替代）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Amons 选择算法自动采样与查询最相关的训练集
- SLATM/aSLATM/BAML 等多种分子表示
- KRR 与多保真 KRR、深度神经网络势（开发中）
- 对接 G09/ORCA4/MOLPRO/CASINO 自动生成量子化学参考数据

## 适用场景

- 预测大分子或固体的总能量等量子化学性质
- 自动挑选最具代表性的小片段训练集降低计算成本
- 批量生成分子片段并构建表示向量用于机器学习

## 场景标签

 · 领域:量子化学/科学计算

## 证据(README 行号)

> L4: AQML is a mixed Python/Fortran/C++ package, intends to simulate quantum chemistry problems through the use of **amon
> L26:  - KRR and multi-fidelity KRR

## 星数曲线

```mermaid
xychart-beta
    title "binghuang2018/aqml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-31 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d39318cbd51d` · [字段定义](../../DATASET.md)*
