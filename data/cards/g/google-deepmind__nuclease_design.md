# google-deepmind/nuclease_design

⭐ 86 · Jupyter Notebook · Apache-2.0 · 推送 2026-04-13 · [GitHub](https://github.com/google-deepmind/nuclease_design) · 组织维护

**核酸酶定向进化论文的配套数据集与分析代码库**

DeepMind 论文 Engineering highly active and diverse nuclease enzymes 的配套仓库：提供 55,760 个 NucB 变体的酶活性估计数据集（landscape.csv）、4 轮实验的多分类催化活性标签、NGS 原始计数数据及各序列设计方法的子库映射；附带 Colab notebook 用于复现论文图表、分析文库命中率与多样性、交互查看用于序列设计的 CNN 模型。数据存放在 Google Cloud Storage 桶中，notebook 会直接从 GitHub 安装本包，本地运行测试需 Python >= 3.10 并以 pip install -e . 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 55,760 个 NucB 变体的酶活性估计数据集（landscape.csv）
- Colab notebook 复现论文全部图表并可分析 CNN 序列设计模型
- GCS 桶提供 NGS 原始计数、富集因子、文库设计映射等多类数据
- 含 VAE 拟合所用的多序列比对数据

## 适用场景

- 基于公开酶活性数据训练新的机器学习模型
- 复现论文中的分析与图表
- 参考其流程构建自己的基因型-表型数据集

## 场景标签

`科研工具` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: This repository accompanies the paper: Engineering highly active and diverse nuclease enzymes by combining machine l
> L6: You can use our dataset of estimated enzyme activity for 55,760 NucB variants to develop new machine learning models

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/nuclease_design 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 85 --> 87
    line [86, 86]
```

2026-10-18 86 → 2026-10-30 86（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `494b5d2afb82` · [字段定义](../../DATASET.md)*
