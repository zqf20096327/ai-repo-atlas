# krokozyab/ofrag

⭐ 16 · 推送 2026-04-05 · [GitHub](https://github.com/krokozyab/ofrag) · 个人维护

**面向 Oracle Fusion ERP 的 MCP 服务器，让 AI agent 自然语言查数据**

MCP 服务器，为 Claude、OpenAI、Gemini 等 MCP 兼容 agent 提供对 Oracle Fusion Cloud 数据的结构化访问：通过 30+ 工具在本地元数据缓存上进行语义表/列发现、AST 校验 SQL 后经 BI Publisher SOAP 只读执行，并支持 REST 调用、BI 报表运行、ESS 作业、多环境切换。面向 Oracle Fusion 顾问与实施/数据团队，以 Windows/macOS 二进制发布，附安装配置指南。限制：仅支持 SELECT 查询。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30+ MCP 工具：语义搜索、SQL lint/执行、REST、BI 报表、ESS 作业、环境切换
- 本地 schema 缓存上做发现与 AST 校验，仅最终 SQL 触达生产实例
- 跨模块 JOIN 关系与业务流程映射（AP→XLA→GL 链路）
- DEV/SIT/UAT/PROD 多环境同会话切换与配置对比

## 适用场景

- 用自然语言对 Oracle Fusion 做即席数据查询与分析
- 实施期间核验 AP/GL 数据并做子账与总账对账
- EBS 到 Fusion 迁移时映射对应表
- 构建 BI Publisher 报表前在对话中验证 SQL

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L36: ofrag is an **MCP (Model Context Protocol) server** — an open standard that lets AI agents use external tools. It g
> L45: **Key principle:** All schema exploration happens locally — zero queries to production during discovery. Only final
> L161: - **Read-only SQL** — `SELECT` queries only through BI Publisher SOAP. Oracle Fusion does not permit write access 

## 星数曲线

```mermaid
xychart-beta
    title "krokozyab/ofrag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3d59067cd8c4` · [字段定义](../../DATASET.md)*
