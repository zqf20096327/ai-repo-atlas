# eresende/pitlane-mcp

⭐ 76 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/eresende/pitlane-mcp) · 个人维护

**面向 AI 编程代理的代码索引与符号级检索 MCP 服务器**

用 tree-sitter 对代码库建立一次 AST 索引，之后通过 MCP 工具让编程代理按符号粒度检索和读取代码，替代整文件灌入上下文；支持 19 种语言的符号索引、BM25 符号搜索与可选语义搜索，并提供路径追踪、影响分析、Git diff 分析及 Markdown/JSON/YAML/TOML 文档检索。完全本地运行，无需外部服务。除 MCP 外还提供功能等价的 pitlane CLI。项目自述为功能完备、处于维护模式，不再规划新的大特性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- tree-sitter AST 索引，覆盖 Rust/Python/JS/TS/Go 等 19 种语言
- BM25 符号搜索与可选语义搜索，增量重建索引并持久化到磁盘
- investigate/trace_path/analyze_impact 等组合导航工具
- 完全本地运行，无必需外部服务；另提供同功能 CLI

## 适用场景

- 给 AI 编程代理配置更小的代码导航面，减少 token 消耗
- 在编辑或重构前做变更影响分析
- 跨子系统追踪执行路径与配置生效链路
- 检索项目内 Markdown 文档与文档段落

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L7: Token-efficient code intelligence MCP server for AI coding agents.
> L9: `pitlane-mcp` indexes a codebase once with tree-sitter and lets agents retrieve the symbols they actually need inste

## 星数曲线

```mermaid
xychart-beta
    title "eresende/pitlane-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-30 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b07dd71d07c4` · [字段定义](../../DATASET.md)*
