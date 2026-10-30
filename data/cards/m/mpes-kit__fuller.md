# mpes-kit/fuller

⭐ 15 · Jupyter Notebook · MIT · 推送 2026-05-19 · [GitHub](https://github.com/mpes-kit/fuller) · [官网](https://mpes-kit.github.io/fuller/) · 组织维护

**从光电子能谱数据重建电子能带结构的机器学习 Python 库**

面向凝聚态物理与材料科学研究者的 Python 包：以 TensorFlow 实现的马尔可夫随机场（MRF）模型，从光电子能谱（ARPES/MPES）数据重建并参数化电子能带结构。核心类 MrfRec 提供数据预处理（含 MCLAHE 对比度直方图均衡）与并行优化重建方法，可用 DFT 计算结果初始化。示例数据为 WSe2 三维光电子能谱（14 条价带）。限制：当前仅支持 TensorFlow 1（1.14 起），CPU 与 GPU 版本均可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 马尔可夫随机场模型实现能带结构重建与参数化
- MrfRec 类提供 MCLAHE 强度归一化与并行优化重建
- 支持 DFT 计算结果初始化优化
- 提供 mpes_reconstruction_mrf.ipynb 示例笔记本

## 适用场景

- 从 ARPES/MPES 实验数据重建材料电子能带结构
- 对实测能谱做强度归一化等预处理
- 基于重建结果进行能带参数化分析

## 场景标签

 · 领域:材料科学/凝聚态物理

## 证据(README 行号)

> L8: This Python package comprises a set of tools to reconstruct and parametrize the electronic band structure (EBS) from
> L9: Xian & Stimper et al. (2020) in TensorFlow.

## 星数曲线

```mermaid
xychart-beta
    title "mpes-kit/fuller 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `761fb00002f5` · [字段定义](../../DATASET.md)*
