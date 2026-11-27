# anandapurva55/nyc-taxi-forecasting

⭐ 35 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/anandapurva55/nyc-taxi-forecasting) · [官网](https://anandapurva55.github.io/nyc-taxi-forecasting/) · 个人维护

**MLOps 工程示范：AWS 上预测纽约出租车需求与车费**

基于 300 万条 NYC TLC 出行记录构建的端到端系统：XGBoost/LightGBM 按 254 个区域预测逐小时叫车需求并估算车费（含出发前报价模型），Optuna 调参，MLflow 注册模型，FastAPI 服务部署在 ECS Fargate，经 CloudFront 提供 HTTPS 访问；预测数据经 Firehose 写入 S3，由 SageMaker Processing 定期检查漂移与线上准确率并触发告警；Streamlit/Plotly 应用展示预测、车费与 SHAP 解释；68 项 AWS 资源由 Terraform 定义，CI 由 GitHub Actions 与 CodeBuild 完成。适合作为云端 ML 工程流程的参考实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个模型（需求、车费、预订时报价）均对照朴素基线给出 bootstrap 置信区间
- 按回测结果仅在模型占优的前 2 小时使用模型，其后切换上周同期规则
- SageMaker Processing 定时漂移检测与线上准确率评分，SNS 告警
- Terraform 定义全部 68 项 AWS 资源，Docker 镜像烘焙模型并按 commit 打标签

## 适用场景

- 学习在 AWS 上搭建从训练到服务到监控的完整 ML 流水线
- 参考时序切分、基线对照与模型门禁重训练的工程做法
- 搭建带漂移检测与告警的预测服务
- 通过浏览器内 stlite 演示试用预测与 SHAP 解释

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L19: An end-to-end **MLOps** system on AWS, written in **Python**, that forecasts hourly taxi pickups across 254 New Yor
> L21: **XGBoost** and **LightGBM** regressors, built on **scikit-learn** and tuned with **Optuna**, forecast pickups per 

## 星数曲线

```mermaid
xychart-beta
    title "anandapurva55/nyc-taxi-forecasting 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-11-26 35 → 2026-11-27 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `d9906deb8428` · [字段定义](../../DATASET.md)*
