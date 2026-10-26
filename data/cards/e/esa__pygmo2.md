# esa/pygmo2

⭐ 542 · C++ · MPL-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/esa/pygmo2) · [官网](https://esa.github.io/pygmo2/) · 组织维护

**面向科研的 Python 大规模并行优化库**

pygmo 是欧洲航天局（esa）维护的科学 Python 库，为全局与局部优化算法及优化问题提供统一接口，基于异步广义岛屿模型（generalized island model）在大量并行环境中部署优化任务。用户自定义的问题、算法、岛屿等对象通过 pickle/cloudpickle 序列化，README 特别警示反序列化等价于任意代码执行。推荐经 conda-forge 安装，PyPI 仅提供 Linux x86_64 与 aarch64 平台，其他平台需从源码构建。附带 JOSS 论文可供引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 优化算法与优化问题的统一接口
- 基于异步广义岛屿模型的大规模并行计算
- conda-forge 提供多平台安装，PyPI 覆盖 Linux x86_64/aarch64

## 适用场景

- 科研与工程中并行求解全局/局部优化问题
- 多目标优化与元启发式算法实验
- 教学中演示岛屿模型的并行优化

## 场景标签

 · 领域:科学计算/优化

## 证据(README 行号)

> L12: pygmo is a scientific Python library for massively parallel optimization. It is built around the idea
> L13: of providing a unified interface to optimization algorithms and to optimization problems and to make their

## 星数曲线

```mermaid
xychart-beta
    title "esa/pygmo2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 541 --> 543
    line [542, 542]
```

2026-10-18 542 → 2026-10-26 542（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `a1e1f0e9fe7e` · [字段定义](../../DATASET.md)*
