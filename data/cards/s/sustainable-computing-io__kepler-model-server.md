# sustainable-computing-io/kepler-model-server

⭐ 30 · Python · Apache-2.0 · 推送 2026-03-19 · [GitHub](https://github.com/sustainable-computing-io/kepler-model-server) · 组织维护

**Kepler 功耗模型的训练与服务基础设施**

Kepler 项目的模型服务器组件，包含模型服务器、estimator、离线训练器与基于 Tekton 的训练流水线等模块，与 Kepler 核心项目和 kepler-model-db 连接，用于功耗模型的训练、存储与在线服务。部署方式包括 Kepler Operator（CRD 配置）与 manifests 脚本（可带 estimator sidecar），本地测试支持 Docker 镜像构建或原生 Python 3.10 环境（经 hatch 管理）。面向在 Kubernetes 环境中部署能耗监控/估算能力的开发者与运维人员。

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

- 模型服务器、estimator、离线训练器与训练流水线模块
- 支持 Kepler Operator CRD 与 make deploy manifests 两种部署方式
- Docker 镜像测试与原生 Python 3.10（hatch）双测试路径

## 适用场景

- 为 Kepler 部署功耗估算模型服务与 estimator sidecar
- 通过 Tekton 流水线训练功耗模型
- 本地用 Docker 或 Python 环境跑各模块测试

## 场景标签

`MLOps` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: This repository contains source code related to Kepler power model. The modules in this repository connects to core 
> L30: Deploy with estimator sidecar and model server

## 星数曲线

```mermaid
xychart-beta
    title "sustainable-computing-io/kepler-model-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `981c9bdbd4cb` · [字段定义](../../DATASET.md)*
