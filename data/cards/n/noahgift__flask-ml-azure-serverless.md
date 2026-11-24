# noahgift/flask-ml-azure-serverless

⭐ 123 · Python · 推送 2026-11-23 · [GitHub](https://github.com/noahgift/flask-ml-azure-serverless) · [官网](https://www.coursera.org/learn/machine-learning-with-databricks-and-mlflow?utm_source=github&utm_medium=repo_website&utm_campaign=funnel_2026q4&utm_content=flask-ml-azure-serverless) · 个人维护

**在 Azure App Services 上部署 Flask 机器学习应用的教程项目**

一个演示型代码仓库，包含基于 sklearn 的 Flask 预测应用及其部署流程：本地可通过 Python 虚拟环境、make install 和 app.py 运行，并通过 make_prediction.sh 调用预测接口；云端按步骤在 Azure Cloud Shell 中使用 az webapp up 部署，再通过 Azure DevOps Pipelines 配置 GitHub 集成的持续交付与 lint 步骤。附带作者的云计算图书与 MLOps 课程链接，主题标签显示其源自 Udacity/Northwestern 课程教学场景。要求 Python 3.8，更新版本存在兼容问题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Flask + sklearn 预测接口，本地运行并可用 make_prediction.sh 验证
- az webapp up 一键部署到 Azure App Services
- Azure DevOps Pipelines 持续交付配置，含 lint 门禁步骤
- 提供 Dockerfile/Makefile 容器构建路径

## 适用场景

- 学习如何把 Flask 机器学习应用部署到 Azure App Services
- 搭建一条从 GitHub 到 Azure 的持续交付流水线
- 作为课程练习的起点工程进行改造

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L2: Deploy Flask Machine Learning Application on Azure App Services
> L11: ## To run it locally follow these steps (on Python 3.8, there are issues on later version of Python)
> L116: **Learn MLOps end to end:** Machine Learning with Databricks and MLflow (Coursera) · MLOps specialization, Duke (C


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `d48638ec7a9e` · [字段定义](../../DATASET.md)*
