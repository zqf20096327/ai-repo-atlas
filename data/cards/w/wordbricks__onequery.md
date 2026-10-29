# wordbricks/onequery

⭐ 17 · TypeScript · Apache-2.0 · 推送 2026-07-30 · [GitHub](https://github.com/wordbricks/onequery) · [官网](https://onequery.dev) · 组织维护 · 中文 README

**自托管数据查询网关：统一连接数据库与分析工具，安全可审计**

用 Rust 编写的自托管查询服务：集中管理 15+ 数据源（PostgreSQL、Snowflake、BigQuery、MongoDB、GitHub 等）的连接与凭据，通过 CLI 与 Web UI 执行带防护的查询——只读校验、单语句限制、查询成本上限与完整审计日志。支持组织级 RBAC，云端版含 SSO/SAML。另提供 Claude Code、OpenClaw、Hermes 等 agent 插件/技能，使 agent 可直接调用其 CLI 查询数据。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一接入 15+ 数据源（数据库、分析工具、API）并集中管理凭据
- 查询防护：只读校验、单语句强制、成本上限、审计日志
- 提供 CLI 与 Web UI 两种使用界面
- 面向 Claude Code / OpenClaw / Hermes 提供 agent 插件与技能

## 适用场景

- 团队统一连接多种数据库与分析工具，避免各自保存凭据
- 给 AI agent 安全地开放数据查询能力（只读、限额、可审计）
- 企业内部对查询历史做审计与权限管控

## 场景标签

 · 领域:数据基础设施/查询网关

## 证据(README 行号)

> L10: **Self-host OneQuery to connect databases, analytics tools, and APIs, manage credentials centrally, and run safe, a
> L18: |**Safe querying**|Read-only validation, single-statement enforcement|✓|
> L89: The `onequery` Claude Code plugin ships from the Wordbricks marketplace:

## 星数曲线

```mermaid
xychart-beta
    title "wordbricks/onequery 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `79b10bf93a5f` · [字段定义](../../DATASET.md)*
