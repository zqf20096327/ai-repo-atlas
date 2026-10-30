# aaronsb/obsidian-mcp-plugin

⭐ 467 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/aaronsb/obsidian-mcp-plugin) · 个人维护

**运行在 Obsidian 内的 MCP 服务器：让 AI 客户端直接读写笔记库**

以 Obsidian 插件形式运行的 Model Context Protocol 服务器，无需外部 Node 进程，通过 HTTP/HTTPS 传输向 MCP 兼容客户端（Claude Desktop、Claude Code、Cline、Continue.dev 等）暴露 8 类工具：vault 文件操作（13 种动作）、内容编辑、视图、图结构遍历、Dataview 查询、Bases 数据库操作等。支持只读模式、逐操作权限控制与路径允许/屏蔽列表，API key 认证，HTTPS 使用自动生成的自签名证书。安装可经社区插件目录、BRAT 或 .mcpb 拖放完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器即插件，无需外部 Node 进程或桥接插件
- 8 类工具含 vault 文件操作、图遍历（链接/标签/反向链接）与 Dataview/Bases 查询
- 只读模式、逐操作权限控制与路径允许/屏蔽列表
- 提供 HTTP(3001)/HTTPS(3443) 端口与 API key 认证

## 适用场景

- 让 Claude 等 AI 助手检索、汇总和编辑我的 Obsidian 笔记
- 通过图遍历发现笔记间的概念关联
- 在权限受限的只读模式下让 AI 分析知识库

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L11: **Read, write, search, and traverse your Obsidian vault from any AI assistant — through an MCP server that runs _in
> L17: **Works with any MCP-compatible client** — Claude Desktop, Claude Code, Cline, Continue.dev, and anything that spea

## 星数曲线

```mermaid
xychart-beta
    title "aaronsb/obsidian-mcp-plugin 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 465 --> 468
    line [466, 467, 467]
```

2026-10-18 466 → 2026-10-30 467（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `880175cfafb0` · [字段定义](../../DATASET.md)*
