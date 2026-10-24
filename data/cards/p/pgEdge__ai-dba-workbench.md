# pgEdge/ai-dba-workbench

⭐ 49 · Go · PostgreSQL · 推送 2026-10-23 · [GitHub](https://github.com/pgEdge/ai-dba-workbench) · [官网](https://docs.pgedge.com/ai-dba-workbench) · 组织维护

**面向 PostgreSQL 实例的监控管理系统，含可选 AI agent**

pgEdge 公司维护的 PostgreSQL v14+ 监控与管理统一环境，兼容 Supabase 与 Amazon RDS。由四个组件构成：Collector 采集指标存入集中式数据存储、Server 提供 MCP 工具与资源、Alerter 基于阈值与 AI 异常检测生成告警、Client 提供 Web 界面。通过 MCP Server 将 Spock 复制状态、集群配置与运营指标暴露给语言模型，支持云端 LLM（如 Claude）与本地 Ollama 模型切换，可在隔离环境运行。安装方式包括二进制文件、源码编译、Docker 容器与 pgEdge 仓库软件包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | PostgreSQL |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四组件架构：Collector/Server/Alerter/Client
- MCP Server 将 pgEdge 工具与数据源暴露给语言模型
- 阈值与 AI 异常检测结合的告警生成
- 支持云端 LLM 与本地 Ollama 模型切换

## 适用场景

- 监控 PostgreSQL 集群并在异常演变为故障前发现
- 用自然语言查询和管理分布式数据库集群
- 在隔离或安全环境中部署带 AI 能力的数据库监控

## 场景标签

 · 领域:数据库运维/监控

## 证据(README 行号)

> L21: The Workbench combines a Model Context Protocol (MCP) Server with a
> L29: Claude and locally hosted models from Ollama. This design ensures similar

## 星数曲线

```mermaid
xychart-beta
    title "pgEdge/ai-dba-workbench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 47 --> 50
    line [48, 49, 49]
```

2026-10-18 48 → 2026-10-24 49（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5085c2ee3913` · [字段定义](../../DATASET.md)*
