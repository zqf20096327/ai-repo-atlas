# XBP-Europe/sagemath-mcp

⭐ 18 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/XBP-Europe/sagemath-mcp) · [官网](https://pypi.org/project/sagemath-mcp/) · 组织维护

**给 LLM 提供沙箱化 SageMath 数学能力的 MCP 服务器**

基于 FastMCP 的 Model Context Protocol 服务器，向 MCP 客户端（Claude Desktop、Claude Code、Gemini CLI、Codex CLI、VS Code、Cursor 等）暴露 40 个 SageMath 工具，覆盖符号微积分、线性代数、数论、图论、椭圆曲线与绘图等。每个 MCP 会话获得独立 Sage worker 子进程，变量与假设跨工具调用持久化；verify_claim 工具经证明阶梯复核声明。调用代码采用 deny-by-default 的 AST 策略（接纳 SageMath 自身 doctest 语料的 98.9%），容器为实际安全边界。安装途径含 pip（含 passagemath 运行时，约 1 GB，需 Python 3.12）、Docker 镜像、conda-forge 与桌面 MCP 一键包；原生 Windows 支持不完整。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40 个 MCP 工具覆盖微积分、代数、数论、图论、绘图等
- 每会话独立 Sage worker 子进程，变量与假设跨调用持久化
- deny-by-default AST 策略，策略经 SageMath 438,124 条 doctest 语料度量
- verify_claim 按证明阶梯输出 proved/refuted/supported/undecided

## 适用场景

- 让 Claude/Gemini CLI 等 MCP 客户端执行并核验符号数学计算
- 跨多次调用的多步数学推导工作流（持久会话）
- 多租户或不可信输入场景下用加固容器隔离运行数学计算

## 场景标签

 · 领域:LLM 工具/计算机代数

## 证据(README 行号)

> L31: A Model Context Protocol server that gives an
> L36: calls**. It ships **40 MCP tools**, one of which — `verify_claim` — re-checks a
> L258: │  MCP Client (Claude Desktop, Gemini CLI, Codex CLI, ...)    │

## 星数曲线

```mermaid
xychart-beta
    title "XBP-Europe/sagemath-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `9a9d4a90799c` · [字段定义](../../DATASET.md)*
