# noahgift/Python-MLOps-Cookbook

⭐ 439 · Jupyter Notebook · CC0-1.0 · 推送 2026-11-23 · [GitHub](https://github.com/noahgift/Python-MLOps-Cookbook) · [官网](https://www.coursera.org/learn/machine-learning-with-databricks-and-mlflow?utm_source=github&utm_medium=repo_website&utm_campaign=funnel_2026q4&utm_content=Python-MLOps-Cookbook) · 个人维护

**面向 MLOps 学习者的容器化 Flask 机器学习服务示例库**

配套 Practical MLOps 书籍与 Duke/Coursera 课程的教学示例仓库：包含一个基于 MLB 球员身高预测模型的容器化 Flask 微服务，提供预测 CLI（cli.py）与模型重训练 CLI（utilscli.py），模型以 joblib 存储。演示容器构建、GitHub Actions 自动化、以及部署到 AWS（Lambda/SAM、App Runner、Elastic Beanstalk、Copilot）、GCP（Cloud Run、App Engine、GKE）与 Azure 的多种方式。仓库部分章节标注 In progress。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个 CLI 工具：身高预测与模型重训练
- Flask 微服务支持本地运行与 Docker 容器化
- GitHub Actions 自动构建并推送镜像到 GHCR 与 Docker Hub
- 覆盖 AWS/GCP/Azure 多种部署目标清单

## 适用场景

- 学习如何将机器学习模型打包成 Flask 微服务
- 照着示例练习把容器部署到 AWS Lambda 或 Cloud Run
- 以该仓库为模板搭建自己的 MLOps 工程脚手架

## 场景标签

`教程课程` `MLOps` · 领域:学习与行业

## 证据(README 行号)

> L4: # Python MLOps Cookbook
> L202: **Learn MLOps end to end:** Machine Learning with Databricks and MLflow (Coursera) · MLOps specialization, Duke (C


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `bd8b090162ae` · [字段定义](../../DATASET.md)*
