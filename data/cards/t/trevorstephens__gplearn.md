# trevorstephens/gplearn

⭐ 1,893 · Python · BSD-3-Clause · 推送 2026-08-14 · [GitHub](https://github.com/trevorstephens/gplearn) · [官网](http://gplearn.readthedocs.io/) · 个人维护

**Python 遗传编程库：面向符号回归与二分类**

gplearn 用 Python 实现遗传编程（GP），刻意限定于符号回归问题，API 仿照并兼容 scikit-learn。通过种群随机公式进化与遗传操作拟合数学表达式，保留熟悉的 fit/predict 接口，可与 scikit-learn 的 pipeline 和 grid search 模块配合使用。提供 SymbolicRegressor（回归）、SymbolicClassifier（二分类）与 SymbolicTransformer（自动特征工程变换）三种估计器，构建于 scikit-learn 之上，安装需较新版本的 scikit-learn。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SymbolicRegressor / SymbolicClassifier / SymbolicTransformer 三种估计器
- 保留 scikit-learn fit/predict API，兼容其 pipeline 与 grid search
- 通过种群进化与遗传操作搜索最优数学表达式
- SymbolicTransformer 用于自动特征工程

## 适用场景

- 用符号回归从数据中找出可解释的数学表达式
- 在 scikit-learn 流水线中做二分类或特征变换
- 自动生成特征以辅助下游回归/分类任务

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L30: `gplearn` implements Genetic Programming in Python, with a `scikit-learn <http://scikit-learn.org>`_ inspired and c
> L34: Symbolic regression is a machine learning technique that aims to identify an underlying mathematical expression tha

## 星数曲线

```mermaid
xychart-beta
    title "trevorstephens/gplearn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 1892 --> 1894
    line [1893, 1893]
```

2026-10-18 1,893 → 2026-10-22 1,893（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8bf00cb7810a` · [字段定义](../../DATASET.md)*
