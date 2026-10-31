# spences10/mcp-turso-cloud

⭐ 18 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/spences10/mcp-turso-cloud) · 个人维护

**让 LLM 通过 MCP 直接管理与查询 Turso 数据库的服务器**

面向 Turso（libSQL/SQLite）数据库的 Model Context Protocol 服务器，供 Cline、Claude Desktop 等 MCP 客户端接入。实现两级认证：组织级 Platform API token 管理数据库的创建/删除/列举/发 token，数据库级 token 执行查询。读写工具分离：只读工具始终申请只读凭据，本地校验拒绝多语句与变更型 PRAGMA；支持向量相似度检索。以 Node.js 实现，开发用 pnpm，需配置 TURSO_API_TOKEN 等环境变量。

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

- 组织级与数据库级两级认证，token 按权限缓存并轮换
- 只读/破坏性 SQL 工具分离，读路径不回退到全量权限
- 基于 SQLite 向量扩展的 vector_search（1–4096 维）
- 分页与 512 KiB 结果预算的截断元信息

## 适用场景

- 在 Claude Desktop/Cline 中对话式管理 Turso 数据库
- 让 LLM 执行带审批分级的 SQL 查询
- 通过 MCP 对 Turso 库做向量检索

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that provides integration with
> L6: database-level operations, making it easy to manage and query Turso

## 星数曲线

```mermaid
xychart-beta
    title "spences10/mcp-turso-cloud 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `b6f007027681` · [字段定义](../../DATASET.md)*
