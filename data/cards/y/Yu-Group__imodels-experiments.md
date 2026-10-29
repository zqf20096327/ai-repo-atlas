# Yu-Group/imodels-experiments

⭐ 18 · Jupyter Notebook · 推送 2026-05-22 · [GitHub](https://github.com/Yu-Group/imodels-experiments) · [官网](https://csinva.io/imodels/) · 组织维护

**imodels 可解释规则模型的实验复现与基准脚本集**

配套 imodels 包的实验代码库：提供复现 FIGS、Hierarchical Shrinkage、G-FIGS、MDI+ 四种可解释树/规则模型方法的脚本。基准流程为：编写 sklearn 兼容模型、通过 config 选择数据集与模型、运行拟合脚本（支持 SLURM 集群并行）、聚合结果并绘图。数据集自动下载，测试用 pytest 运行。主要面向希望复现论文实验或对新监督模型做基准比较的研究者。仅覆盖监督学习任务，无监督学习需自行改代码。

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

- 复现 FIGS / Hierarchical Shrinkage / G-FIGS / MDI+ 四种方法
- 按 config 组织数据集与模型选择，数据集自动下载
- 支持 SLURM 集群并行提交拟合任务
- 聚合脚本将跨数据集结果合并为 combined.pkl 供绘图

## 适用场景

- 复现 FIGS 等可解释模型的论文实验
- 对新的 sklearn 兼容模型做多数据集基准比较
- 在集群上并行跑多种子拟合实验并汇总结果

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L2: 	Scripts for easily comparing different aspects of the imodels package. Contains code to reproduce FIGS + Hierarchic
> L6: Follow these steps to benchmark a new (supervised) model.

## 星数曲线

```mermaid
xychart-beta
    title "Yu-Group/imodels-experiments 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `0ff5fe4d4ac9` · [字段定义](../../DATASET.md)*
