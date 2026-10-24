# ozgurcd/gograph

⭐ 230 · Go · MIT · 推送 2026-10-10 · [GitHub](https://github.com/ozgurcd/gograph) · [官网](https://gograph.identuum.ai) · 个人维护

**本地 Go 代码静态分析引擎，为 AI 编码代理提供结构感知**

gograph 在本地对 Go 仓库构建结构图，支持可选的类型检查 CHA/SSA 增强，提供 CLI 与内置 MCP 服务器两种工作流。面向 Go 编码代理与开发者，用于追踪调用者/被调用者与接口实现、变更影响分析、符号搜索与架构约束检查，不依赖嵌入向量或托管代码索引。默认索引本地解析 Go 源码、不执行目标代码；精确模式需类型检查通过，否则按配置回退。会话遥测仅存于本地 .gograph/ 目录。

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

- 本地构建 Go 仓库结构图，可选类型检查 CHA/SSA 精确模式
- 提供 CLI 与 MCP 服务器（stdio），可在 MCP Registry 分发
- 机器可读结构校验（gograph validate --json，SHA-256 指纹绑定）
- 低内存模式（--memory-mode=low --max-memory）与增量重建

## 适用场景

- 让 AI 编码代理在重构前获取调用图与影响分析
- 对 Go 仓库做符号搜索与接口实现追踪
- 在 CI 中用结构校验命令检查符号/调用边存在性

## 场景标签

 · 领域:开发工具/静态分析

## 证据(README 行号)

> L47: `gograph` builds a local structural graph of your Go repository, with optional
> L48: type-checked CHA/SSA enrichment. Its CLI and MCP workflows help coding agents
> L79: Homebrew and `go install` install the normal `gograph` CLI. MCP clients that

## 星数曲线

```mermaid
xychart-beta
    title "ozgurcd/gograph 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 228 --> 231
    line [229, 230, 230]
```

2026-10-18 229 → 2026-10-24 230（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `172d7acf0e4f` · [字段定义](../../DATASET.md)*
