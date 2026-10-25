# RamiKrispin/useR2024-pipeline-workshop

⭐ 57 · HTML · 推送 2026-10-25 · [GitHub](https://github.com/RamiKrispin/useR2024-pipeline-workshop) · [官网](https://ramikrispin.github.io/useR2024-pipeline-workshop/) · 个人维护

**useR!2024 工作坊材料：用 R 与免费工具部署监控 ML 流水线**

面向 R 用户的 MLOps 工作坊教学材料：以预测加州 CISO 四个供电区 24 小时电力需求为案例，演示用 Docker 与 Dev Containers 搭建开发环境、从 EIA API 拉取数据、以 Modeltime（线性回归/GLMNET/Prophet）做回测选模、用 MLflow 记录实验、point-blank 监控数据与模型健康，并以 GitHub Actions 定时刷新、Quarto 仪表板发布到 GitHub Pages。提供 Dockerfile、devcontainer 配置与工作流 YAML，采用 CC BY-NC-SA 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Docker 两层镜像（base-R + 项目镜像）与 Dev Containers 开发环境
- GitHub Actions 定时数据刷新与预测更新工作流
- Modeltime 多模型回测竞速并用 MLflow 记录实验
- point-blank 数据/模型监控 + Quarto 仪表板发布到 GitHub Pages

## 适用场景

- 学习用 R 和免费开源工具搭建端到端 ML 流水线
- 参考定时数据刷新与预测部署的 GitHub Actions 工作流
- 了解 MLflow 实验记录与 point-blank 监控的实践用法

## 场景标签

`MLOps` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: Materials for the **Deploy and Monitor ML Pipelines with Open Source and Free Applications** workshop at the useR!20
> L11: The workshop will focus on different deployment designs of machine learning pipelines using R, open-source applicat

## 星数曲线

```mermaid
xychart-beta
    title "RamiKrispin/useR2024-pipeline-workshop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-25 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `224b274ae444` · [字段定义](../../DATASET.md)*
