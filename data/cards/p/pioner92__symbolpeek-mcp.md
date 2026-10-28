# pioner92/symbolpeek-mcp

⭐ 21 · Rust · MIT · 推送 2026-07-25 · [GitHub](https://github.com/pioner92/symbolpeek-mcp) · 个人维护

**给 AI 编程 agent 的 MCP 服务器：按符号级别读取代码省 token**

SymbolPeek 是一个 stdio MCP 服务器，为 AI 编程 agent 提供代码库的符号级视图：agent 可请求单个声明（read_symbol）、引用查找（find_references）、调用层级、类型推断、跨文件重命名等约 20 个工具，代替读取整个文件。TS/JS 用官方 TypeScript Compiler API 做语义分析，Rust/Python/Java/Go/JSON/Markdown 用内嵌 Tree-sitter 做语法级操作。提供二进制安装脚本（macOS/Linux/Windows），无需 clone、Rust 工具链或手动构建；TS/JS 分析需 Node.js 20+，其余语言不需要。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TS/JS 语义分析（引用/类型/重命名/诊断），其余语言 Tree-sitter 语法级操作
- 每语言操作能力矩阵可由 get_capabilities 在运行时查询
- 未支持的操作返回显式错误而非空结果，结果附带 analysis 信任元数据
- 可用 sym tools 按需禁用工具以缩减 MCP 启动上下文

## 适用场景

- 让 AI 编程 agent 只读某个符号而非整个大文件以节省 token
- 在真实代码库中做影响分析（找引用、调用者、实现类）
- 跨文件重命名符号并预检命名冲突
- 查看文件符号大纲或按名称和种类搜索声明

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L27: SymbolPeek is an MCP server that gives an AI coding agent a symbol-level view of
> L32: TypeScript and JavaScript are analyzed with the official TypeScript Compiler

## 星数曲线

```mermaid
xychart-beta
    title "pioner92/symbolpeek-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4fad1e974920` · [字段定义](../../DATASET.md)*
