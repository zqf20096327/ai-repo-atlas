# mlop-ai/server

⭐ 15 · Shell · Apache-2.0 · 推送 2026-03-05 · [GitHub](https://github.com/mlop-ai/server) · [官网](https://mlop.ai) · 组织维护

**mlop 实验追踪服务器的自托管部署集合**

由 mlop 团队提供的自托管服务集合，用于存储、分析、可视化并分享 mlop 客户端或其他平台录制的机器学习实验数据。通过 docker-compose 部署，包含前端/后端（端口3000/3001）、Rust 高性能数据接入服务（3003）、Python 健康监控服务（3004）、S3 兼容存储（9000）、ClickHouse 与 PostgreSQL 数据库（默认不暴露端口）。数据由用户完全控制并本地映射到主机目录，迁移时携带 .mlop 文件夹与 .env 即可。另提供 mlop.ai 托管实例选项。

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

- docker-compose 一键自托管部署，Web 服务位于 localhost:3000
- Rust 服务处理高性能数据接入（端口3003）
- 内置 S3 兼容存储、ClickHouse 与 PostgreSQL 数据库
- 数据完全由用户控制，本地目录映射，迁移仅需 .mlop 文件夹与 .env

## 适用场景

- 团队或个人自托管机器学习实验追踪服务，不依赖官方托管
- 将实验数据存储、可视化并分享给协作者
- 把已有 mlop 客户端指向自建服务器进行实验记录

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: This is the collection of services that allow any individual to self-host their own instance of the **mlop** server.
> L5: For a managed instance with better scalability, stability and support, please visit mlop.ai or contact us at founder

## 星数曲线

```mermaid
xychart-beta
    title "mlop-ai/server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `51cbc91e0893` · [字段定义](../../DATASET.md)*
