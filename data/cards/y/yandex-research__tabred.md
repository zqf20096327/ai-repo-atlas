# yandex-research/tabred

⭐ 97 · Python · Apache-2.0 · 推送 2026-07-30 · [GitHub](https://github.com/yandex-research/tabred) · [官网](https://arxiv.org/abs/2406.19380v4) · 组织维护

**八个工业级表格数据基准数据集，供评估表格深度学习方法**

ICLR 2025 论文配套的表格机器学习基准集合：收录八个来自竞赛与行业场景的数据集，覆盖分类与回归任务，强调时间分布偏移、特征工程产出的丰富特征集等更贴近实际应用的条件。提供 uvx tabred 命令行下载器获取预处理数据（npy 特征矩阵 + info.json 元数据），包含默认/随机/滑动窗口三种切分供切分策略研究；仓库另含论文复现代码与数据集重建脚本（当前重建脚本暂未整理完毕，作者标注数日内发布）。面向表格深度学习方向的研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 八个工业级表格数据集，含分类与回归任务
- 默认/随机/滑动窗口三种数据切分支持切分策略研究
- uvx tabred CLI 下载预处理数据，可按数据集选择下载
- 仓库含论文复现代码与可复现的预处理管线

## 适用场景

- 在含时间分布偏移的数据上评估表格深度学习方法
- 研究不同数据切分策略对基准结论的影响
- 复现 TabReD 论文实验结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: TabReD is a collection of eight industry-grade tabular datasets designed to evaluate machine learning methods under 
> L39: |Dataset|Features|Task|Instances Used|Instances Available|Source|

## 星数曲线

```mermaid
xychart-beta
    title "yandex-research/tabred 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-25 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `21edf23d91d4` · [字段定义](../../DATASET.md)*
