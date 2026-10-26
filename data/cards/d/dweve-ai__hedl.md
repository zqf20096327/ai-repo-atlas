# dweve-ai/hedl

⭐ 78 · Rust · Apache-2.0 · 推送 2026-07-29 · [GitHub](https://github.com/dweve-ai/hedl) · [官网](https://dweve.com) · 组织维护

**面向 LLM 应用的省 token 数据格式，JSON 替代**

HEDL（Hierarchical Entity Data Language）是一种为 LLM 应用设计的数据序列化格式：通过 %S 模式声明一次性定义结构，行内只传值，按其基准报告较 JSON 平均减少 56% token。提供 Rust 库、CLI、MCP Server（AI agent 发 JSON 由服务端自动转换，无需改代码）、LSP 编辑器集成、WASM 与 C/C++/Python FFI 绑定；支持与 JSON/YAML/XML/CSV/Parquet/Neo4j Cypher 的双向转换、schema 校验、实体引用与流式解析。README 同时列出不适场景：需要最大生态兼容、数据量极小或团队不愿换格式时应保留 JSON。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模式声明去重复键，报告平均省 56% token
- MCP Server 零代码接入 AI agent，自动 JSON↔HEDL 转换
- 支持 JSON/YAML/XML/CSV/Parquet/Neo4j Cypher 双向转换
- 提供 CLI、LSP、WASM、C/C++/Python FFI 等 19 个 crate 组成的模块化生态

## 适用场景

- 高并发 RAG/LLM 服务压缩 prompt 中的结构化数据以降低 token 成本
- ETL 流水线中做格式转换与流式解析
- 知识图谱构建中用 @Type:id 引用做实体解析并导出 Neo4j Cypher
- 配置管理中用 schema 校验与 LSP 补全编辑配置文件

## 场景标签

 · 领域:数据序列化/LLM 基础设施

## 证据(README 行号)

> L5:  The Token-Efficient Data Format for LLM Applications
> L63: The MCP server handles everything automatically. Your AI agent sends JSON like it always did, the server converts t
> L263: |**MCP Server**|`hedl-mcp`|AI agent tools for Claude and other MCP-compatible systems|

## 星数曲线

```mermaid
xychart-beta
    title "dweve-ai/hedl 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 76 --> 79
    line [77, 78, 78]
```

2026-10-18 77 → 2026-10-26 78（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c9b2bfdd1ecd` · [字段定义](../../DATASET.md)*
