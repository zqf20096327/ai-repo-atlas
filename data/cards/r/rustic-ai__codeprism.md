# rustic-ai/codeprism

⭐ 32 · Rust · NOASSERTION · 推送 2026-02-14 · [GitHub](https://github.com/rustic-ai/codeprism) · [官网](https://rustic-ai.github.io/codeprism/) · 组织维护

**AI 编程助手的 MCP 代码智能服务器，图结构理解代码库**

Rust 实现的 Model Context Protocol（MCP）服务器，向 Claude Desktop、Cursor 等 AI 编程助手提供代码库的图结构化理解：将 JavaScript/TypeScript/Python 解析为通用 AST 图，提供 20 个分析工具（符号搜索、数据流追踪、复杂度与安全分析、批处理编排等）及解析器开发工具（AST 可视化、REPL、性能剖析）。需 Rust 1.82+ 从源码构建。项目自述为实验性的 100% AI 生成项目，由单一 AI 编码代理维护，不接受人工代码贡献，由 Dragonscale Industries 赞助开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- MCP 协议（JSON-RPC 2.0）服务器，提供 20 个代码分析工具
- JS/TS/Python 通用 AST 图表示，毫秒级增量解析与图遍历查询
- 解析器开发工具：AST 可视化、验证、REPL、AST diff 与 GraphViz 导出
- 含 Mandrel（moth）MCP 测试框架，支持 stdio/HTTP/SSE 传输

## 适用场景

- 让 Claude/Cursor 等编程助手基于代码图回答架构与依赖问题
- 通过 MCP 工具做安全漏洞检测、未用代码与重复代码分析
- 观察全 AI 生成的开源软件项目的开发方式

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: A production-ready, high-performance code intelligence server implementing the Model Context Protocol (MCP). CodePri
> L76: │   AI Assistant  │◄──────────────────►│   codeprism-mcp-server │

## 星数曲线

```mermaid
xychart-beta
    title "rustic-ai/codeprism 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `46725599c3c9` · [字段定义](../../DATASET.md)*
