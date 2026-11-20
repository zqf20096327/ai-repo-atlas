# cookieY/Yearning

⭐ 8,979 · Go · AGPL-3.0 · 推送 2026-11-19 · [GitHub](https://github.com/cookieY/Yearning) · [官网](https://v4.yearning.io/) · 组织维护 · 中文 README

**给 DBA/平台团队提供 AI 预检与治理的 SQL 审核变更平台**

面向 MySQL/PostgreSQL/TiDB/OceanBase/PolarDB 的 SQL 审核与数据库变更治理平台，采用 Go 单体二进制加 React 前端与 PostgreSQL 元数据存储。机制包括：SQL 变更提交前经确定性加 AI 两阶段预检（语句指纹去重后仅审查代表样本）、提交时冻结多级审批快照、内置进程内 gh-ost 在线 DDL、跨引擎基于前镜像的回滚、只读查询工单与列脱敏、Top-SQL 性能诊断。AI 能力以 OpenAI 兼容云端接口或本地自托管模型（vLLM/Ollama）运行，支持每日成本预算。通过企业邮箱提供商业支持与许可咨询。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零泄漏 AI 预检：SQL 字面量与标识符在内存中匿名化，指纹分组后仅审查代表语句
- 提交时加密冻结审批流程与 SQL SHA-256，任何角色不可改派或跳过
- 内置进程内 gh-ost 在线 DDL 与跨引擎免 binlog 回滚
- 双轨 AI 隔离：云端匿名化通道与本地 vLLM/Ollama 自托管通道

## 适用场景

- 为生产库的 DDL/DML 变更设置多级审批与审计留痕
- 在不暴露数据库凭据的前提下给开发者只读查询与导出权限
- 用本地自托管模型做 SQL 风险预检避免语句外泄
- 对慢 SQL 生成根因分析与索引建议并转入变更工单

## 场景标签

 · 领域:数据库工具/DevOps

## 证据(README 行号)

> L9: **AI-Powered Database Change Governance & SQL Review Platform**
> L50: **Yearning v4** is a ground-up architectural rebuild of the open-source Yearning SQL audit and database governance 
> L99:  - **`san` Track (Local Self-Hosted Models via vLLM / Ollama)**: Compact Raw-SQL Native prompts on internal RFC1918


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `f5d19edae015` · [字段定义](../../DATASET.md)*
