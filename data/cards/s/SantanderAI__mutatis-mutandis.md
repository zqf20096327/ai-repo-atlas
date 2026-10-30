# SantanderAI/mutatis-mutandis

⭐ 26 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/SantanderAI/mutatis-mutandis) · [官网](https://github.com/SantanderAI) · 组织维护

**反事实情景测试的歧视审计研究代码（论文配套）**

Santander AI Lab 与比萨大学论文《Mutatis Mutandis: Revisiting the Comparator in Discrimination Testing》的配套研究代码，提供可配置的 situation_testing Python 包：含混合属性距离函数（kdd2011）、Wald 置信区间、逐个体歧视报告、反事实情景测试（cfST）。区分 Ceteris Paribus 与 Mutatis Mutandis 两类比较器。附 Law School 数据集复现流水线（Python+R，数据需自行获取，不随库分发），需 Python>=3.10，可选 R>=4.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可配置 SituationTesting 估计器与 Python API
- Wald 置信区间与逐个体歧视报告
- 反事实情景测试（cfST）与反事实不公平性编码
- Law School 数据集可复现实验流水线（Python + R）

## 适用场景

- 审计决策规则对受保护群体的歧视性
- 在公平性分析中比较事实性与反事实性比较器
- 复现论文第 4 节实验

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: > Repository for *Mutatis Mutandis: Revisiting the Comparator in Discrimination Testing*, forthcoming in *Computatio
> L55: - `situation_testing` Python package with a configurable `SituationTesting` estimator.
> L63: - Auditing a decision rule for discrimination against a protected group.

## 星数曲线

```mermaid
xychart-beta
    title "SantanderAI/mutatis-mutandis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4461521b1423` · [字段定义](../../DATASET.md)*
