# jspw/Claude-Code-Dashboard

⭐ 18 · TypeScript · AGPL-3.0 · 推送 2026-10-16 · [GitHub](https://github.com/jspw/Claude-Code-Dashboard) · [官网](https://tools.claude.dashboard.heyshifat.com) · 个人维护

**VS Code 扩展：展示 Claude Code 的 token、成本与会话数据**

本地读取 ~/.claude/ 目录下的会话日志，在 VS Code 内展示 Claude Code 的 token 用量、基于静态价格表的本机成本估算、会话历史与使用洞察（热力图、工具分布、活跃时段、热点文件）。支持按项目查看逐轮对话、token 分解与导出 JSON/CSV；可选注入 hooks 实现实时运行指示（自动备份并可随时移除）。无需 API key，无网络请求与遥测。要求 VS Code 1.85+ 且 Claude Code 已安装并使用过至少一次；成本为本地估算，可能与 Anthropic 账单不一致。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取本地 ~/.claude/projects/ 日志统计 token 与估算成本，无需 API key
- Overview/Charts/Insights 三类视图：周报、30 天趋势、热力图、工具分布、热点文件
- 项目级会话历史与逐轮对话、MCP servers 查看，可导出 JSON/CSV
- 可选 live tracking hooks（注入前自动备份，卸载即清理）

## 适用场景

- 查看我在各项目里 Claude Code 的 token 用量与估算花费
- 设置月度 token 或美元预算并在 80%/100% 时收到提醒
- 回顾会话历史与热点文件，了解自己的使用习惯

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: A VS Code extension that shows you what Claude is doing on your machine — token usage, estimated costs, sessions, an
> L55: - Token counts come from local Claude session logs in `~/.claude/projects/`.
> L86: The extension only reads files in `~/.claude/` and your project directories. No network requests. No telemetry. The

## 星数曲线

```mermaid
xychart-beta
    title "jspw/Claude-Code-Dashboard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2e09dac38a06` · [字段定义](../../DATASET.md)*
