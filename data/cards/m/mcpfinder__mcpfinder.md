# mcpfinder/mcpfinder

⭐ 13 · JavaScript · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/mcpfinder/mcpfinder) · [官网](https://mcpfinder.dev) · 组织维护

**帮 AI agent 发现、评估并安装其他 MCP server 的 MCP server**

以 MCP server 形式运行的发现层：聚合 Official MCP Registry 与 Glama 两个来源，提供 search_mcp_servers / get_server_details / get_install_config / browse_categories 四个工具，供 Claude Desktop、Cursor、Claude Code、Cline/Roo Code、Windsurf 等 AI 客户端查找缺失能力、查看信任信号与告警标记，并生成目标客户端的 JSON 配置片段。通过 npx @mcpfinder/server 以 stdio 方式运行；首次启动可从预构建 SQLite 快照引导（gzip/brotli 双压缩、内容寻址校验），快照每日检查更新。Smithery 来源已因 API 停服计划被移除。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合 Official MCP Registry 与 Glama，跨注册表去重合并
- 四工具面：搜索、详情、安装配置生成、分类浏览
- 信任信号与告警标记（stale 项目、缺失仓库 URL、单来源等）
- SQLite 快照引导：内容寻址、gzip/brotli 双压缩、每日增量检查

## 适用场景

- 让 AI 助手在缺能力时自行搜索并安装合适的 MCP server
- 推荐 MCP server 前核验其元数据、所需密钥与告警信息
- 为不同 AI 客户端生成对应的 MCP 配置片段

## 场景标签

 · 领域:AI 基础设施/MCP 生态

## 证据(README 行号)

> L3: > The MCP server that helps AI agents discover, evaluate, and install other MCP servers.
> L5: MCPfinder is an AI-first discovery layer over the Official MCP Registry and Glama. Install it once, and your assista
> L100: |Tool|Purpose|When to call|

## 星数曲线

```mermaid
xychart-beta
    title "mcpfinder/mcpfinder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `eeaf4b0e0e12` · [字段定义](../../DATASET.md)*
