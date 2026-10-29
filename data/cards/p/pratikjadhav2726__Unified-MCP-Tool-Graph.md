# pratikjadhav2726/Unified-MCP-Tool-Graph

⭐ 28 · Python · MIT · 推送 2026-03-12 · [GitHub](https://github.com/pratikjadhav2726/Unified-MCP-Tool-Graph) · 个人维护

**MCP 工具图谱层：用 Neo4j 图库为 LLM 检索最相关工具**

将多个 MCP 服务器的工具 API 聚合并结构化为 Neo4j 图数据库，记录工具元数据与 overlaps_with、preferred_for 等关系边；LLM/Agent 执行任务时通过 Dynamic Tool Retriever MCP 查询图谱，仅返回所需工具及其 MCP 服务器配置，按需拉起服务器（闲置 10 分钟后关闭，5 个常用 MCP 常驻），避免工具过载与循环调用。提供 MCP 统一网关（端口 8000）、A2A 与 LangGraph 示例 agent；使用 mcp-proxy 将 stdio 服务器暴露为 HTTP/SSE。README 声称支持 11066 个工具、4161 个 MCP 服务器；摄取脚本、Schema 蓝图等列为 Coming Soon。MIT 许可，已集成进 SmarterMCP 预览模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Neo4j 图数据库集中存储跨 MCP 服务器的工具元数据与关系边（overlaps_with/extends/preferred_for_task）
- 按查询动态返回 3-4 个最相关工具及对应 MCP 服务器配置
- 按需启动 MCP 服务器，5 个常用 MCP 常驻，闲置 10 分钟后关闭
- 使用 mcp-proxy 将 stdio MCP 服务器暴露为 Streamable HTTP/SSE 端点

## 适用场景

- Agent 面对大量 MCP 工具时只加载当前任务所需工具，避免选错或死循环
- 企业自定义助手按权限/范围从图谱过滤暴露内部工具
- 跨供应商（LinkedIn、Google、Notion 等）工具统一编目与链式调用推荐

## 场景标签

`Agent 框架` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Unified MCP Tool Graph** is a research-driven project that aggregates and structures tool APIs from diverse **Mode
> L133: 2. **Dynamic Tool Retriever MCP** queries the Neo4j graph and returns the most relevant tools **plus their MCP ser
> L135: 4. **Agent** (A2A or LangGraph) loads only the retrieved tools and executes the workflow.

## 星数曲线

```mermaid
xychart-beta
    title "pratikjadhav2726/Unified-MCP-Tool-Graph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7f68ea7404d0` · [字段定义](../../DATASET.md)*
