# LAMDA-NJU/Deep-Forest

⭐ 960 · Python · NOASSERTION · 推送 2026-05-18 · [GitHub](https://github.com/LAMDA-NJU/Deep-Forest) · [官网](https://deep-forest.readthedocs.io) · 组织维护 · 中文 README

**Deep Forest 2021.2.1 的 Python 框架实现，面向表格数据建模**

南京大学 LAMDA 实验室维护的 DF21，是 Deep Forest（周志华、冯霁提出）2021.2.1 版本的实现，提供 CascadeForestClassifier 与 CascadeForestRegressor，通过 sklearn 风格 API 完成分类与回归任务。针对表格数据优化，参数调优工作量较少；处理图像等结构化数据的 multi-grained scanning 部分不在本实现范围内，需参考原始 gcForest 实现。以 pip 安装的 Python 库形式提供，附文档与论文引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 Deep Forest 2021.2.1 算法（级联森林）
- 提供分类器与回归器，sklearn 风格 API
- 针对表格数据的树集成方法，参数调优负担较少

## 适用场景

- 在表格数据上训练分类或回归模型
- 作为树集成方法（随机森林/GBDT）之外的建模选项
- 复现或研究 Deep Forest 算法

## 场景标签

 · 领域:机器学习/算法库

## 证据(README 行号)

> L23: **DF21** is an implementation of `Deep Forest <https://arxiv.org/pdf/1702.08835.pdf>`__ 2021.2.1. It is designed to
> L30: DF21 offers an effective & powerful option to the tree-based machine learning algorithms such as Random Forest or G

## 星数曲线

```mermaid
xychart-beta
    title "LAMDA-NJU/Deep-Forest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 959 --> 961
    line [960, 960]
```

2026-10-18 960 → 2026-10-31 960（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `cab2e84cb065` · [字段定义](../../DATASET.md)*
