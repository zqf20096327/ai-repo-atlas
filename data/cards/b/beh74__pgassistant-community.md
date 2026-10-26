# beh74/pgassistant-community

⭐ 57 · JavaScript · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/beh74/pgassistant-community) · [官网](https://beh74.github.io/pgassistant-blog/) · 个人维护

**面向开发者的 PostgreSQL 持续优化平台：分析、规划与度量改进**

开源 Web 平台，连接 PostgreSQL 实例后通过确定性顾问（Global/Index/Parameter/Autovacuum/Fillfactor）分析模式、索引、配置与维护问题，将发现整合为按优先级排序的 Executive Plan 工作包，并可生成面向 DEV/OPS 的 PDF 报告。Collector 组件采集历史工作负载快照，Workload Insights 对比采集结果度量改进效果。支持单库深度分析与数百上千库的舰队模式。AI 辅助为可选项（SQL 重写、命名检查等），核心顾问不依赖 LLM。通过 Docker 镜像部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性顾问体系覆盖索引、参数、Autovacuum、模式与配置检查
- Executive Plan 将发现整合为按优先级排序的工作包并生成 PDF 报告
- Collector 采集历史快照，对比度量工作负载改进结果
- 支持单库分析与数百上千库的舰队集中管理
- AI 辅助可选，核心顾问不依赖 LLM

## 适用场景

- 系统性地排查和修复 PostgreSQL 的索引、配置与维护问题
- 把数据库优化建议整理成团队可执行的工作包并跟踪实施
- 管理大量 PostgreSQL 实例并按优先级决定先改哪个
- 度量优化措施对实际工作负载的影响

## 场景标签

 · 领域:数据库运维/开发工具

## 证据(README 行号)

> L34: AI assistance is optional. The core advisors remain deterministic and can be used without an LLM.
> L99: - **Optional LLM assistance** — request SQL rewrites, schema-design feedback, naming checks, and contextual explana

## 星数曲线

```mermaid
xychart-beta
    title "beh74/pgassistant-community 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 55 --> 58
    line [56, 57, 57]
```

2026-10-18 56 → 2026-10-26 57（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `73fc95d587a4` · [字段定义](../../DATASET.md)*
