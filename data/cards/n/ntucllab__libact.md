# ntucllab/libact

⭐ 791 · Python · BSD-2-Clause · 推送 2026-10-12 · [GitHub](https://github.com/ntucllab/libact) · [官网](http://libact.readthedocs.org/) · 组织维护

**Python 池式主动学习库：多种查询策略与自动策略选择**

面向机器学习研究者的池式主动学习 Python 库，实现 14 种查询策略（不确定性采样、CoreSet、BALD、QUIRE、ALBL 元算法等），内置 LogisticRegression/SVM/Perceptron 模型并提供 SklearnAdapter 封装任意 scikit-learn 估计器；支持批量查询与多样性感知批次。构建基于 meson/meson-python，含 C 扩展模块，需 BLAS/LAPACKE 系统依赖，Windows 用户建议使用 WSL。由台大计算学习实验室团队维护，附 arXiv 技术报告与 readthedocs 文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 种主动学习查询策略，含 ALBL 多臂老虎机元算法自动选择策略
- 支持批量查询 make_query_batch 与 DiversityWeightedMeta 多样性感知批次
- SklearnAdapter/SklearnProbaAdapter 封装任意 scikit-learn 估计器
- 提供 9 个示例脚本与单元测试套件

## 适用场景

- 标注预算有限时挑选最有信息量的样本进行标注
- 对比不同主动学习策略的性能
- 在 scikit-learn 模型上快速搭建主动学习流程

## 场景标签

 · 领域:机器学习/数据高效学习

## 证据(README 行号)

> L14: `libact` is a Python package designed to make active learning easier for
> L152: |Strategy|Type|Description|

## 星数曲线

```mermaid
xychart-beta
    title "ntucllab/libact 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 790 --> 792
    line [791, 791]
```

2026-10-18 791 → 2026-10-25 791（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8bfe20897f06` · [字段定义](../../DATASET.md)*
