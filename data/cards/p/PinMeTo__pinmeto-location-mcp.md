# PinMeTo/pinmeto-location-mcp

⭐ 15 · TypeScript · MIT · 推送 2026-09-06 · [GitHub](https://github.com/PinMeTo/pinmeto-location-mcp) · [官网](https://www.pinmeto.com) · 组织维护

**把 PinMeTo 门店数据接入 AI 助手的 MCP 服务器**

PinMeTo 官方提供的 MCP 服务器，通过 STDIO 将用户的 PinMeTo 位置数据连接到 Claude Desktop、ChatGPT 桌面版、VS Code、Cursor 等 MCP 兼容客户端。提供 12 个工具，覆盖位置查询、Google/Facebook/Apple 的洞察、评论、评分与关键词数据，支持时间聚合与同比环比对比；可选插件生成 PDF 和 PowerPoint 报告。需 PinMeTo API 凭据，ChatGPT 本地安装需 Node.js v22+；凭据仅在内存中使用，不写入磁盘。

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

- 提供 12 个工具读取 Google/Facebook/Apple 的位置洞察、评论与评分
- 支持按日/月/季度聚合及环比、同比对比
- 可选 PinMeTo Locations 插件生成 PDF/PowerPoint 报告
- 凭据仅在内存中使用，进程退出后不保留数据

## 适用场景

- 用自然语言向 AI 助手查询多门店的评分与评论表现
- 找出待回复的差评并对比各门店表现
- 让 AI 助手生成季度或年度门店分析报告

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: An MCP server that connects your PinMeTo locations to AI assistants. Ask questions about your business in natural la
> L7: Works with MCP-compatible clients that can run local STDIO servers, including Claude Desktop, the ChatGPT desktop ap
> L34: 4. **Done!** This installs the data connection — the MCP server and its twelve tools. Start asking questions about 

## 星数曲线

```mermaid
xychart-beta
    title "PinMeTo/pinmeto-location-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `36cd1963eb98` · [字段定义](../../DATASET.md)*
