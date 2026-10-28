# aimclub/Fedot.Industrial

⭐ 88 · Python · BSD-3-Clause · 推送 2026-10-27 · [GitHub](https://github.com/aimclub/Fedot.Industrial) · [官网](https://github.com/aimclub/Fedot.Industrial/wiki) · 组织维护

**面向工业时间序列的 AutoML 框架：自动完成分类/回归/预测建模**

Fedot.Ind 是基于 FEDOT AutoML 框架构建的 Python 库，面向工业时间序列问题，提供分类、回归、预测与异常检测能力。高层 API FedotIndustrial 提供 fit/predict/get_metrics 接口，fit 阶段自动完成特征提取与流水线优化，输入支持 NumPy 数组与 Pandas DataFrame。开发环境要求 Python 3.10 或 3.11，暂不支持 3.12。README 附带 UCR 等 112 个数据集上的多算法基准结果与建筑能耗、PMSM 转子温度等真实案例 notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- fit/predict 接口自动完成特征提取与流水线构建调优
- 支持时间序列分类、回归、预测与异常检测
- 提供基准测试基础设施与核学习（Kernel Learning）文档
- 附建筑能耗预测等真实工业案例 notebook

## 适用场景

- 用少量代码对工业时间序列做分类或回归建模
- 自动搜索与调优时间序列预测流水线，替代手工建模
- 复现或对比 UCR 等时间序列基准上的算法表现

## 场景标签

 · 领域:工业/时间序列机器学习

## 证据(README 行号)

> L73: Fedot.Ind is a automated machine learning framework designed to solve industrial problems related
> L74: to time series forecasting, classification, and regression. It is based on
> L111: Fedot.Ind provides a high-level API that allows you to use its capabilities in a simple way.
> L112: The API can be used for classification, regression, and time series forecasting problems, as well as

## 星数曲线

```mermaid
xychart-beta
    title "aimclub/Fedot.Industrial 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 87 --> 89
    line [88, 88]
```

2026-10-18 88 → 2026-10-28 88（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0d3efda632b9` · [字段定义](../../DATASET.md)*
