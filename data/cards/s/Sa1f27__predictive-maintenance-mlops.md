# Sa1f27/predictive-maintenance-mlops

⭐ 15 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/Sa1f27/predictive-maintenance-mlops) · 个人维护

**卡车故障预测的端到端 MLOps 流水线：预测、评分、部署、监控**

基于 SCANIA 卡车车队真实传感器数据构建的预测性维护系统：用生存分析模型（LightGBM 离散时间风险等 4 种模型）预测部件在未来 6-48 时间步内故障的概率，按 SCANIA 成本矩阵给出成本最优告警，并用共形预测输出 90% 覆盖的窗口集合与 TreeSHAP 解释。数据管道用 Polars 与 Pandera 校验、SHA-256 固定下载；MLflow 管理模型版本与晋级门，Dagster 编排并在漂移时触发重训；FastAPI 提供评分 API，配 Prometheus/Grafana 监控、数字孪生与维护 copilot。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 种生存模型按成本矩阵对比，含共形预测窗口集与 TreeSHAP 解释
- MLflow champion/challenger 晋级门 + PSI 漂移监控触发重训
- OPC UA/MQTT Sparkplug B 模拟车队经统一命名空间接入 FastAPI 平台
- 维护 copilot 基于平台工具回答且展示每次工具调用

## 适用场景

- 为车队传感器数据搭建故障预测与告警服务
- 搭建带漂移检测与自动重训的 ML 生命周期管理
- 按工业标准（OPC UA/AAS）接入实时评分平台
- 面向维护计划员生成车间维修计划与单卡决策解释

## 场景标签

`MLOps` `数据分析` `聊天机器人` · 领域:效率与自动化

## 证据(README 行号)

> L3: Predicting failures of an engine component across a fleet of SCANIA trucks: when it will fail, how sure the model
> L87: - **Survival, not plain classification.** Every model predicts the probability of failing within 6, 12, 24 and 48
> L96: - **MLflow registry with champion and challenger.** `predmaint train` compares all four models and registers the


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `47720537b67c` · [字段定义](../../DATASET.md)*
