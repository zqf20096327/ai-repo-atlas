# vcerqueira/experiments-sizematters

⭐ 41 · R · 推送 2025-12-31 · [GitHub](https://github.com/vcerqueira/experiments-sizematters) · 个人维护

**复现论文实验：ML 与统计方法的时间序列预测对比**

V. Cerqueira 等人 2022 年发表于 Journal of Intelligent Information Systems 的论文《A case study comparing machine learning with statistical methods for time series forecasting: size matters》的实验代码仓库。以 R 语言编写，按顺序运行三个源文件（1-tsdl-build-db.r 构建数据、2-main.r 主实验、3-result-analysis.r 结果分析）即可复现实验，对比机器学习与统计方法在不同样本规模下的时间序列预测表现。默认为在线分析，运行耗时较长。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 复现已发表论文实验的 R 源码
- 三个脚本按序运行：建库、主实验、结果分析
- 使用 TSDL 时间序列数据构建实验库

## 适用场景

- 复现论文中 ML 与统计方法的预测对比实验
- 在不同样本规模上验证预测方法的表现
- 作为时间序列预测方法比较研究的参考实现

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains the code to reproduce the experiments reported in the paper:
> L5: `Cerqueira, V., Torgo, L., & Soares, C. (2022). A case study comparing machine learning with statistical methods for

## 星数曲线

```mermaid
xychart-beta
    title "vcerqueira/experiments-sizematters 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `adf4c48c02fc` · [字段定义](../../DATASET.md)*
