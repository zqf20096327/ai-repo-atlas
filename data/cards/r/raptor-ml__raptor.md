# raptor-ml/raptor

⭐ 164 · Go · Apache-2.0 · 推送 2026-01-31 · [GitHub](https://github.com/raptor-ml/raptor) · [官网](https://raptor.ml) · 组织维护

**给数据科学家的特征工程平台：Python 研究代码编译为生产制品**

面向数据科学家与 ML 工程师的特征工程与部署平台。LabSDK 以 Python 包形式在 notebook/IDE 中开发模型与特征，通过装饰器声明式定义加函数代码，导出为含 Makefile 的生产制品，部署到 Kubernetes 后由 Raptor Core 管理扩展性、缓存、监控等工程事项。内置缓存与历史数据存储，可替代独立 Feature Store 的预计算编排；模型可部署到 Sagemaker 等服务端。生产部署前置条件为 Kubernetes 集群与 Redis，Snowflake/S3 为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python 研究代码经装饰器声明编译为生产制品
- 同一代码用于训练与生产以消除 serving/training skew
- 内置缓存与历史存储，无需独立 Feature Store 编排
- 基于 Kubernetes 的扩展、自恢复、监控等能力

## 适用场景

- 在 notebook 中开发特征并直接导出部署到生产
- 避免训练与线上服务之间的特征偏差
- 数据科学家不写后端代码即可上线 ML 功能

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L21: It **compiles** your python research code to production artifacts, and takes care of the engineering concerns such 
> L36: With Raptor, you can export your Python research code as **standard production artifacts**, and deploy them to
> L137: standard tools; Once deployed, Raptor Core(the server-side part) is extending Kubernetes with the ability to imple

## 星数曲线

```mermaid
xychart-beta
    title "raptor-ml/raptor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 163 --> 165
    line [164, 164]
```

2026-10-18 164 → 2026-10-26 164（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b2443ee87321` · [字段定义](../../DATASET.md)*
