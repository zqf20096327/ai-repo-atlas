# dida-do/eurocropsml

⭐ 33 · Python · MIT · 推送 2026-01-16 · [GitHub](https://github.com/dida-do/eurocropsml) · [官网](https://zenodo.org/doi/10.5281/zenodo.10629609) · 组织维护

**欧洲农作物少样本分类基准数据集（Sentinel-2 时序）**

面向少样本作物类型分类的预处理即用基准数据集：含 706,683 个 Sentinel-2 多类标注数据点、176 个类别，覆盖爱沙尼亚、拉脱维亚、葡萄牙三国 2021 年逐地块的中值像元时序（L1C 反射率）。区域间类别分布差异大，适合研究跨区域迁移与少样本学习方法。以 PyPI Python 包 eurocropsml 提供 CLI 下载，数据亦托管于 Zenodo；由慕尼黑工业大学遥感技术教席与 dida 在 PreTrainAppEO 项目中开发，附 Sci Data 论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 706,683 个标注数据点、176 个作物类别，覆盖三国
- 每数据点为 2021 年逐地块 Sentinel-2 L1C 年度时序
- 提供 eurocropsml-cli 命令行下载与配置管理
- 基于 EuroCrops 第 9 版开源遥感参考数据

## 适用场景

- 少样本/迁移学习作物分类方法的基准评测
- 跨区域农业地块分类研究（区域标签分布差异场景）
- 遥感时序机器学习模型的训练数据来源

## 场景标签

 · 领域:地球观测/农业遥感

## 证据(README 行号)

> L14: `EuroCropsML` is a pre-processed and ready-to-use machine learning dataset for crop type classification of agricult
> L87: The ready-to-use EuroCopsML dataset is developed for the purpose of improving and benchmarking few-shot crop type c

## 星数曲线

```mermaid
xychart-beta
    title "dida-do/eurocropsml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `26d0b6c823ed` · [字段定义](../../DATASET.md)*
