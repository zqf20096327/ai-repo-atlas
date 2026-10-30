# manavgup/context-analyzer

⭐ 19 · HTML · MIT · 推送 2026-07-21 · [GitHub](https://github.com/manavgup/context-analyzer) · 个人维护

**面向 Claude Code/Codex 的 token 成本取证与可视化工具**

通过 Claude Code hooks 捕获工具调用、压缩事件与会话生命周期，结合 Codex CLI rollout 日志与已有 transcripts 解析 API 报告的精确 token 用量，存入 SQLite；提供 FastAPI 单会话仪表盘与跨会话分析页（成本/调用 vs 上下文规模、token 组成、消息检查器、预算阈值）。另含 MCP server 与离线的 headroom 压缩上限审计命令。Python 3.11+，uv/pip 安装，hooks 安装可逆、幂等并自动备份设置。

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

- Hooks + SQLite + 仪表盘捕获并可视化每调用/每轮/每会话 token 用量
- API 报告的精确 token 计数（输入/输出/cache_read/cache_creation），非估算
- 跨会话分析：成本/调用 vs 峰值上下文散点、自动生成洞察
- 离线 headroom 压缩上限审计命令，零 API 花费

## 适用场景

- 排查长会话中 Claude Code 调用成本增长的原因
- 查看 token 组成（工具 I/O/对话/系统前缀）定位上下文占用
- 设置预算阈值观察会话何时进入高成本区间

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L84: - **Hooks** into Claude Code via `~/.claude/settings.json` to capture tool calls, compaction events, session lifecy
> L87: - **SQLite persistence** stores session data for fast queries and cross-session analysis
> L88: - **Dashboard** at `/` for single-session visualization: context growth, cache churn, composition, message inspecto

## 星数曲线

```mermaid
xychart-beta
    title "manavgup/context-analyzer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `729ab9642499` · [字段定义](../../DATASET.md)*
