# wheattoast11/openrouter-deep-research-mcp

⭐ 54 · JavaScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/wheattoast11/openrouter-deep-research-mcp) · [官网](https://terminals.tech) · 个人维护

**面向多智能体深度研究的 MCP 服务器，经 OpenRouter 调度多模型**

生产级 MCP 服务器，为 MCP 客户端（Claude Desktop、Claude Code、Jan AI、Continue 等）提供多智能体研究工具：异步/同步/批量研究、上下文追问，以及 BM25+向量混合检索、SQL 查询、知识图谱遍历与 PageRank、会话时间旅行与分叉。模型经 OpenRouter API 调用，通过本地向量嵌入路由选择模型（无需 LLM 调用），支持多 key 轮换、熔断器与持久化存储。以 npx 分发，STDIO 默认、Streamable HTTP 为主推传输。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 异步/同步/批量研究与上下文追问工具集
- 嵌入路由选模型 + BM25+向量混合检索与 SQL 查询
- 知识图谱遍历、聚类与 PageRank，会话 checkpoint/分叉
- 多 OpenRouter key 轮换与模型 API 熔断器

## 适用场景

- 在 Claude 等 MCP 客户端中发起多智能体深度研究
- 对研究产物建立可 SQL/混合检索的知识库
- 团队以共享服务器模式跑批量研究任务

## 场景标签

`多智能体` `科研工具` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L7: Production MCP server for multi-agent AI research. Plan, parallelize, synthesize.
> L65: |STDIO|(default)|MCP clients (Claude, Jan AI, Continue)|

## 星数曲线

```mermaid
xychart-beta
    title "wheattoast11/openrouter-deep-research-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 53 --> 56
    line [55, 54, 54]
```

2026-10-18 55 → 2026-10-24 54（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a048db98df21` · [字段定义](../../DATASET.md)*
