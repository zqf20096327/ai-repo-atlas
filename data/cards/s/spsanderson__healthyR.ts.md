# spsanderson/healthyR.ts

⭐ 20 · R · NOASSERTION · 推送 2026-01-27 · [GitHub](https://github.com/spsanderson/healthyR.ts) · [官网](https://www.spsanderson.com/healthyR.ts/) · 个人维护

**面向医院管理/临床数据的时间序列分析与预测 R 包**

healthyR.ts 是 healthyR 的时间序列配套 R 包，基于 tidymodels 生态，面向医院管理与临床指标（住院时长、再入院率、住院量、床位占用等）的时间序列分析。提供 15 个自动化建模工作流函数（ARIMA、Prophet、XGBoost、神经网络自回归、ETS、SVM 等），单个函数完成 recipe、模型设定、拟合、调参与校准；另含可视化套件（日历热图等）、合成数据生成、统计检验与基于特征的时间序列聚类。通过 CRAN 或 GitHub 安装，自标生命周期为 experimental。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 15 个 ts_auto_* 自动化建模工作流（ARIMA/Prophet/XGBoost/NNETAR/ETS/SVM 等）
- 90+ 函数，覆盖数据生成、可视化、聚类、统计检验与 recipe 步骤
- 基于 tidymodels 生态的单函数端到端建模管道
- CRAN 稳定版与 GitHub 开发版两种安装途径

## 适用场景

- 预测医院日/周住院量与床位占用以做资源规划
- 分析并预测平均住院时长与再入院率趋势
- 对临床时间序列做季节模式识别与事件前后分析

## 场景标签

 · 领域:医疗健康数据分析/时间序列

## 证据(README 行号)

> L15: `healthyR.ts` is a comprehensive R package designed specifically for
> L40: ✅ **Forecasting** - 15 automated model workflows (ARIMA, Prophet,

## 星数曲线

```mermaid
xychart-beta
    title "spsanderson/healthyR.ts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d2033d5dfccc` · [字段定义](../../DATASET.md)*
