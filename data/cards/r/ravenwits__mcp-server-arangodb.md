# ravenwits/mcp-server-arangodb

⭐ 46 · TypeScript · MIT · 推送 2026-06-01 · [GitHub](https://github.com/ravenwits/mcp-server-arangodb) · 个人维护

**让 AI 客户端通过 MCP 操作 ArangoDB 的 TypeScript 服务器**

基于 TypeScript 实现的 Model Context Protocol 服务器，向 MCP 客户端（Claude Desktop、VSCode Copilot Agent、Cline、OpenCode、WARP）暴露 30 个操作 ArangoDB 的工具，覆盖 AQL 查询与校验、集合/文档/索引管理、ArangoSearch 全文检索、图遍历与最短路径、JSON 文件备份。通过环境变量配置连接，工具返回 JSON 与 structuredContent，读操作带 limit 边界，查询支持 memoryLimit/maxRuntime 等护栏。README 明确声明仅限本地开发环境使用，不建议连接生产数据库。

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

- 30 个 MCP 工具覆盖查询、集合、文档、索引、ArangoSearch、图操作与备份
- 查询工具支持 bind 变量、limit 边界与 memoryLimit/maxRuntime 护栏
- 备份工具拒绝绝对路径、路径穿越与符号链接逃逸
- 支持 Claude Desktop / VSCode Copilot / Cline / OpenCode / WARP 配置接入

## 适用场景

- 在 Claude 等 AI 客户端中用自然语言查询和管理 ArangoDB
- 开发环境下让 agent 执行 AQL、插入文档或建集合
- 对 ArangoSearch 视图做 BM25 检索与图遍历分析

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: A Model Context Protocol server for ArangoDB
> L7: This is a TypeScript-based MCP server that provides database interaction capabilities through ArangoDB. It implement

## 星数曲线

```mermaid
xychart-beta
    title "ravenwits/mcp-server-arangodb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `711c45035d74` · [字段定义](../../DATASET.md)*
