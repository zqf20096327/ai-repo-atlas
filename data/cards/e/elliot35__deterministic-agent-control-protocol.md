# elliot35/deterministic-agent-control-protocol

⭐ 82 · TypeScript · MIT · 推送 2026-02-12 · [GitHub](https://github.com/elliot35/deterministic-agent-control-protocol) · [官网](https://www.npmjs.com/package/@det-acp/core) · 个人维护

**AI agent 治理网关：策略化管控与审计 agent 的每个动作**

面向 AI agent 的控制平面：agent 的工具调用不直接执行，而是经策略评估、会话级预算、风险操作人工审批与不可篡改审计账本（SHA-256 哈希链）后放行或拒绝。支持 MCP Proxy、Shell Proxy、HTTP API 与 TypeScript SDK 四种接入模式，内置 Coding Agent、DevOps 等 6 套策略；被拒绝的动作可触发策略自演进，生成最小策略修改建议并由用户决策。以 npm 包与 npx CLI 提供，适配 Cursor、Claude Code、Codex 等 MCP 客户端。治理强度分 Soft/Semi-Hard/Hard 三级，Soft 级存在被提示词绕过的可能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个动作经策略评估，输出到 SHA-256 哈希链防篡改审计账本
- MCP Proxy / Shell Proxy / HTTP API / TypeScript SDK 四种接入模式
- 策略自演进：拒绝时生成最小策略修改建议，用户三选一决策
- 内置 6 套生产可用策略（编码、部署、数据分析等）

## 适用场景

- 给我的 Cursor/Claude Code agent 加治理层，阻止读取 .env 等敏感操作
- 为部署类 agent 设定预算与人工审批门禁
- 留存 AI agent 全部动作的防篡改审计记录

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L43: Agents never execute tools directly. Every action flows through the control plane for evaluation, enforcement, and 
> L147: |**MCP Proxy**|Transparent proxy between agent and MCP servers|Cursor, Claude Code, any MCP client|

## 星数曲线

```mermaid
xychart-beta
    title "elliot35/deterministic-agent-control-protocol 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 81 --> 84
    line [83, 82, 82]
```

2026-10-18 83 → 2026-10-28 82（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f2ce0bf3c41a` · [字段定义](../../DATASET.md)*
