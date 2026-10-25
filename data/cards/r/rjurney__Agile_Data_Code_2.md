# rjurney/Agile_Data_Code_2

⭐ 461 · Jupyter Notebook · MIT · 推送 2026-02-11 · [GitHub](https://github.com/rjurney/Agile_Data_Code_2) · [官网](http://bit.ly/agile_data_science) · 个人维护

**《Agile Data Science 2.0》书籍配套示例代码库**

O'Reilly 2017 年《Agile Data Science 2.0》一书的配套源代码仓库。以航班延误预测应用为主线，构建从历史数据训练分类器（Spark 批处理）、经 Kafka 队列由 Spark Streaming 实时预测、结果存入 MongoDB 并由 Web 前端展示的完整预测系统。README 说明书中原始代码已过时，应使用仓库内的 Jupyter Notebook 与 Docker Compose 运行，并声明代码仍在维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 航班延误预测的完整批处理+实时系统示例（Spark/Kafka/MongoDB）
- 以 Docker Compose 为唯一安装方式，附带 Jupyter Notebook
- 包含数据价值金字塔与前后端架构说明

## 适用场景

- 跟随书籍章节学习敏捷数据科学开发流程
- 参考 Spark Streaming + Kafka 实时预测系统架构
- 在本地 Docker 环境中复现书中的应用示例

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains the updated sourcec code for Agile Data Science 2.0, O'Reilly 2017. Now available at the O'
> L5: NOTE: THE BOOK'S CODE IS OLD, BUT THE CODE IS MAINTAINED. USE DOCKER COMPOSE AND THE NOTEBOOKS IM THIS REPOSITORY.
> L75: The back end architecture diagram shows how we train a classifier model using historical data (all flights from 201

## 星数曲线

```mermaid
xychart-beta
    title "rjurney/Agile_Data_Code_2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 460 --> 462
    line [461, 461]
```

2026-10-18 461 → 2026-10-25 461（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `f1f267199d88` · [字段定义](../../DATASET.md)*
