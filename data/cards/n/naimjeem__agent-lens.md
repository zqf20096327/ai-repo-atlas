# naimjeem/agent-lens

⭐ 21 · HTML · 推送 2026-05-13 · [GitHub](https://github.com/naimjeem/agent-lens) · 个人维护

**本地仪表盘：汇总可视化 8 种 AI 编程 agent 的用量与成本**

读取本机 Claude Code、Codex CLI、Gemini CLI、OpenCode、Kimi Code、Cursor、Antigravity、GitHub Copilot 八种 AI 编程 agent 的本地数据文件/SQLite，生成统一 Web 仪表盘：会话数、消息数、token 用量、按日成本估算、缓存命中率、工具调用分析与提示词历史。数据目录按 OS 自动探测且可用环境变量覆盖；成本按可配置的每百万 token 费率计算（可选拉取 OpenRouter 实时价格）。限制：Cursor/Copilot 订阅制默认费率为 0，Copilot 无 token 计数，Antigravity 仅能读会话元数据。通过 npx 直接运行或 git clone + npm install 运行，需 Node.js 18+；macOS 经过实测，Linux/Windows 按约定路径解析。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 8 种 AI 编程 agent 的本地数据并统一可视化
- token/成本/缓存命中率/工具调用/按日活动分析与 HTTP API
- 数据目录自动探测、环境变量覆盖，OpenRouter 实时定价可选
- 纯内联 SVG 图表，OpenCode/Cursor 经可选 better-sqlite3 读 SQLite

## 适用场景

- 我在多个 AI 编程工具间切换，想在一个面板看总花费和 token 用量
- 我想按天核对各 agent 的成本与缓存节省效果
- 我想检索自己发给各 agent 的历史提示词

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Local dashboard for visualizing usage across **eight AI coding agents** — sessions, token costs, cache performance, 
> L11: |Agent|Default data path|Token data|Tool calls|Models|
> L54: The dashboard is plain JSON over HTTP — useful for scripting or integrations.

## 星数曲线

```mermaid
xychart-beta
    title "naimjeem/agent-lens 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1b8f5023a478` · [字段定义](../../DATASET.md)*
