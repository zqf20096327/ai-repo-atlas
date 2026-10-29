# TheAndreyZakharov/Frappe-HR-Forge

⭐ 19 · Python · Apache-2.0 · 推送 2026-06-28 · [GitHub](https://github.com/TheAndreyZakharov/Frappe-HR-Forge) · 个人维护 · 中文 README

**面向 ERPNext/Frappe HRMS 的本地 HR 模块开发基础（含 ML 脚手架）**

为扩展 ERPNext 与 Frappe HRMS 提供本地开发基座：Docker 化门户、自定义 Frappe 应用 compass_hr_ai、HR 专用 DocTypes（职业履历、技能、职业预测、团队计划等）、角色权限、演示种子数据，以及 Python 3.11 ML 环境与 ETL 管线脚手架（Rostrud/Zenodo、hh.ru、Stepik 缓存采集与 parquet 输出）。AI/ML 推荐、规划功能（嵌入、Qdrant、职业轨迹模型、薪资模型、FastAPI 服务）处于规划或脚手架阶段，尚未实现，作者自述非完成产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Docker 化 ERPNext/Frappe HRMS 本地门户与自定义应用 compass_hr_ai
- 自定义 HR DocTypes、角色、权限与工作区配置
- Python 3.11 ML 环境与可复现 ETL 管线（hh.ru/Stepik/Rostrud 缓存采集）
- 规划中的 NLP/职业轨迹/薪资模型与 FastAPI ML 服务（未实现）

## 适用场景

- 在 ERPNext/Frappe HRMS 上构建自定义 HR 功能的本地开发起点
- 准备 HR 数据 ETL 与 ML 实验环境（含本地数据分层与缓存）
- 按路线图逐步实现技能抽取、职业推荐与团队规划功能

## 场景标签

 · 领域:人力资源/ERP 定制开发

## 证据(README 行号)

> L3: Frappe HR Forge is a local ERPNext/Frappe HRMS development project prepared for building custom HR modules.
> L5: The repository contains a working local portal foundation, a custom Frappe application, HR-focused DocTypes, workspa
> L26: The repository is intentionally structured as a development foundation. The AI/ML recommendation features are plann
> L391: It currently provides the portal foundation, custom app structure, DocTypes, roles, permissions, demo data, ML env

## 星数曲线

```mermaid
xychart-beta
    title "TheAndreyZakharov/Frappe-HR-Forge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7c6d3392474e` · [字段定义](../../DATASET.md)*
