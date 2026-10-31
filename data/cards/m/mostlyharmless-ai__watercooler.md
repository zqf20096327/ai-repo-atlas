# mostlyharmless-ai/watercooler

⭐ 14 · Python · Apache-2.0 · 推送 2026-07-21 · [GitHub](https://github.com/mostlyharmless-ai/watercooler) · [官网](https://github.com/mostlyharmless-ai/watercooler) · 组织维护

**为 AI 协作编程团队保存代码背后决策与理由的 MCP 服务器**

Watercooler 是一个 git-backed 的 MCP 服务器，为使用 AI agent 的编程团队提供存放代码背后推理过程的场所：提案、权衡、批评、理由与决策以结构化线程（say/ack/handoff/set_status、ball 机制、六种角色）写入团队自己的 git 仓库，随代码版本化并可检索。Agent 起草内容，人做最终决策（human-gated），每条记录携带作者、角色与关联 commit。核心开源（Apache-2.0），本地运行，通过 uvx 接入 Claude Code/Codex/Cursor 等 MCP 客户端；另有托管版提供记忆图谱与仪表盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- git-backed 线程记录决策/批评/理由，随代码版本化
- 结构化写操作（say/ack/handoff/set_status）与 ball 问责机制
- 支持关键词与语义搜索及跨仓库联邦搜索
- 通过 uvx 按需运行 MCP 服务器，支持 Claude Code/Codex/Cursor

## 适用场景

- 多 agent/多人协作编程时留存设计决策与权衡过程
- 团队间异步交接工作并通过搜索回溯历史决策
- 让 agent 起草提案、人审批后形成可追溯的决策记录

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L15: Watercooler is an MCP server that gives agentic coding teams a git-backed place for the reasoning behind the code —
> L140: claude mcp add --transport stdio --scope user watercooler -- uvx --from 'git+https://github.com/mostlyharmless-ai/

## 星数曲线

```mermaid
xychart-beta
    title "mostlyharmless-ai/watercooler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `0042d5139272` · [字段定义](../../DATASET.md)*
