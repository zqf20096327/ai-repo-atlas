# rvandewater/YAIB

⭐ 110 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/rvandewater/YAIB) · [官网](https://github.com/rvandewater/YAIB/wiki) · 组织维护

**ICU 临床预测模型的标准化实验基准框架**

面向 ICU 与 EHR 数据的临床机器学习实验框架：支持 MIMIC-III/IV、eICU-CRD、HiRID、AUMCdb 四类数据集，预置 ICU 死亡率、AKI、败血症、肾功能、住院时长五个预测任务，可自定义数据集、队列、任务与模型。内置 Logistic 回归、LightGBM、LSTM、GRU、TCN、Transformer 等模型，通过 ricu 做队列预处理统一数据接口，支持评估与微调、WandB 超参扫描，从源码用 uv 安装并提供 MIMIC/eICU demo 数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预置 5 个临床预测任务（分类与回归）
- 开箱支持 4 个 ICU/EHR 数据集并允许新增
- 内置 LightGBM、LSTM、GRU、TCN、Transformer 等模型
- 支持跨数据集评估与微调、WandB 超参扫描

## 适用场景

- 在 ICU 数据上训练和对比临床预测模型
- 复现论文中的多中心基准实验
- 无数据权限时用 demo 数据快速上手

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L14: Yet another ICU benchmark (YAIB) provides a framework for doing clinical machine learning experiments on Intensive 
> L30: We provide five common tasks for clinical prediction by default:
> L251: We provide several existing machine learning models that are commonly used for multivariate time-series data.

## 星数曲线

```mermaid
xychart-beta
    title "rvandewater/YAIB 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 109 --> 111
    line [110, 110]
```

2026-10-18 110 → 2026-10-26 110（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `f283e029d3c5` · [字段定义](../../DATASET.md)*
