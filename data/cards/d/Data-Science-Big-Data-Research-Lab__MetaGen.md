# Data-Science-Big-Data-Research-Lab/MetaGen

⭐ 33 · Python · GPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/Data-Science-Big-Data-Research-Lab/MetaGen) · [官网](https://pymetagen.readthedocs.io/) · 组织维护

**面向科研与开发者的元启发式开发与超参数优化框架**

Python 框架，提供元启发式算法开发基类（含运行循环、精英保留、回调）与机器学习/深度学习超参数优化工具：搜索空间支持整数、实数、类别、排列、子集、条件变量与变长结构，可实现动态架构优化。内置随机搜索、禁忌搜索、遗传算法、TPE、CVOA 等算法，兼容 scikit-learn/TensorFlow/PyTorch，支持 seed 复现、断点续跑、TensorBoard 记录与 Ray 集群分布式执行。需 Python 3.10+，经 pip 安装，由塞维利亚大学 Minerva AI Lab 与 Pablo de Olavide 大学 DataLabUPO 团队维护，配套 Neurocomputing 2025 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 元启发式基类：写三个方法即获得运行循环、精英保留与回调
- 搜索空间支持条件变量、变长结构与逐位置范围，可做架构级调参
- checkpoint 断点续跑，结果与不间断运行一致
- Ray 集群分布式执行与 seed 级复现

## 适用场景

- 为回归/分类模型调优超参数
- 在 Ray 集群上分布式运行优化过程
- 快速实现并标准化自定义元启发式算法
- 研究中复现与对比多种优化算法（配套论文与 Colab 笔记）

## 场景标签

 · 领域:机器学习/优化

## 证据(README 行号)

> L12: MetaGen simplifies the development of **metaheuristics** and the **optimization of hyperparameters** in **machine l
> L17: ✔ **Hyperparameter Optimization Tools** – Search spaces with integers, reals, categoricals, permutations, subsets, 
> L20: ✔ **Seamless Integration** – Compatible with `scikit-learn`, `tensorflow`, `pytorch`, and other ML libraries.

## 星数曲线

```mermaid
xychart-beta
    title "Data-Science-Big-Data-Research-Lab/MetaGen 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-31 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `abdc21542a82` · [字段定义](../../DATASET.md)*
