# hoangsonww/YouTube-Success-Prediction-ML

⭐ 20 · TypeScript · MIT · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/YouTube-Success-Prediction-ML) · [官网](https://hoangsonww.github.io/YouTube-Success-Prediction-ML/) · 个人维护

**面向开发者的 YouTube 频道表现预测与 MLOps 部署平台**

基于 Kaggle Global YouTube Statistics 2023 数据集（995 行）的机器学习平台：以 uploads/category/country/age 为输入，预测订阅数、年收益与 30 天增长；用 KMeans/DBSCAN 聚类频道原型，生成国家级可视化数据。提供 FastAPI/Flask API 与 Next.js 前端，附带 Docker、Kubernetes、Argo CD、Terraform 多云与 Jenkins/GitHub Actions 的 CI/CD 工作流。主要受众为 ML/后端/前端与 DevOps 工程师，自我定位为作品集级（portfolio-grade）项目。

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

- 三个目标的监督预测（订阅数/年收益/增长），支持批量预测与 what-if 模拟
- KMeans/DBSCAN 聚类并赋予可读的频道原型标签
- FastAPI 与 Flask 双 API 服务及 Next.js 可视化仪表盘
- Kubernetes/Argo CD/Terraform 多云部署与 GitOps 发布策略

## 适用场景

- 输入频道基本数据预测订阅、收益与短期增长
- 把频道聚类为战略原型并查看国家级行情
- 作为 ML 训练、测试、镜像构建与多云部署的工程参考实现

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: This repository contains a production-oriented machine learning platform for YouTube channel success prediction and 
> L113: - predicted subscribers
> L173: - Models trained for three targets:

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/YouTube-Success-Prediction-ML 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f7f77c299e42` · [字段定义](../../DATASET.md)*
