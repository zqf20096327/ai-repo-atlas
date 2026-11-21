# rishv1912/Customer-Churn-MLOps

⭐ 10 · Jupyter Notebook · 推送 2026-07-24 · [GitHub](https://github.com/rishv1912/Customer-Churn-MLOps) · 个人维护

**电信客户流失预测的端到端 ML 工程与 MLOps 项目**

面向电信行业的客户流失预测机器学习项目：基于客户历史记录与服务数据（通话时长、套餐、客服呼叫次数等特征）预测客户留存或流失。技术栈覆盖 Streamlit 前端单条预测、FastAPI 批量预测接口、PostgreSQL 数据存储、Airflow 流水线编排、MLflow 指标追踪（F1/Precision/Recall）、GitHub Actions CI/CD、Docker 镜像与 AWS（ECR/S3/EC2）部署。README 的数据集章节与目录部分存在未填写内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 决策树分类模型预测电信客户流失
- Airflow 编排训练、重训与批量预测流水线
- MLflow 追踪 F1-score/Precision/Recall 指标
- GitHub Actions + Docker + AWS EC2/ECR/S3 部署链路

## 适用场景

- 学习端到端 MLOps 工程的完整流程
- 搭建电信客户流失预测模型
- 参考 CI/CD 与云端部署的 ML 项目实践

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L2: This Project is for detecting Customer Churn using their past records and service provided.
> L24: |**Orchestration**|Apache Airflow|Orchestrates training, retraining, and batch prediction pipelines.|
> L26: |**CI/CD**|GitHub Actions|Automates CI/CD pipelines, including Docker build and deployment.|

## 星数曲线

```mermaid
xychart-beta
    title "rishv1912/Customer-Churn-MLOps 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-11-21"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-19 10 → 2026-11-21 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `a0006dcd2181` · [字段定义](../../DATASET.md)*
