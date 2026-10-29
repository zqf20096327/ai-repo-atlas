# evilayman/opencode-raven

⭐ 36 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/evilayman/opencode-raven) · 个人维护

**OpenCode 插件：把搜索与 MCP 检索委托给子代理，返回紧凑结果**

面向 OpenCode V1/V2 的 npm 插件，将搜索、fetch、shell 探索及 MCP 工具调用路由到两个独立可配置模型的 Raven 子代理（raven_seek / raven_mcp），由子代理执行检索后仅向主会话返回紧凑结论，避免原始工具输出占用主模型上下文；支持后台检索、会话 ID 复用追问、按需 MCP（Context7/Exa/Grep.app 预置）与自动免费模型探测，并统计节省的上下文量。配置存于 ~/.config/opencode/ 下 JSON 文件，需重启 OpenCode 生效。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- raven_seek/raven_mcp 两个公开委托工具，自动路由搜索与 MCP 调用
- 按需 MCP：子代理内部发现调用，schema 不进入主模型工具列表
- V2 默认后台检索，经持久化 inbox 送达结果
- 首次启动自动探测零成本可用模型，并跟踪估算节省的上下文

## 适用场景

- 减少 OpenCode 主会话被搜索和工具输出占满
- 让子代理代为调研网络资料并只拿回结论
- 按需加载 MCP 服务而不污染主模型工具列表

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12:  Raven delegates search and on-demand MCP retrieval to separate focused agents, then returns compact evidence to th
> L14:  Routes OpenCode search tools and globally configured MCPs through <code>raven_seek</code>.

## 星数曲线

```mermaid
xychart-beta
    title "evilayman/opencode-raven 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-29 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c23098ad407f` · [字段定义](../../DATASET.md)*
