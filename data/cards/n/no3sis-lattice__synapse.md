# no3sis-lattice/synapse

⭐ 14 · Python · MIT · 推送 2025-11-13 · [GitHub](https://github.com/no3sis-lattice/synapse) · 个人维护

**把 Synapse 知识引擎暴露给 Claude Code 的 MCP 服务器**

基于 FastMCP 的 stdio 传输 MCP 服务器，封装 Synapse Pattern Map 知识引擎（Neo4j + Redis + 向量嵌入），向 Claude Code agent 提供 4 个工具：模式图检索、语言编码规范获取、项目模板获取与系统健康检查。实现上以 subprocess 调用已有 Synapse CLI 工具，每请求约 20ms 额外开销，配合 Redis 缓存（300s TTL）。需先运行 Synapse 知识引擎与 Neo4j/Redis，通过 claude mcp add 或 .mcp.json 注册。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 暴露 search_pattern_map / get_coding_standard / get_project_template / check_system_health 四个 MCP 工具
- FastMCP + stdio 传输，subprocess 包装 Synapse CLI 工具
- 支持 local/user/project 三种 Claude Code 注册作用域
- 提供绕过 MCP 协议的 CLI 测试模式

## 适用场景

- 让 Claude Code agent 在编码时检索团队的模式与最佳实践
- 为 agent 按语言注入编码规范和项目模板
- 监控 Synapse 知识引擎基础设施健康状态

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: **MCP server exposing the Synapse Pattern Map to Claude Code agents**
> L5: No3sis (νόησις - "understanding, knowledge") is a FastMCP-based server that wraps the Synapse System's knowledge eng
> L175: No3sis uses **FastMCP** with **stdio transport**:

## 星数曲线

```mermaid
xychart-beta
    title "no3sis-lattice/synapse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `1b50bc4fd0f5` · [字段定义](../../DATASET.md)*
