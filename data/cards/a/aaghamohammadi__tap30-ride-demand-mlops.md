# aaghamohammadi/tap30-ride-demand-mlops

⭐ 13 · Jupyter Notebook · Apache-2.0 · 推送 2026-01-13 · [GitHub](https://github.com/aaghamohammadi/tap30-ride-demand-mlops) · [官网](https://www.kaggle.com/competitions/tap30challenge/data) · 个人维护

**德黑兰出租车需求预测的端到端 MLOps 项目**

基于 Tapsi（伊朗网约车公司）公开的德黑兰网格化出行数据，构建端到端 ML 流水线：数据摄取（对接云对象存储）、数据处理、用 sklearn 训练 Random Forest 模型预测各区域不同时段的出租车需求。工程侧用 FastAPI 提供 /predict 推理 API，MLflow 做实验跟踪，Docker 容器化，GitHub Actions 自动构建推送镜像，Kubernetes 部署。面向想参考 MLOps 完整实践的开发者，README 未提供直接的安装运行命令，仅给出部署后的 curl 测试示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据摄取→处理→Random Forest 训练的三段式流水线
- FastAPI 提供预测 Web API
- MLflow 实验跟踪 + Docker + GitHub Actions + Kubernetes 部署链路

## 适用场景

- 参考完整 MLOps 流水线（训练到 K8s 部署）的实现
- 学习网约车需求预测的建模与服务化流程
- 基于 Tapsi 公开数据复现需求预测

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L14: The company shares a portion of their data for taxi demand in Tehran, which is divided into grid cells (rows and co
> L19: - **Model Training**: Trains a Random Forest model (using sklearn) on the processed data.

## 星数曲线

```mermaid
xychart-beta
    title "aaghamohammadi/tap30-ride-demand-mlops 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `c9266d1caeb7` · [字段定义](../../DATASET.md)*
