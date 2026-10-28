# sammcj/mcp-devtools

⭐ 161 · Go · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/sammcj/mcp-devtools) · [官网](https://smcleod.net) · 个人维护

**面向 AI 编程 agent 的 Go 单二进制 MCP 服务器，聚合常用开发工具**

用 Go 编写的单一 MCP 服务器，以统一模块化接口向 AI 编程 agent 提供 20+ 开发工具：联网搜索、网页抓取、库文档查询（Context7）、包版本查询、结构化推理、GitHub 操作、代码语义搜索、PDF/Excel/文档处理、文件系统操作、MCP 代理等；默认工具开箱即用，附加工具经 ENABLE_ADDITIONAL_TOOLS 按需启用，并可把 Claude Code/Codex/Copilot/Gemini/Kiro CLI agent 挂载为工具。支持 STDIO 与无状态 HTTP 两种传输，提供 go install、安装脚本、源码编译与预编译二进制四种安装方式。部分工具（如 API to MCP）标注实验性或处于弃用评审中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 Go 二进制替代多个 Node.js/Python MCP 服务器，20+ 工具统一接口
- 默认工具零依赖开箱即用，附加工具按环境变量模块化启用
- 支持 STDIO 与无状态 Streamable HTTP（MCP 2026-07-28）两种传输
- 可将 Claude Code / Codex / Copilot / Gemini / Kiro CLI agent 集成为工具

## 适用场景

- 为 Claude Code、Cline、LM Studio 等 MCP 客户端一站式配置开发工具
- 生产部署中通过 HTTP 传输共享 MCP 工具服务，支持负载均衡与滚动重启
- 让编程 agent 联网搜索、查库文档、处理 PDF/Excel 与操作代码库

## 场景标签

`网页抓取` `语义搜索` · 领域:效率与自动化

## 证据(README 行号)

> L3: A single, high-performance MCP server that replaces many Node.js and Python-based MCP servers with one efficient Go 
> L27: - Replace multiple potentially resource-heavy Node.js/Python MCP servers, each spawned for every client tool you us
> L216: **Agents as Tools** - In addition to the above tools, MCP DevTools can provide access to AI agents as tools by int

## 星数曲线

```mermaid
xychart-beta
    title "sammcj/mcp-devtools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 160 --> 162
    line [161, 161]
```

2026-10-18 161 → 2026-10-28 161（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `93f3753a9b00` · [字段定义](../../DATASET.md)*
