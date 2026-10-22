# caraml-dev/merlin

⭐ 184 · Go · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/caraml-dev/merlin) · 组织维护

**Kubernetes 上 ML 模型部署与 serving 平台**

Merlin 是面向机器学习模型部署与线上服务的平台，以 Project/Model/Version/Endpoint 为核心概念，将部署与 serving 的基础设施复杂度抽象掉，供使用者在生产环境自助部署模型。平台构建于 Knative 与 KFServing 之上，提供 serverless 自动伸缩的推理服务。提供 Python SDK、API 文档（make swagger-ui 启动）以及经 Swagger Codegen 自动生成的 Golang 与 Python 客户端库。README 声明项目仍在活跃开发中，完整文档位于 docs 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Project/Model/Version/Endpoint 概念抽象部署流程
- 基于 Knative 与 KFServing 的 serverless 自动伸缩 serving
- 提供 Python SDK 与 Swagger Codegen 生成的 Golang/Python 客户端

## 适用场景

- 在 Kubernetes 环境中自助部署 ML 模型到生产
- 为模型服务配置自动伸缩的 serverless 推理端点
- 通过 Python SDK 或 API 客户端程序化管理模型版本与端点

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: Merlin is a platform for deploying and serving machine learning models. The project was born of the belief that mode
> L13: * **Autoscaling**: Merlin is built on top Knative and KFServing to provide a production ready serverless solution.

## 星数曲线

```mermaid
xychart-beta
    title "caraml-dev/merlin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 183 --> 185
    line [184, 184]
```

2026-10-18 184 → 2026-10-22 184（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `eb542277df37` · [字段定义](../../DATASET.md)*
