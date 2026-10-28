# mehmetkahya0/f1-race-prediction

⭐ 50 · Python · 推送 2026-02-01 · [GitHub](https://github.com/mehmetkahya0/f1-race-prediction) · 个人维护

**F1 车迷与数据爱好者的 2026 赛季比赛结果蒙特卡洛+ML 预测模拟器**

Python 编写的 F1 比赛模拟引擎，以真实 F1 数据（Fast-F1 API，占 50%）+ 机器学习集成（Random Forest/Gradient Boosting/MLP，占 25%）+ 蒙特卡洛模拟（占 25%）的混合方式预测排位赛与正赛结果。覆盖 2026 新规（350kW MGU-K、主动空气动力学）、11 车队 22 车手 24 站赛历，含轮胎退化物理、进站策略优化、天气与事故系统，并生成多种可视化图表。通过 git clone 源码运行 python main.py，声明预测仅供娱乐与教育用途，非投注工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 真实数据+ML+蒙特卡洛的三方混合预测（50/25/25）
- 含轮胎退化物理与动态规划进站窗口优化
- Random Forest/Gradient Boosting/MLP 加权集成与置信度评分
- 覆盖 2026 新规与 24 站赛历，附 2025 赛季预测对实绩记录

## 适用场景

- 模拟 2026 赛季各站排位赛与正赛结果
- 分析不同天气与轮胎策略下的比赛走向
- 查看车队/车手表现的对比可视化图表

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L10: **A sophisticated Formula 1 race simulation engine combining real telemetry data with Monte Carlo probabilistic mod
> L28: - **Triple Hybrid Prediction**: Real F1 data (50%) + ML Models (25%) + Monte Carlo simulation (25%)

## 星数曲线

```mermaid
xychart-beta
    title "mehmetkahya0/f1-race-prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-28 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bb6e966ef5d0` · [字段定义](../../DATASET.md)*
