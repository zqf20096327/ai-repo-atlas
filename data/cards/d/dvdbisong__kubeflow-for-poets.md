# dvdbisong/kubeflow-for-poets

⭐ 14 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/dvdbisong/kubeflow-for-poets) · 个人维护

**教程配套仓库：用 Docker/Kubernetes/Kubeflow 部署 ML 流水线**

《Kubeflow for Poets》教程系列的配套源码仓库，教程讲解以容器、Kubernetes 和 Kubeflow Pipelines 将机器学习流水线上线生产的完整流程，2026 年 10 月更新以适配 KFP SDK v2 与 Google Cloud。仓库含 Docker/Kubernetes 入门示例与一个端到端流水线：加载加密货币价格 CSV、按日期切分、时序交叉验证调优神经网络回归器并训练，输出 RMSE/MAE。支持本地运行器逐组件虚拟环境执行，也可编译 YAML 提交到 Kubeflow 或 Google Agent Platform Pipelines。需 Python 3.12+。

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

- KFP SDK v2 的四步端到端流水线（加载/变换/调优/训练）
- 本地 runner 为每个步骤提供独立虚拟环境
- 同一 YAML 可运行于 Kubeflow Pipelines 与 Google Agent Platform Pipelines
- 内置 971 种加密货币 2013-2018 年日线数据（498,380 行），可经 data_url 参数替换

## 适用场景

- 跟随教程学习容器化 ML 流水线的部署流程
- 参考 KFP SDK v2 端到端流水线的写法与本地运行方式
- 用自己的价格数据替换数据集复现流水线

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: Source code for **Kubeflow for Poets**, a guide to putting machine learning pipelines into production with container
> L17: 7. Kubeflow Pipelines
> L32: `kubeflow-pipelines/crypto_pipeline.py` defines four steps with the KFP SDK v2:

## 星数曲线

```mermaid
xychart-beta
    title "dvdbisong/kubeflow-for-poets 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c9fb7a9f7b51` · [字段定义](../../DATASET.md)*
