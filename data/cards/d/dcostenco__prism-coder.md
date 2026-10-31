# dcostenco/prism-coder

⭐ 156 · TypeScript · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/dcostenco/prism-coder) · [官网](https://synalux.ai/prism-mcp) · 个人维护

**给 AI 编程 agent 提供本地优先的持久会话记忆 MCP 服务器**

一个 MCP 服务器，为 Claude Code、Cursor、Codex 等 AI 编程工具提供跨会话的长期记忆：会话交接笔记、待办、知识图谱与基于 ACT-R 的联想召回。捆绑开放权重模型（2B–27B），将有界任务经本地 Ollama 路由，并提供 `prism savings` 统计本地服务节省的 token 量。无账号与 API key 即可本地运行；另有 Synalux 付费订阅提供云同步、高阶模型与团队功能。通过 npm 或 Claude Code/Codex 插件市场安装，`prism connect` 一键配置各宿主。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨会话持久记忆：交接笔记、待办、知识图谱、ACT-R 联想召回
- 本地优先推理：基于安装模型/RAM/上下文自动选择 2B–27B 模型
- 可审计的 token 节省统计（prism savings，报告假设与已知低估）
- `prism connect` 一次配置 Claude Code、Cursor、Gemini CLI、Codex 等宿主

## 适用场景

- 让 Claude Code / Cursor / Codex 在重启后记住项目上下文并恢复会话
- 把有界推理任务路由到本地模型，减少云模型 token 消耗
- 查看本地服务实际节省的 token 报告

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L12: Prism Coder is an MCP server that gives Claude, Cursor, and other AI tools long-term memory that survives across se
> L36: - **One setup for every agent** — `prism connect` configures Claude Code,
> L37:  Claude Desktop, Cursor, Gemini CLI, and Codex while preserving unrelated

## 星数曲线

```mermaid
xychart-beta
    title "dcostenco/prism-coder 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 155 --> 158
    line [157, 156, 156]
```

2026-10-18 157 → 2026-10-31 156（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `307a376e05fa` · [字段定义](../../DATASET.md)*
