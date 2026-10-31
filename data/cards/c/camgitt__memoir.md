# camgitt/memoir

⭐ 15 · JavaScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/camgitt/memoir) · [官网](https://memoir.sh) · 个人维护

**给编码 Agent 的跨工具持久记忆与项目交接工具**

以本地可读文件保存决策、理由、目标与下一步行动，通过 MCP server 让 Claude Code、Codex、Cursor 等编码 agent 保存和检索上下文，并支持本地、Git 与云端加密备份在多机间同步。提供项目级 handoff（memoir work setup/resume）、浏览器项目视图、自动恢复快照与 SessionStart hook 会话简报。搜索为本地词法检索而非语义检索；本机源文件为明文，仅备份加密；MCP 记忆连接不可执行命令。以 npm CLI 形式安装，需 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP server 提供 memoir_note/remember/recall/resume/forget 等记忆工具
- 支持 Claude Code、Codex、Cursor 的项目 MCP 配置与通用 MCP 客户端
- 本地/Git/云端备份含端侧加密，云端迁移逐文件校验替换
- 项目 handoff 携带已回答问题、决策、下一步行动与检查回执

## 适用场景

- 在 Cursor 和 Codex 等不同编码工具间延续同一项目的上下文
- 跨机器同步编码 agent 的决策记录与会话状态
- 通过浏览器项目视图检索、修正与移除已保存的决策

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Portable, project-scoped memory and session handoffs for coding agents.
> L5: Memoir keeps decisions, rationale, goals, and next actions in readable local files. An MCP server lets an agent save
> L140: |Surface|Capability|Verification boundary|

## 星数曲线

```mermaid
xychart-beta
    title "camgitt/memoir 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ea7aa66091c5` · [字段定义](../../DATASET.md)*
