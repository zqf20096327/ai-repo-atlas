# deburky/credit-risk-modeling-on-aws

⭐ 18 · Python · MIT · 推送 2026-01-26 · [GitHub](https://github.com/deburky/credit-risk-modeling-on-aws) · 个人维护

**AWS 信用风险建模代码示例集：训练/部署/推理流水线**

配套《Credit Risk Modeling on AWS》书籍项目的代码示例库，作者 Denis Burakov。包含四个完整实现：基于 SageMaker+Kinesis+Lambda+DynamoDB 的实时评分、EventBridge 触发 SageMaker Pipelines 的 CatBoost 批量评分与额度管理、AWS 上的 MLflow 跟踪服务器部署、SageMaker 端点 A/B 测试 Lambda。均通过 LocalStack + Docker 在本地运行，需 AWS 凭证使用 SageMaker local mode，各模块用 Makefile 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时/批量/MLflow/A-B 测试四套完整流水线示例
- LocalStack + Docker 本地模拟 AWS 服务
- CatBoost + SHAP 建模与额度决策业务逻辑
- Makefile 驱动各工作流运行

## 适用场景

- 学习在 AWS 上构建信用评分训练与部署流水线
- 本地用 LocalStack 复现 SageMaker ML 工作流
- 参考 MLflow 在 AWS 上的跟踪服务器部署方式

## 场景标签

`教程课程` `MLOps` · 领域:学习与行业

## 证据(README 行号)

> L5: This repository contains code examples and implementations from the **Credit Risk Modeling on AWS** book project.
> L11: This project demonstrates several credit risk modeling use cases using AWS services, including model training, depl

## 星数曲线

```mermaid
xychart-beta
    title "deburky/credit-risk-modeling-on-aws 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `80a0c96fbf5d` · [字段定义](../../DATASET.md)*
