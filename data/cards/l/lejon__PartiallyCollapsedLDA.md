# lejon/PartiallyCollapsedLDA

⭐ 28 · Java · 推送 2026-06-30 · [GitHub](https://github.com/lejon/PartiallyCollapsedLDA) · 组织维护

**面向科研的主题模型（LDA）并行采样器 Java 工具包**

多个快速并行化 LDA 采样器的 Java 实现，包括 Partially Collapsed LDA、Light LDA、Polya-Urn LDA、稀疏精确采样器（Spalias）与 HDP 采样器。功能含锚词先验、采样中断续采、停用词与文本清洗、TF-IDF 词频阈值、LDAVis 统计导出、随机种子固定与 thinning。通过 Maven 构建，以 jar 与配置文件方式命令行运行；README 声明其为科研原型，代码中存在注释掉的代码与未清理内容，基础采样器已经过科学评测。随附论文（JCGS 2017、TPAMI 2017）与 Zenodo DOI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多种并行采样器：PC-LDA、Light LDA、Polya-Urn、Spalias、HDP
- 锚词先验与采样中断后续采
- 停用词、文本清洗、TF-IDF 词频阈值过滤
- 统计可导出至 LDAVis，支持随机种子与 thinning

## 适用场景

- 科研人员对文本语料做主题模型推断
- 复现论文中的稀疏部分坍缩 MCMC 与 Polya-Urn 采样方法
- 需要可中断续采的大规模 LDA 训练

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: * Several implemented samplers including a very fast approximate Polya Urn sampler, an exact sparse sampler (Spalia
> L22: Repo for our Partially Collapsed Parallel LDA implementations described in the articles:

## 星数曲线

```mermaid
xychart-beta
    title "lejon/PartiallyCollapsedLDA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `481d62c1a267` · [字段定义](../../DATASET.md)*
