# Wolfe-Jam/claude-faf-mcp

⭐ 23 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/Wolfe-Jam/claude-faf-mcp) · [官网](https://faf.one) · 个人维护

**为 Claude 维护项目持久上下文的 MCP 服务器（.faf 格式）**

面向 Claude Desktop / Claude Code 用户的 MCP 服务器：以 IANA 注册的 .faf（YAML）格式记录项目的 3W/6W 人类上下文与语言、框架等机器检测结果，提供 Core 14 个 MCP 工具（FAF_TOOLS=all 时 30 个），支持从 .faf 同步生成 CLAUDE.md、MEMORY.md、AGENTS.md、.cursorrules 等文件，并按 always-33 引擎输出确定性的 AI 就绪评分。上下文随仓库提交，团队成员 git clone 后即获得相同上下文；无账号、无遥测，本地运行。检测、评分与写入均来自所依赖的 faf-cli，不执行 PATH 上的命令。需要 Node 22+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Core 14 个 MCP 工具（FAF_TOOLS=all 时 30 个）+ 2 个提示
- project.faf 同步生成 CLAUDE.md / MEMORY.md / AGENTS.md / .cursorrules 等多表面
- always-33 引擎输出确定性 AI 就绪评分（0-100%）
- faf_etch / faf_recall 跨会话记忆（soul.fafm）

## 适用场景

- 让 Claude 每次会话自动读取项目上下文，无需重复解释项目
- 团队共享项目上下文：提交 project.faf，新成员 clone 即就绪
- 评估并逐步补全项目的 AI 就绪评分

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L25: **v0.2-conformant reader** of the FAF Context Ingestion Contract.
> L37: Core 14 MCP tools (30 with `FAF_TOOLS=all`). IANA-registered formats (`application/vnd.faf+yaml` · `application/vnd

## 星数曲线

```mermaid
xychart-beta
    title "Wolfe-Jam/claude-faf-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `3dcc0218b18f` · [字段定义](../../DATASET.md)*
