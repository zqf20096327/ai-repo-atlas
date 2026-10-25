# griffinwork40/agent-afk

⭐ 61 · TypeScript · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/griffinwork40/agent-afk) · [官网](https://agentafk.com) · 个人维护

**可离席的自主编码 agent：跑长任务、自验证、完成后通知**

Apache-2.0 的开源编码 agent harness，npm 全局安装本地运行，支持包括本地模型在内的任意 provider（默认 Anthropic，local 槽位可指向 Ollama/LM Studio/OpenAI 兼容 shim）。提供四种界面共享同一会话管理：一次性 chat、REPL、headless daemon（可配 Telegram 通知）与 Telegram bot。每次运行写入 append-only trace 供审计；内置 /mint、/diagnose 等编排器分发 subagent 波次；本地双层记忆（HOT.md + SQLite FTS5 档案）；afk whatif 可在沙箱中预测配置变更对 agent 行为的影响。可从 Claude Code/Codex 导入凭证、插件与 MCP 配置。限制：需 Node 22/24/26 指定版本，pnpm 10+ 需额外批准构建脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种界面（chat/REPL/daemon/Telegram）共享同一会话管理与本地记忆
- append-only trace：工具调用、gate 决策、subagent 生命周期与成本可审计回放
- afk whatif 行为影响预测：沙箱内实测 prompt/模型/技能变更的行为偏移
- 模型槽位机制：local 槽可绑定 Ollama/LM Studio 等本地模型

## 适用场景

- 把长耗时编码任务交给 daemon，完成后通过 Telegram 收到通知再回来审 trace
- 在终端 REPL 里带全套工具（Bash/文件/web fetch/subagent）做日常开发对话
- 用 whatif 预先验证 prompt 或记忆规则修改对 agent 行为的影响
- 从 Claude Code/Codex 迁移凭证、插件与 MCP 服务器

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Start a task and walk away.** AFK builds the feature, verifies its own work, and texts you when it's done. You com
> L47: - **Built-in orchestrators** — `/mint`, `/diagnose`, `/spec`, `/research`, `/ship`, `/review` dispatch subagent wav
> L74: The model isn't the product -- the loop is. Agent AFK hands you the loop as code: prompts, gates, routing, skills, 

## 星数曲线

```mermaid
xychart-beta
    title "griffinwork40/agent-afk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-25 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `29a3c010f16c` · [字段定义](../../DATASET.md)*
