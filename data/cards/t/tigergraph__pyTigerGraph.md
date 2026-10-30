# tigergraph/pyTigerGraph

⭐ 39 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/tigergraph/pyTigerGraph) · [官网](https://docs.tigergraph.com/pytigergraph/current/intro/) · 组织维护

**TigerGraph 图数据库的 Python 客户端库**

封装 TigerGraph 数据库 REST++ 与 GSQL API 的 Python 客户端，提供同步与异步（aiohttp）两种连接接口，支持 token/JWT 认证与 TigerGraph Cloud HTTPS 连接。可选扩展：gds 子模块将顶点/边数据流式加载到 PyTorch Geometric、DGL 或 Pandas 供机器学习使用；mcp 扩展现已独立为 pyTigerGraph-mcp 包，将数据库操作暴露为 AI agent 工具；fast 扩展用 orjson 加速 JSON 解析。通过 pip/conda 安装，面向使用 TigerGraph 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同步与异步双接口，异步模式共享 aiohttp 连接池
- gds 子模块提供到 PyTorch Geometric/DGL/Pandas 的数据加载器
- 独立 MCP 服务器包将 TigerGraph 操作暴露为 AI agent 工具
- orjson 可选后端加速 JSON 解析，未安装时透明回退标准库

## 适用场景

- 在 Python 程序中连接并查询 TigerGraph 图数据库
- 把图数据流式加载进 GNN 框架做图机器学习
- 让 Claude Desktop/Cursor 等 AI agent 通过 MCP 操作图数据库

## 场景标签

 · 领域:数据库/图数据

## 证据(README 行号)

> L3: pyTigerGraph is a Python client for TigerGraph databases. It wraps the REST++ and GSQL APIs and provides both a sync
> L165: The TigerGraph MCP server is now a standalone package: **pyTigerGraph-mcp**. It exposes TigerGraph operations as t

## 星数曲线

```mermaid
xychart-beta
    title "tigergraph/pyTigerGraph 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-30 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7d576737583f` · [字段定义](../../DATASET.md)*
