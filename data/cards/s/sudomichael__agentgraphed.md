# sudomichael/agentgraphed

⭐ 47 · TypeScript · MIT · 推送 2026-07-02 · [GitHub](https://github.com/sudomichael/agentgraphed) · [官网](https://github.com/sudomichael/agentgraphed) · 个人维护

**本地 AI 编程会话的搜索与分析仪表盘（Claude Code/Codex）**

读取 Claude Code 与 Codex CLI 在本地写下的 JSONL 会话日志，索引到本地 SQLite（~/.agentgraphed），在 localhost:3737 提供仪表盘：按天浏览会话、一键复制 resume 命令、按项目/提供商/模型检索、用量与成本统计（基于 LiteLLM 2700+ 模型零售价目录）。可选功能（BYO API key）包括 LLM 会话自动分类与标题生成、为新会话生成上下文 primer、Anthropic/OpenAI 配额探测。默认完全本地，排行榜上报为 opt-in。以 npx/npm 安装，依赖 better-sqlite3 原生模块（多数情况下载预编译二进制，否则需 Python3 与 C++ 工具链）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动索引本地 Claude Code 与 Codex 会话日志到 SQLite，每 5 分钟后台重扫
- 会话搜索、项目历史浏览、一键复制 claude --resume 命令
- 按提供商/模型/项目的用量与成本图表（LiteLLM 2700+ 模型价目）
- 可选 BYO key 的 LLM 会话分类与标题生成、配额探测、上下文 primer 生成

## 适用场景

- 找回并恢复以前中断的 AI 编程会话
- 跨项目统计 AI 编程的用量与成本
- 从历史会话生成上下文粘贴到新会话

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L19: AgentGraphed automatically indexes every Claude Code and Codex session on your machine. With it you can:
> L27: Everything stays local. AgentGraphed reads the JSONL logs your CLI tools were already writing (`~/.claude/projects/
> L139: - **Claude Code** — reads `~/.claude/projects/*/*.jsonl`

## 星数曲线

```mermaid
xychart-beta
    title "sudomichael/agentgraphed 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-26 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a93c29d26844` · [字段定义](../../DATASET.md)*
