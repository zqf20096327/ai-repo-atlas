# thomaschill/unclog

⭐ 36 · Python · MIT · 推送 2026-04-25 · [GitHub](https://github.com/thomaschill/unclog) · [官网](https://pypi.org/project/unclog/) · 个人维护

**扫描并清理 Claude Code 上下文占用项的本地 CLI 审计工具**

面向 Claude Code 用户的本地命令行工具：扫描 ~/.claude/ 下的 agents、skills、slash commands 及 ~/.claude.json 中声明的 MCP server，显示各项 token 成本与 30 天调用计数（零调用标记 [unused]），并计算发送消息前加载的 baseline 总 token；随后通过交互式勾选界面批量删除选中项。调用计数来自遍历 ~/.claude/projects/ 下会话 JSONL 的 tool_use 块。全程无遥测、无账号、无网络调用。需 Python 3.11+ 与 Claude Code ≥ 2.1.90，支持 macOS/Linux；因新版会话日志不再记录工具 schema，无法给出各 MCP server 的精确 token 数。删除操作不可撤销且不保留快照。

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

- 列出 agents/skills/commands/MCP servers 的 token 成本与 30 天调用计数
- 交互式分节勾选批量删除，删除后显示节省 token 与新 baseline
- 遍历会话 JSONL 统计每个 MCP server 的 tool_use 调用数
- 纯本地运行：无遥测、无账号、无网络调用

## 适用场景

- 查看我的 Claude Code 里哪些 agents/skills/MCP 在吃上下文
- 找出 30 天没调用过的 MCP server 并清理
- 在安装新插件前了解 baseline token 占用变化

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L6: **Every agent, skill, slash command, and MCP server you've installed occupies your Claude Code context window on eve
> L23: - Every **MCP server** declared in `~/.claude.json` (global and per-project), with its **invocation count over the 

## 星数曲线

```mermaid
xychart-beta
    title "thomaschill/unclog 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-25 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3820acb2fbc0` · [字段定义](../../DATASET.md)*
