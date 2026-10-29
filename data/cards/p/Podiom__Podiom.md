# Podiom/Podiom

⭐ 20 · Go · MIT · 推送 2026-10-25 · [GitHub](https://github.com/Podiom/Podiom) · [官网](https://github.com/Podiom/Podiom/tree/master/docs) · 组织维护

**本地优先的 Claude Code/Codex 代理工作区管理工具**

Podiom 是开源的本地优先工作区，用于管理 Claude Code 与 OpenAI Codex CLI 代理：为每个代理提供命名、持久身份与上下文，集中管理会话、项目、路线图任务、定时调度与长期目标（含进度指标与活动时间线）。它不替代提供方运行时，而是调用原生 claude/codex CLI 并复用其模型、MCP、工具与认证。状态存储在本地单一根目录，Web UI 内嵌于 podiomd 守护进程，支持 macOS/Linux/Windows，可作 Home Assistant 插件或容器运行，并提供 iOS/Android 应用。安装含脚本安装器与 Homebrew。

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

- 会话持久化：切换 provider/profile 后可将规范历史重放到新 CLI 会话
- 目标机制：首席代理将结果转为路线图任务并定期回顾，记录进度与证据
- 本地优先：状态存于 PODIOM_HOME 单一根目录，Web UI 内嵌守护进程
- 可作 Home Assistant 插件运行，提供 Capacitor iOS/Android 客户端

## 适用场景

- 同时运行多个 Claude Code/Codex 会话时统一管理项目与任务
- 给代理设定长期目标并追踪进度与工具调用记录
- 在 Home Assistant 或容器中托管代理调度与定时任务

## 场景标签

`编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: Podiom is an open-source, local-first workspace for Claude Code and OpenAI Codex.
> L35: Podiom does not replace the provider runtime. It shells out to the native
> L36: `claude` and `codex` CLIs and uses their models, MCP servers, tools, skills, and

## 星数曲线

```mermaid
xychart-beta
    title "Podiom/Podiom 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-29 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1cc7349ab3cd` · [字段定义](../../DATASET.md)*
