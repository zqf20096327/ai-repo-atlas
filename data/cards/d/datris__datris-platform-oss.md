# datris/datris-platform-oss

⭐ 13 · Scala · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/datris/datris-platform-oss) · [官网](https://datris.ai) · 组织维护

**面向 AI agent 的自托管数据控制平面：MCP 接入数据获取、校验与落地**

自托管的 AI agent 数据控制平面：通过单个 MCP server（88 个工具）暴露数据能力，Claude Desktop、Cursor 等 MCP 客户端可学习统一接口。提供凭据 Vault 代管、按 agent 的作用域密钥、审批门与审计日志；AI 功能包括自然语言生成 tap 采集脚本、校验/转换脚本、数据画像、错误解释、自然语言查 SQL 与 RAG 管道。管道含字段脱敏/加密等保护阶段，支持 CSV/JSON/PDF 等格式。基础设施 100% 开源（MinIO/PostgreSQL/MongoDB/Vault 等），Apache-2.0，无托管服务。全栈需约 8 GB Docker 内存，最小安装约 4 GB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个 MCP server 聚合 88 个数据工具供 AI agent 调用
- Vault 代管凭据，agent 脚本在无密钥的隔离容器中运行
- 作用域密钥、审批门与审计日志的治理机制
- AI 生成 tap/校验/转换脚本、数据画像、自然语言查询与 RAG 管道

## 适用场景

- 让 Claude/Cursor 等 agent 通过统一 MCP 接口完成数据采集与加载
- 在敏感字段进入 AI 阶段前做脱敏、掩码或加密
- 自托管一套带审计与审批流程的 agent 数据管道平台

## 场景标签

`RAG` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L28: - **One MCP door** — 88 tools behind a single MCP server. Claude, Cursor, and any MCP-compatible agent learn one in
> L12: Agents ask Datris for data. Datris finds it, acquires it, validates it, lands it in the stores you already run, and
> L135: |**MCP Server**|88 tools for AI agents — pipeline CRUD, upload, query, search, profiling, taps, catalogs, provenan

## 星数曲线

```mermaid
xychart-beta
    title "datris/datris-platform-oss 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `6e9a47a00670` · [字段定义](../../DATASET.md)*
