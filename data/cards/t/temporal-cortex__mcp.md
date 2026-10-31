# temporal-cortex/mcp

⭐ 13 · Dockerfile · MIT · 推送 2026-08-31 · [GitHub](https://github.com/temporal-cortex/mcp) · [官网](https://www.npmjs.com/package/@temporal-cortex/cortex-mcp) · 组织维护

**给 AI 代理的日历调度 MCP 服务器：原子预约与时间推理**

面向 AI 代理的开放调度基础设施：以 MCP/A2A/REST/浏览器四种协议提供 18 个工具，覆盖联系人解析、时区与时间推理、跨日历源（Google Calendar/Outlook/CalDAV）忙闲合并、基于两阶段提交的原子预约与确定性 RRULE 展开；TOON 格式压缩输出 token。本地经 npx 运行，或使用托管 Platform（OAuth 接入、多代理分布式锁防双订）。运行需 Node.js 18+ 或 Docker，以及至少一个日历提供商凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段提交原子预约，多代理竞争同一时段仅一个成功
- 确定性 RRULE 展开（DST、BYSETPOS=-1、EXDATE 含时区、闰年）
- 跨 Google/Outlook/CalDAV 的统一忙闲合并视图
- TOON 输出格式压缩日历数据约 40% token

## 适用场景

- 让 Claude Desktop/Cursor 等 MCP 客户端代我查空闲并预约会议且防重复
- 为自己的 AI 代理产品接入跨日历源调度能力
- 通过 Open Scheduling 公开可被代理查询的可用时间并支持人类网页兜底预约

## 场景标签

 · 领域:AI 代理基础设施/日历调度

## 证据(README 行号)

> L11: Give any AI agent autonomous scheduling capabilities. Temporal Cortex is open scheduling infrastructure that lets a
> L32: Add scheduling to your AI agent or product. 18 tools across 5 layers, 4 protocols (MCP, A2A, REST, Browser), atomic
> L36: - **Framework integrations:** LangGraph, CrewAI, OpenAI Agents SDK

## 星数曲线

```mermaid
xychart-beta
    title "temporal-cortex/mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `57408aad9142` · [字段定义](../../DATASET.md)*
