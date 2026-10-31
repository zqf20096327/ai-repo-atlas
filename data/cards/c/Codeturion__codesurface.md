# Codeturion/codesurface

⭐ 21 · Python · MIT · 推送 2026-07-28 · [GitHub](https://github.com/Codeturion/codesurface) · [官网](https://www.fuatcankoseoglu.com/) · 个人维护

**为 AI agent 提供代码库公共 API 索引查询的 MCP 服务器**

Python 实现的 MCP 服务器，启动时解析代码库源文件，提取公共类/方法/属性/字段/事件并建立内存索引，通过 search、get_signature、get_class、get_stats、reindex 共 5 个 MCP 工具供 AI agent 查询。支持 C#、C++ 头文件、Go、Java、Python、TypeScript/JavaScript，语言自动检测；每条记录含行号区间，支持按 offset/limit 定向读取以减少 token 消耗。索引基于 mtime 增量更新，查询未命中时自动刷新。通过 uvx 或 pip 安装，配置到 .mcp.json 后在 Claude Code、Cursor、Windsurf 等 MCP 兼容工具中使用；需 Python 3.10+。

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

- 启动时解析 6 类语言的公共 API 并建立内存索引，通过 5 个 MCP 工具供 agent 查询
- 每条记录含 line_start/line_end，支持定向读取替代整文件读取
- mtime 增量 reindex，查询未命中时自动刷新索引
- 支持 .codesurfaceignore 与 --exclude 过滤索引路径，可多实例索引多个项目

## 适用场景

- 让 Claude Code/Cursor 等 AI 编程工具查询代码库 API 而非读取整个源文件
- 跨 Unity、Spring Boot、.NET 等多类型项目做代码 API 检索
- 降低 agent 代码调研任务的 token 消耗

## 场景标签

 · 领域:开发者工具/代码智能

## 证据(README 行号)

> L13: **MCP server that indexes your codebase's public API at startup and serves it via compact tool responses, saving to
> L15: Parses source files, extracts public classes/methods/properties/fields/events, and serves them through 5 MCP tools.

## 星数曲线

```mermaid
xychart-beta
    title "Codeturion/codesurface 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2af64a384888` · [字段定义](../../DATASET.md)*
