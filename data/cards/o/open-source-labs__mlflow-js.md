# open-source-labs/mlflow-js

⭐ 40 · TypeScript · MIT · 推送 2026-01-01 · [GitHub](https://github.com/open-source-labs/mlflow-js) · [官网](https://mlflow-js.org/) · 组织维护

**面向 JS/TS 开发者的 MLflow 客户端库**

开源 JavaScript/TypeScript 库，以 TypeScript 封装 MLflow Tracking Server 与 Model Registry 的全部 REST API 端点，让开发者在 JavaScript 代码库中追踪机器学习实验、记录指标/参数/模型并管理模型注册表。提供 Experiment Manager、Run Manager、Model Manager 等高层工作流抽象（如 runNewExperiment、copyRun、createModelFromRunWithBestMetric）。使用前需本机安装 MLflow（pip）或以 Docker 启动 Tracking Server，再 npm install mlflow-js 引入。定位为配合 TensorFlow.js 等库做客户端/浏览器侧 ML 生命周期管理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 MLflow Tracking Server 与 Model Registry 的全部 REST API 端点
- TypeScript 实现，提供类型安全的面向对象模块结构
- 高层工作流抽象：Experiment/Run/Model Manager
- 可与 TensorFlow.js 等 JavaScript ML 库配合使用

## 适用场景

- 在 JavaScript/TypeScript 项目中记录 ML 实验指标与参数
- 通过代码管理 MLflow 模型注册表的版本、别名与标签
- 在浏览器/客户端环境中集成 MLflow 工作流

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L9:  MLflow.js is an open-source JavaScript library that helps developers track machine learning experiments and manage 
> L13:  MLflow.js covers all REST API endpoints under MLflow's Tracking Server and Model Registry. Moreover, high-level ab

## 星数曲线

```mermaid
xychart-beta
    title "open-source-labs/mlflow-js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-29 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `644f34369da6` · [字段定义](../../DATASET.md)*
