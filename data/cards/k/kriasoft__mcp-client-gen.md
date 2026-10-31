# kriasoft/mcp-client-gen

⭐ 20 · TypeScript · MIT · 推送 2026-10-01 · [GitHub](https://github.com/kriasoft/mcp-client-gen) · [官网](https://medium.com/@koistya/why-i-built-mcp-client-generator-and-why-you-should-care-c860193ca902) · 个人维护

**把远程 MCP 服务器生成为类型安全的 TypeScript SDK**

面向 TypeScript 开发者的代码生成 CLI：给定远程 MCP 服务器 URL（Streamable HTTP 或 SSE），读取其工具的 JSON Schema，生成一个模块，每个工具对应一个类型化方法，prompts 与 resources 以命名空间形式暴露。生成代码仅依赖官方 MCP SDK 类型，不锁定本包。生成过程支持 OAuth 2.1 浏览器授权（凭据仅保存在内存），也可无 URL 时读取 .mcp.json/.cursor/mcp.json 批量生成。需 Node.js 22+ 或 Bun，生成模块需 @modelcontextprotocol/client ^2.2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 由服务器 JSON Schema 生成输入输出类型化的一工具一方法模块
- 生成过程内置 OAuth 2.1 浏览器授权流程
- 支持读取 .mcp.json / .cursor/mcp.json / .vscode/mcp.json 批量生成
- 同服务器重复运行产生相同文件，diff 可显示服务器变更

## 适用场景

- 在 TypeScript 项目中以类型化方法调用 MCP 服务器的工具
- 在测试中用桩对象替身生成的客户端
- 跟踪远程 MCP 服务器工具集合的变化

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L8: Generate a typed TypeScript client for a remote MCP server (Streamable HTTP or SSE): point it at a URL, get a module
> L15: - **Thin** — each method calls the official MCP SDK and returns its result unchanged

## 星数曲线

```mermaid
xychart-beta
    title "kriasoft/mcp-client-gen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e3eded56d315` · [字段定义](../../DATASET.md)*
