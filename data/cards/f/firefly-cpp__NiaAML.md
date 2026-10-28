# firefly-cpp/NiaAML

⭐ 33 · Python · MIT · 推送 2026-04-26 · [GitHub](https://github.com/firefly-cpp/NiaAML) · 组织维护

**给开发者的 Python AutoML 框架：自动组装优化分类/回归流水线**

基于自然启优化算法的 Python 自动化机器学习框架，使用 NiaPy 框架执行优化过程：先从特征选择算法、特征变换算法和分类器三组组件中选取最优组合，再优化所选组件的超参数；也支持组件选择与超参数优化合并为一步的原始方法。支持数值/类别特征与缺失值，新增回归任务支持（API 中回归器仍称 classifiers）。提供 CLI（optimize/infer 子命令）、GUI 与远程 API，可在多发行版通过包管理器安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段优化：组件选择与超参数调优分离（或合并为一步的原始方法）
- 支持数值/类别特征、缺失值填补、类别特征编码
- 提供 CLI（niaaml optimize / infer）与远程 API，流水线可导出为 .ppln 文件复用
- 支持回归任务，含 LinearRegression/Ridge 等回归组件

## 适用场景

- 不手写代码、在终端快速跑一次流水线优化与推理
- 为分类/回归任务自动选择特征选择、变换算法与模型组合
- 实现自定义分类器、适应度函数、编码器或填补器并接入优化流程

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L37: NiaAML is a framework for Automated Machine Learning based on nature-inspired algorithms for optimization. The fram
> L175: Load data and try to find the optimal pipeline for the given components. The example below uses the Particle Swarm

## 星数曲线

```mermaid
xychart-beta
    title "firefly-cpp/NiaAML 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `32956060df39` · [字段定义](../../DATASET.md)*
