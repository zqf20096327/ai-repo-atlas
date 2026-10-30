# psweens/ml-forecast-lab

⭐ 16 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/psweens/ml-forecast-lab) · [官网](https://www.buymeacoffee.com/psweens) · 个人维护

**Home Assistant 多模型时序预测应用：训练、评测并发布校准预测**

面向 Home Assistant 高级用户的 HA 应用：接入任意 HA 传感器历史数据，对 32 种预测后端（LightGBM/CatBoost/LSTM/PatchTST/Chronos-Bolt/AutoARIMA 等）在相同交叉验证折上做 MAE/RMSE/MASE 复合排名（含 95% bootstrap CI），一键将胜出模型提升为生产模型，按计划重训练（默认 24h）并以伴随传感器形式将预测与 80% conformal 区间发布回 HA。定位 Pi 5（8GB RAM、无 GPU、ARM64）硬件区间，通过 HA 应用商店安装，首次构建在 Pi 5 上需 10-15 分钟。代码库稳定但公开用户群小，作者以业余时间维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 32 种模型后端在相同交叉验证折上复合排名并附 95% bootstrap CI
- 胜出模型按计划自动重训练并以伴随传感器发布预测
- 80% split conformal 校准预测区间（滚动残差缓冲）
- 支持 zero-shot 基础模型 Chronos-Bolt 与 Granite TTM（免训练预测）

## 适用场景

- 为家庭能耗等 HA 传感器生成带校准区间的预测
- 在我的数据上一次性对比多种时序模型再选定生产模型
- 在树莓派 5 上无 GPU 运行本地预测，无需云端与订阅

## 场景标签

 · 领域:物联网/家庭自动化时序预测

## 证据(README 行号)

> L7: Train, benchmark, and deploy time-series models for any HA sensor — with academic-standard evaluation built in.
> L19: A Home Assistant app for HA power users who want to forecast a sensor — not data scientists who want a fresh framew
> L45: ML Forecast Lab trains every enabled forecasting backend on your sensor's history, ranks them on identical cross-va

## 星数曲线

```mermaid
xychart-beta
    title "psweens/ml-forecast-lab 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `425ecadff8ce` · [字段定义](../../DATASET.md)*
