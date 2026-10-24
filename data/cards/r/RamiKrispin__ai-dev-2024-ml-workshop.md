# RamiKrispin/ai-dev-2024-ml-workshop

⭐ 93 · HTML · 推送 2026-10-24 · [GitHub](https://github.com/RamiKrispin/ai-dev-2024-ml-workshop) · [官网](https://ramikrispin.github.io/ai-dev-2024-ml-workshop/) · 个人维护

**AI Dev 2024 会议工作坊材料：用开源工具部署与监控 ML 流水线**

面向 AI Dev 2024 会议参与者的工作坊教学材料：以加州 CISO 四个供电区的逐小时电力需求为案例，演示如何用 Python、Docker、GitHub Actions 搭建全自动数据刷新与预测流水线，每 24 小时生成未来 24 小时需求预测。使用 EIA API 拉取数据，MLflow 跟踪回测实验并按 MAPE 选模型（Darts 库的线性回归与 XGBoost），Quarto 生成监控仪表盘并部署到 GitHub Pages。内容基于作者在 LinkedIn Learning 的课程，采用 CC BY-NC-SA 许可。

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

- GitHub Actions + Docker 实现数据刷新与预测的全自动定时流水线
- MLflow 跟踪回测结果并按 MAPE 指标为每个序列选最优模型
- Quarto 静态仪表盘部署到 GitHub Pages 展示预测与元数据
- 元数据收集覆盖数据刷新日志、模型选择与预测刷新日志

## 适用场景

- 学习如何用开源工具部署端到端 ML 流水线
- 参考 GitHub Actions 定时任务加 Docker 的 CI/CD 模式
- 了解 MLflow 实验跟踪与模型回测选型的实践做法

## 场景标签

`教程课程` `MLOps` · 领域:学习与行业

## 证据(README 行号)

> L3: Materials for the **Deploy and Monitor ML Pipelines with Open Source and Free Applications** workshop at the AI_dev 
> L9: The workshop will focus on different deployment designs of machine learning pipelines using open-source applications
> L302: This tutorial is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

## 星数曲线

```mermaid
xychart-beta
    title "RamiKrispin/ai-dev-2024-ml-workshop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-24 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `07826c5dc88f` · [字段定义](../../DATASET.md)*
