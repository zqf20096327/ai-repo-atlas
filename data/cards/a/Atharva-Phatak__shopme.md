# Atharva-Phatak/shopme

⭐ 20 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/Atharva-Phatak/shopme) · 个人维护

**面向开发者的 H&M 时尚商品端到端推荐系统模板**

为 H&M 商品构建的端到端图像推荐系统，可用作 MLOps 项目模板：用 BeautifulSoup 抓取商品元数据并用 Airflow 编排，存储于 S3；以 SimCLR 自监督方法训练 Resnet18 与 Efficient-Net B3 生成图像嵌入，用 Dagster 编排训练并以 MLflow 记录实验；后端用 BentoML 打包为 API 并容器化，前端为 Streamlit 应用，部署到 Google Cloud Run。提供两个已发布到 Docker Hub 的服务镜像。README 以教程式说明为主，未给出完整一键安装流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SimCLR 自监督训练 Resnet18 / Efficient-Net B3 生成图像嵌入
- Airflow 数据采集 + Dagster 训练编排 + MLflow 实验跟踪的 MLOps 流水线
- BentoML 打包后端 API，附 SwaggerUI
- Resnet18 与 Efficient-Net B3 两个服务镜像发布于 Docker Hub

## 适用场景

- 参考完整 MLOps 流水线搭建自己的端到端 ML 项目
- 学习从数据采集、训练到部署的 ML 系统构建流程
- 运行图像相似度时尚商品推荐演示

## 场景标签

`推荐系统` `MLOps` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L6: **In this project we will be building an end to end fashion recommender system for H&M products.**
> L46: The overall goal is to build an image based recommender system. There are multitude ways to do it, but I
> L51: SIMCLR was used to train two models: Resnet18 and Efficient-net B3.

## 星数曲线

```mermaid
xychart-beta
    title "Atharva-Phatak/shopme 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fe0da1a755bb` · [字段定义](../../DATASET.md)*
