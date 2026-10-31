# colliery-io/muninn

⭐ 14 · Rust · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/colliery-io/muninn) · 组织维护

**面向 AI 编码代理的隐私优先递归上下文网关**

以 Rust 编写的本地守护进程 + Claude Code 插件形态运行的上下文网关：通过 UserPromptSubmit 钩子，由廉价路由模型判断用户提示是否需要代码库探索，再由递归探索模型（RLM）在本地或廉价后端完成探索并将结果注入为 Claude 的上下文，同时以 MCP server 暴露 search_code 与 query_graph 两个工具。默认配置使用 Ollama Cloud 的 gemma4:31b，支持 Groq、本地 Ollama、Anthropic 适配器；分层配置（router/rlm）可分别指定 provider 与模型。状态（图索引、会话、trace）存储于项目内 .muninn/ 目录，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- UserPromptSubmit 钩子预答并注入上下文，失败时静默透传不阻塞用户回合
- MCP server 暴露 search_code 与 query_graph（基于代码图索引）
- router/rlm 分层配置，探索负载卸载到廉价模型，昂贵推理留在 Claude Code 侧
- 已测试后端表：Ollama Cloud 默认可用，Groq 各模型可靠性分级记录

## 适用场景

- 在 Claude Pro/Max 套餐下节省 token，把代码库探索交给廉价模型
- 不把专有代码发给云端时为 AI 编码代理提供本地上下文探索
- 让 Claude Code 通过 MCP 工具按需查询代码结构与调用关系

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L27: Muninn ships as a Claude Code plugin: a UserPromptSubmit hook that
> L29: result, plus an MCP server exposing `search_code` and `query_graph`.

## 星数曲线

```mermaid
xychart-beta
    title "colliery-io/muninn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2acdd76328df` · [字段定义](../../DATASET.md)*
