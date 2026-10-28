# aliengiraffe/spotdb

⭐ 21 · Go · MIT · 推送 2026-10-26 · [GitHub](https://github.com/aliengiraffe/spotdb) · 个人维护

**面向 AI agent 的临时 SQL 数据沙箱：CSV 上传、隔离查询、带护栏**

基于 DuckDB 的轻量临时数据沙箱，为 LLM 与 agentic 工作流提供安全隔离的 SQL 分析环境，避免 agent 直接访问生产数据库。功能包括临时数据库创建、数据快照与状态恢复、MCP API 与 REST API 两种访问方式、护栏规则与安全防护。通过 Homebrew 安装后运行 spotdb 命令启动服务，支持 curl 上传 CSV 与查询，带浏览器 Explorer UI，并可注册为 Claude Code 的 MCP 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 DuckDB 的临时数据沙箱，agent 无需接触生产库
- 同时提供 MCP API 与 REST API 访问通道
- 数据快照与时间点状态恢复
- 护栏规则与安全防护机制

## 适用场景

- 让 AI agent 在隔离沙箱里查询我上传的 CSV 数据
- 为 agentic 工作流提供带安全护栏的 SQL 分析环境
- 通过浏览器 Explorer UI 快速探索数据

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: This project provides a lightweight, **ephemeral data sandbox** designed for large language models (LLMs) and agenti
> L13: - 🧠 **MCP API**: Access data through a Model Context Protocol for seamless integration with AI models and agentic w

## 星数曲线

```mermaid
xychart-beta
    title "aliengiraffe/spotdb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `5150f1683e72` · [字段定义](../../DATASET.md)*
