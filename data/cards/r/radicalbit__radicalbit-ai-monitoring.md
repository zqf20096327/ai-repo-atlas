# radicalbit/radicalbit-ai-monitoring

⭐ 92 · Python · Apache-2.0 · 推送 2026-06-15 · [GitHub](https://github.com/radicalbit/radicalbit-ai-monitoring) · [官网](https://docs.oss-monitoring.radicalbit.ai/) · 组织维护

**生产环境 ML/LLM 模型监控平台：数据质量、模型质量与漂移检测**

Radicalbit 维护的 AI 模型监控平台，面向在生产环境中运行机器学习与大语言模型的团队。平台分析参考数据集与当前数据集，监控数据质量、模型质量与模型漂移；指标计算通过 Spark 作业完成，使用 K3s 集群部署。仓库包含 ui、api、sdk、spark 四个组件，以 Docker Compose 一键启动，可选 UI 与演示数据；默认用 MinIO，可切换真实 AWS S3。目前支持表格数据的二分类/多分类/回归批量监控与 LLM 数据质量，LLM 模型质量、计算机视觉与实时负载在路线图中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 监控数据质量、模型质量与模型漂移三类指标
- Spark 作业计算指标，K3s 集群部署
- Docker Compose 一键启动，可加载演示模型
- 提供 Python SDK 与文档

## 适用场景

- 模型上线后持续监控性能衰退与数据/概念漂移
- 对比参考数据集与生产数据集检测数据质量问题
- 监控表格数据分类/回归模型与 LLM 数据质量

## 场景标签

`LLM 可观测性` `MLOps` · 领域:评测与运维

## 证据(README 行号)

> L17: The **Radicalbit AI Monitoring Platform** provides a comprehensive solution for monitoring your Machine Learning an
> L23: The platform provides extensive monitoring capabilities to ensure optimal performance of your AI models in producti
> L109: We've released a first few dashboards, covering Classification, both Binary and Multiclass, and Regression models 

## 星数曲线

```mermaid
xychart-beta
    title "radicalbit/radicalbit-ai-monitoring 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-31 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d161f4edbc3d` · [字段定义](../../DATASET.md)*
