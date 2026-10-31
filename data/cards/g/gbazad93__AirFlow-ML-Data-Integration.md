# gbazad93/AirFlow-ML-Data-Integration

⭐ 15 · Python · MIT · 推送 2026-08-25 · [GitHub](https://github.com/gbazad93/AirFlow-ML-Data-Integration) · 个人维护

**Apache Airflow 天气数据每日 ETL 示例管线，产出供 ML 使用的数据**

演示如何用 Apache Airflow 编排每日 ETL 管线：从 OpenWeather 免费 API 获取天气数据，经清洗与校验后写入 PostgreSQL 数据库，可扩展用于下游机器学习训练或可视化。提供 docker compose 一键运行全栈，或按 Setup 文件夹的分步说明自行安装 Airflow、PostgreSQL 与 API key，通过 Airflow UI 触发 weather_data_pipeline。需注意 Airflow 在 Windows 上不完全支持，建议 Linux/WSL/Docker 环境。仓库本身不含模型训练代码，ML 为可扩展方向。

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

- Airflow 调度的每日天气数据获取-清洗-入库管线
- docker compose 一键运行 Airflow + PostgreSQL 全栈
- Setup 文件夹提供分步安装配置指南
- 模块化设计：DAG、数据库连接、数据处理分文件

## 适用场景

- 学习 Airflow DAG 编排与数据库连接配置
- 搭建可复现的天气数据 ETL 管线
- 为机器学习训练准备结构化数据集

## 场景标签

 · 领域:数据工程/ETL

## 证据(README 行号)

> L9: This project demonstrates how to use Apache Airflow for orchestrating a daily ETL pipeline that fetches weather data
> L35: This repository offers a sample Airflow project integrating a daily weather data fetch from OpenWeather’s free API 

## 星数曲线

```mermaid
xychart-beta
    title "gbazad93/AirFlow-ML-Data-Integration 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `002fc19a3268` · [字段定义](../../DATASET.md)*
