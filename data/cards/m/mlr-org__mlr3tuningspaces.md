# mlr-org/mlr3tuningspaces

⭐ 14 · R · 推送 2026-07-25 · [GitHub](https://github.com/mlr-org/mlr3tuningspaces) · [官网](https://mlr3tuningspaces.mlr-org.com) · 组织维护

**mlr3 生态的超参数优化搜索空间集合，供 R 用户调参**

mlr3 生态的 R 包，收录来自四篇科学论文的机器学习算法超参数搜索空间，覆盖 glmnet、ranger、rpart、svm、xgboost、mlp、tab_resnet、ft_transformer 等学习器。用户通过 lts() 函数将默认或指定搜索空间附加到学习器上，即可在 mlr3 调参流程中使用；搜索空间以字典 mlr_tuning_spaces 组织，可通过 add_tuning_space() 贡献来自同行评审论文的新空间。支持与 mlr3pipelines 结合在流水线中应用。面向使用 mlr3 做超参数优化的 R 开发者与科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 收录 Bischl et al. (2023)、Kuehn et al. (2018) 等四篇论文的搜索空间
- lts() 函数为学习器附加默认或指定搜索空间
- mlr_tuning_spaces 字典统一管理全部搜索空间
- 支持贡献来自同行评审论文的新搜索空间

## 适用场景

- 为 mlr3 学习器快速套用论文中的超参数搜索空间
- 在 AutoML 流程中免去手工定义搜索范围
- 复现论文调参设置或按论文添加新搜索空间集合

## 场景标签

 · 领域:机器学习/AutoML

## 证据(README 行号)

> L12: *mlr3tuningspaces* is a collection of search spaces for hyperparameter
> L14: It features ready-to-use search spaces for many popular machine learning
> L15: algorithms. The search spaces are from scientific articles and work for

## 星数曲线

```mermaid
xychart-beta
    title "mlr-org/mlr3tuningspaces 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a56bbadbe4e8` · [字段定义](../../DATASET.md)*
