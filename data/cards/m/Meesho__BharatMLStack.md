# Meesho/BharatMLStack

⭐ 716 · Go · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/Meesho/BharatMLStack) · 组织维护 · 中文 README

**企业级端到端 ML 基础设施栈：实时特征、推理与向量检索**

Meesho 开源的云无关 ML 基础设施平台，覆盖实时特征服务、模型推理编排与向量相似度检索。核心组件包括 TruffleBox UI（特征注册控制台）、在线特征存储、Inferflow（DAG 式推理编排）、Numerix（Rust 数学计算引擎）、Skye（可插拔后端的向量检索）、Go/Python SDK 与 Horizon 控制平面。面向需要在生产环境运行实时/批处理 ML 负载的工程团队，通过 git clone 加 Docker Compose 快速启动。README 自述在 Meesho 电商场景承载百万级 QPS。采用 Business Source License 1.1 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在线特征存储自称 Sub-10ms 检索、百万级 QPS
- Inferflow 提供 DAG 式实时推理编排，支持深度学习与 LLM 部署
- Skye 向量检索支持可插拔后端
- 提供 Go 与 Python SDK

## 适用场景

- 为推荐系统提供低延迟特征服务与实时排序
- 流式摄取交互信号做欺诈与风险检测
- 大规模图像检索的向量相似度搜索
- 在 GPU 集群上编排深度学习与 LLM 推理流水线

## 场景标签

`向量数据库` `MLOps` `推理引擎` · 领域:知识与检索

## 证据(README 行号)

> L12: BharatMLStack is a production-ready, cloud-agnostic ML infrastructure platform that powers real-time feature servin
> L59: |**Inferflow**|DAG-based real-time inference orchestration for composable ML pipelines|`v1.0.0`|Docs|

## 星数曲线

```mermaid
xychart-beta
    title "Meesho/BharatMLStack 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 714 --> 717
    line [715, 716, 716]
```

2026-10-18 715 → 2026-10-29 716（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `04128890db82` · [字段定义](../../DATASET.md)*
