# DecisionsDev/odm-ondocker

⭐ 54 · Shell · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/DecisionsDev/odm-ondocker) · [官网](https://odmdev.github.io/odm-ondocker/) · 组织维护

**用 Docker Compose 部署 IBM ODM 决策平台的仓库**

集中提供 IBM Operational Decision Manager 的 Docker 部署材料：Dockerfile 用于构建 ODM 各运行时组件镜像，docker-compose 描述文件用于组合构建、推送镜像并运行拓扑，覆盖 Standalone（开发）、Standard（预生产）、Clustered（生产）三种拓扑。适用于 ODM Standard V9.0.x 及至 v8.11.x 的早期版本，面向需要容器化部署该商业决策平台的运维或开发人员；需持有相应许可，另含 Kubernetes 部署的独立仓库。仓库采用 Apache 2.0 许可。

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

- 提供 ODM 运行时组件的 Dockerfile 与 docker-compose 描述文件
- 三种部署拓扑：Standalone/Standard/Clustered，支持容器数量扩展
- 覆盖 ODM Standard V9.0.x 至 v8.11.x 版本

## 适用场景

- 在开发环境用单一镜像快速运行 ODM 全组件
- 为预生产/生产环境按组件构建镜像并扩展容器数量
- 配合镜像仓库推送与运行 ODM 拓扑

## 场景标签

 · 领域:业务决策管理/容器化部署

## 证据(README 行号)

> L10: This repository centralizes the material to deploy IBM Operational Decision Manager in Docker.
> L13: IBM ODM is a decisioning platform to automate your business policies. Business rules are used at the heart of the p

## 星数曲线

```mermaid
xychart-beta
    title "DecisionsDev/odm-ondocker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-30 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `38f8229952b3` · [字段定义](../../DATASET.md)*
