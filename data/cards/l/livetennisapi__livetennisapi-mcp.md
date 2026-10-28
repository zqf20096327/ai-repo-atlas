# livetennisapi/livetennisapi-mcp

⭐ 148 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/livetennisapi/livetennisapi-mcp) · [官网](https://docs.livetennisapi.com) · 组织维护

**给 LLM agent 提供实时网球比分与数据的 MCP 服务器**

Live Tennis API 的官方 MCP server，向 Claude、Cursor、Zed、Codex 等 MCP 客户端暴露 20 余个只读工具：实时比分、球员资料、赛程、排名、历史结果档案（1968–2022）、赔率与模型胜率分析。数据端点按 FREE/BASIC/PRO/ULTRA 四档付费计划分级，需 API key（免费档无需信用卡）。提供 stdio（npx 按需拉取）与托管 Streamable-HTTP 两种接入方式；stdio 模式下 key 不离开本机。要求 Node 20+。工具遇付费墙时返回英文说明而非裸错误，方便模型向用户解释升级需求。

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

- 20+ 只读 MCP 工具覆盖实时比分、档案、赔率与模型胜率
- stdio 本地运行与多租户托管 HTTP 端点两种接入方式
- 付费墙返回普通结果形式的英文说明而非 403 错误
- 附赠 Polymarket/Kalshi 网球交易数据 Agent Skill（仅观察，无下单）

## 适用场景

- 在 Claude/Cursor 中直接查询正在进行的网球比分与赛程
- 为网球内容或数据分析构建 agent 的实时数据源
- 查询跨时代球员交锋与历史档案数据

## 场景标签

 · 领域:体育数据/LLM 工具服务

## 证据(README 行号)

> L5: **MCP server for the Live Tennis API.**
> L7: Give Claude, Cursor, Zed or any MCP client live tennis scores, players and
> L233: - Requires Node 20+.

## 星数曲线

```mermaid
xychart-beta
    title "livetennisapi/livetennisapi-mcp 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-28"]
    y-axis "stars" 146 --> 148
    line [147, 147]
```

2026-10-26 147 → 2026-10-28 147（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `02e6b9bee9a0` · [字段定义](../../DATASET.md)*
