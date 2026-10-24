# mrjoshuak/godoc-mcp

⭐ 126 · Go · MIT · 推送 2026-03-06 · [GitHub](https://github.com/mrjoshuak/godoc-mcp) · [官网](https://github.com/mrjoshuak) · 个人维护

**为 AI 编程 agent 提供 Go 文档的 MCP 服务器，降低 token 消耗**

基于 Model Context Protocol 的 Go 文档服务器：通过 `go doc` 按符号、包等粒度返回结构化文档，避免 LLM 读取整个源文件；支持本地路径与 import 路径、自动临时模块上下文、响应缓存与分页。提供 get_doc 与 list_packages 两个工具，支持 stdio/SSE/HTTP 三种传输模式，可配合 Claude Code、Claude Desktop 及 Docker MCP Gateway 使用，离线可访问文档。面向使用 LLM 进行 Go 开发的开发者。

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

- 按符号/包粒度返回结构化 Go 文档，减少 token 用量
- 支持本地路径与 import 路径，自动创建与清理临时模块上下文
- 内置响应缓存与分页结果
- 支持 stdio/SSE/HTTP 三种传输模式

## 适用场景

- AI 编程 agent 在 Go 项目中按需查询包与符号文档
- 探索陌生 Go 项目的包结构与接口
- 查询第三方库类型的文档与用法

## 场景标签

 · 领域:开发者工具/AI agent 基础设施

## 证据(README 行号)

> L9: `godoc-mcp` is a Model Context Protocol (MCP) server that provides efficient access to Go documentation. It helps LL
> L107: - **stdio** (default): Standard input/output, for local MCP clients like Claude Desktop

## 星数曲线

```mermaid
xychart-beta
    title "mrjoshuak/godoc-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 124 --> 126
    line [125, 125]
```

2026-10-18 125 → 2026-10-24 125（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `6c3289db0c5b` · [字段定义](../../DATASET.md)*
