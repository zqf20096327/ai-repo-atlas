# rclement/sqlite-ml

⭐ 56 · Python · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/rclement/sqlite-ml) · 个人维护

**SQLite 机器学习扩展：用 SQL 函数在库内训练模型并预测**

基于 Python SQLite3 加载的 SQLite 扩展，注册 sqml_load_dataset、sqml_train、sqml_predict、sqml_predict_batch 等 SQL 函数，支持回归与分类任务（如逻辑回归、SVM），模型在实验内按得分自动部署，无需修改预测查询即可切换更优模型。面向在 SQLite 中完成数据分析与预测的开发者，提供 Datasette 插件 datasette-ml 与 SQLite-Utils 插件 sqlite-utils-ml 两种接入方式。当前限制：尚不可作为原生 SQLite 扩展在任意 SQLite 环境加载。

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

- SQL 函数完成训练与预测：sqml_train / sqml_predict / sqml_predict_batch
- 支持回归与分类，算法含逻辑回归、SVC
- 实验内新模型得分更高时自动部署，预测查询无需改动
- 内置 sqml_load_dataset 加载 Scikit-Learn 标准数据集

## 适用场景

- 在 SQLite 数据旁直接训练分类/回归模型，省去数据导出与回写
- 用纯 SQL 流水线把预测嵌入既有应用查询
- 在 Datasette 或 SQLite-Utils 中做即席数据分析加预测

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: Train machine learning models and run predictions directly from your SQLite database.
> L83: SELECT sqml_train(
> L106: SELECT

## 星数曲线

```mermaid
xychart-beta
    title "rclement/sqlite-ml 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-26 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `06d4f0bda688` · [字段定义](../../DATASET.md)*
