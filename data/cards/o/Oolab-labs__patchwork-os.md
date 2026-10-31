# Oolab-labs/patchwork-os

⭐ 31 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Oolab-labs/patchwork-os) · [官网](https://patchworkos.com) · 组织维护

**本地优先的个人 AI 决策层：审批高风险 agent 动作并留痕**

运行在终端与编辑器之间的自动化运行时与决策层：YAML recipe 由触发器（cron/webhook/git 等）驱动 agent 跨 GitHub、Slack、Gmail 等 45+ 服务执行任务。核心机制是审批闸门：按爆炸半径对动作分级，高风险动作进入审批队列等待人工确认；worker（具名 agent）从受监督起步、按行动类型逐步赢得自主权；每个决策留下可回放的记录。运行时、凭据、日志全部存于本机 ~/.patchwork。另含 180 个 MCP 工具的 IDE bridge，支持 VS Code 系扩展与 JetBrains 插件。新装默认 governed 档位开启闸门，旧配置保持 compat 档不拦截。需要 Node 22.5+ 与终端环境，模型驱动依赖 Claude CLI 或 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按爆炸半径分级的审批队列，高风险动作暂停等待人工确认
- worker 从受监督起步、按行动类型的信任递升机制，可被一键降级
- 每个决策留下持久、可回放、可解释的记录（judgments/traces）
- 180 个 MCP 工具的 IDE bridge，支持 VS Code/Cursor/Windsurf/JetBrains

## 适用场景

- 让 agent 自动化真实工作（收件箱、repo、生产服务）同时拦截高风险操作
- 追踪 agent 被允许做了什么、为什么以及结果如何
- 作为 Claude Code 等编码 agent 的 IDE 工具桥接层使用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: Every AI-agent horror story ends the same way: an action nobody stopped to question. Patchwork OS is the layer betw
> L118: **As an automation runtime** — recipes, workers, connectors, the decision layer. Needs `~/.patchwork` and a model 
> L128: **As a standalone IDE bridge** — 180 MCP tools giving Claude Code eyes and hands in your editor: diagnostics, LSP 

## 星数曲线

```mermaid
xychart-beta
    title "Oolab-labs/patchwork-os 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2dbd9ca96756` · [字段定义](../../DATASET.md)*
