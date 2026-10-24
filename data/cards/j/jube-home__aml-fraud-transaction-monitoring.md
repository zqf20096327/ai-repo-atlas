# jube-home/aml-fraud-transaction-monitoring

⭐ 115 · C# · AGPL-3.0 · 推送 2026-10-18 · [GitHub](https://github.com/jube-home/aml-fraud-transaction-monitoring) · [官网](https://www.jube.io) · 组织维护

**开源实时反洗钱与欺诈交易监控平台，带 AI 代理问答**

面向合规/反欺诈场景的开源实时交易监控平台：混合检测引擎结合规则、速率与制裁名单筛查以及有监督/无监督 ML（含可解释 ML），提供案例管理、合规人员可编辑的规则构建器、云原生多租户架构与横向扩展。其 agentic AI 层“Ask Jooby”由 150+ Joobriks AI 代理组成，以自然语言问答替代菜单与查询语言，每一步经平台验证；默认推理后端为 DigitalOcean Serverless Inference，可切换至任意 OpenAI 兼容端点。通过 Docker Compose 从源码构建部署，单节点用于评估，生产环境提供 Jube Cluster（Docker Swarm 高可用集群）。AGPLv3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合检测：规则+速率+制裁筛查，叠加有监督与无监督可解释 ML
- Ask Jooby：150+ AI 代理（Joobriks）自然语言执行监控任务，推理端点可切换为任意 OpenAI 兼容服务
- 案例管理与合规人员可编辑的规则构建器
- 生产级 Jube Cluster：Docker Swarm 高可用、Patroni/PostgreSQL 自动故障转移与 WAL 时间点恢复

## 适用场景

- 金融机构实时监控交易以履行反洗钱合规义务
- 合规团队通过自然语言提问完成调查与取证步骤
- 在自有基础设施上部署可解释、可审计的欺诈检测系统

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: **Open-source agentic AI for transaction monitoring. “Just ask Jooby.”** Real-time AML and fraud monitoring, run by 
> L19: on it, and all of it is in the open: explainable ML, hybrid detection (rules, velocity and sanctions, plus supervis
> L20: and unsupervised ML), real-time and horizontally scalable, case management, a rule builder compliance can edit,

## 星数曲线

```mermaid
xychart-beta
    title "jube-home/aml-fraud-transaction-monitoring 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 114 --> 116
    line [115, 115]
```

2026-10-18 115 → 2026-10-24 115（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `42c10f056dbe` · [字段定义](../../DATASET.md)*
