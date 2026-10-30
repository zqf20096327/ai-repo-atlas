# SynapticHQ/Synapse

⭐ 22 · TypeScript · MIT · 推送 2026-06-22 · [GitHub](https://github.com/SynapticHQ/Synapse) · 组织维护

**面向 Solana DeFi 的多 agent MCP 编排器，输出行动方案**

基于 Bun 1.2 与 Claude Agent SDK 的多 agent 编排系统：接收任务后由 Claude 驱动的 router 选择最小所需 agent 集合，依次运行 defi-agent（链上数据）、market-agent（市场分析）与 executor（综合排序），返回带置信度的行动方案。router 使用 tool_choice: any 强制派发决策，含置信度门控、上下文截断（4,000 字符）、agent 超时与 token 预算统计；运行时在 localhost:3000 提供实时仪表盘。需配置 ANTHROPIC_API_KEY 与 HELIUS_API_KEY。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude router 用 tool_choice: any 强制派发，按任务选取最小 agent 集合
- defi/market/executor 三类专职 agent，executor 输出带置信度的排序行动方案
- 置信度门控、4,000 字符上下文截断、agent 超时与 token 预算追踪
- localhost:3000 实时仪表盘展示调用、耗时与 token 用量

## 适用场景

- 我想把一条 DeFi 问题自动分派给专职 agent 并拿到综合行动方案
- 追踪每个编排周期的 agent 调用与 API 花费
- 在 agents/ 目录扩展自己的专职 agent 参与路由派发

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L8: A multi-agent MCP orchestrator for Solana DeFi. Send a task — Synapse routes it to the right combination of speciali
> L28: - **defi-agent** — on-chain data specialist. Fetches pool states, scores volume authenticity, pulls token prices. R
> L30: - **executor** — synthesizer. Receives the other agents' output as context and returns a ranked action plan with co
> L134: - **Agents**: Claude Agent SDK — individual `stop_reason === "tool_use"` loops per agent

## 星数曲线

```mermaid
xychart-beta
    title "SynapticHQ/Synapse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a26a08fd7a89` · [字段定义](../../DATASET.md)*
