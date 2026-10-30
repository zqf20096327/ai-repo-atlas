# FutureisinPast/mcp-agent-switchboard

⭐ 18 · Python · NOASSERTION · 推送 2026-10-06 · [GitHub](https://github.com/FutureisinPast/mcp-agent-switchboard) · 个人维护

**本地 MCP 桥接层：让 Claude Code/Codex/Gemini/Antigravity 互传任务**

单文件 Python MCP broker，运行于本地 stdio JSON-RPC，用 SQLite（~/.agent-broker）保存共享状态，使 Claude Code、Codex、Gemini/Antigravity、VS Code 之间互相派发任务、跨模型多轮辩论并合成裁决、共享压缩后的项目上下文快照。复用已有订阅的 CLI 与 IDE 桥接路由，无需 API key 或云端中转。安装支持 Windows 单文件 exe（内嵌 VSIX 桥接扩展）或 Python 3.10+ 源码脚本；明确声明仅 Antigravity 具备完整应用内往返，Claude/Codex 走 CLI 往返或收件箱文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨模型多轮辩论并合成裁决（agent-switchboard debate）
- token 压缩交接、压缩上下文包与按主题工作记忆
- doctor 命令报告每条路由在本机的完整/部分/仅应用内状态
- 无依赖单 Python 文件 broker + Windows 自包含 exe 安装

## 适用场景

- 让 Codex 请 Claude 审计代码，或反向求助
- 用已有的订阅让多个 AI 编码助手互相评审与辩论
- 在不复制粘贴上下文的情况下跨助手共享项目状态

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Agent Switchboard is a **local MCP bridge** that lets your AI coding agents hand tasks to each other, review each ot
> L7: **No API keys. No cloud broker. No extra billing.** It uses the local CLIs, IDE bridge routes, and subscriptions you

## 星数曲线

```mermaid
xychart-beta
    title "FutureisinPast/mcp-agent-switchboard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `4bbfe870cb65` · [字段定义](../../DATASET.md)*
