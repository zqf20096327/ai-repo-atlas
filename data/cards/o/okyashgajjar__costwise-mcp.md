# okyashgajjar/costwise-mcp

⭐ 22 · Go · MIT · 推送 2026-08-07 · [GitHub](https://github.com/okyashgajjar/costwise-mcp) · [官网](https://costwise-mcp.vercel.app) · 个人维护

**本地 MCP 服务器：让编程 agent 少读文件、记住事实、缩小上下文**

面向 AI 编程客户端（Claude Code/Cursor/OpenCode 等）的本地 MCP 服务器，用 Go 编写，完全本地运行、无需 API key。核心机制：用 Tree-sitter 将仓库解析为 SQLite 符号索引（11 种语言），导航类问题从索引返回压缩片段而非整文件；提供 remember/recall 持久化事实、stash_context 把大块输出暂存到磁盘换取短句柄，以减少常驻上下文 token 与缓存开销；通过 MCP instructions 字段下发约 275 token 的会话技能。共 10 个 MCP 工具。安装需 Go 1.25+ 与 C 编译器（CGO 必需），脚本从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tree-sitter 解析 11 种语言，符号/引用/调用边存入本地 SQLite 索引
- 10 个 MCP 工具：检索（search_code/find_symbol 等）、索引维护、上下文控制
- stash_context 暂存大块输出，句柄约 20 token，recall 按 token 预算取回切片
- 100% 本地运行，无需 API key

## 适用场景

- 让编程 agent 回答导航问题时不整读文件
- 长会话中持久化决策与事实避免每轮重复
- 把构建日志等大输出移出上下文窗口

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L51: CostWise is a local MCP server that makes coding agents behave more like that experienced engineer. It gives them f
> L79: A small piece of guidance (about 275 tokens) is delivered to every connected editor through the MCP protocol's `ins

## 星数曲线

```mermaid
xychart-beta
    title "okyashgajjar/costwise-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `befd8e32b3f6` · [字段定义](../../DATASET.md)*
