# AmirhosseinHonardoust/Synthetic-Data-Artist

⭐ 21 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/AmirhosseinHonardoust/Synthetic-Data-Artist) · 个人维护

**生成并评估合成表格数据的 Python 研究项目（Copula vs VAE）**

读取真实表格 CSV，用 Gaussian Copula 与轻量 VAE 两种方法生成合成数据，并做多维评估：分布重叠（Jensen-Shannon）、相关性差异、类别相似度、边界违规、精确重复率与近邻距离隐私代理指标，可选 train-synthetic-test-real 的下游 ML 效用评估。输出合成 CSV、metrics.json、quality_summary.csv、可视化图与 HTML 报告。README 明确声明这是研究与作品集演示，不提供形式化差分隐私，不替代 SDV/CTGAN 等成熟库。通过 pip 可编辑安装与 CLI 运行，VAE 需另装 PyTorch extra。

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

- Gaussian Copula 与轻量 VAE 双生成方法对比
- 分布/相关/类别/边界/隐私代理多维评估指标
- 可选 train-on-synthetic, test-on-real 下游 ML 效用评估
- 输出 metrics.json、可视化图与 HTML 报告

## 适用场景

- 生成合成表格数据用于原型或演示而不暴露原始数据
- 对比统计方法与神经方法在合成数据质量上的差异
- 检查合成数据的分布保真度与隐私风险代理指标

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L6: A professional research-style Python project for generating and evaluating **synthetic tabular data**. The project c
> L37: - Generate synthetic rows using a Gaussian Copula method
> L38: - Generate synthetic rows using a lightweight VAE method

## 星数曲线

```mermaid
xychart-beta
    title "AmirhosseinHonardoust/Synthetic-Data-Artist 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e7f82a9b2e9d` · [字段定义](../../DATASET.md)*
