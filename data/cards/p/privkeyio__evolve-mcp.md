# privkeyio/evolve-mcp

⭐ 13 · Python · MIT · 推送 2026-03-05 · [GitHub](https://github.com/privkeyio/evolve-mcp) · 组织维护

**MCP 服务器：用遗传算法让 AI agent 自我优化提示词**

基于 FastMCP 的 Model Context Protocol 服务器，向 Claude Code、Goose、ChatGPT 等任意 MCP 兼容客户端暴露 21 个工具，用遗传算法对 agent 提示词做变异、交叉与适应度评估，含安全校验（注入检测）、指标采集与异常检测、检查点恢复。设计受 Darwin Gödel Machine 与 AlphaEvolve 启发，本地优先。通过 git clone 源码 + uv sync 安装，MIT 许可，由 PrivKey LLC 维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 21 个 MCP 工具覆盖进化生命周期、变异生成、适应度评估、安全校验与指标采集
- 5 种变异策略（paraphrase/instruction_add/context_expand/cot_injection/tone_shift）
- 可插拔适应度函数与 Pareto 优化、并行评估
- 安全校验含注入检测与策略执行，支持检查点恢复

## 适用场景

- 在 Claude Code 或 Goose 中对 agent 提示词做自动进化优化
- 通过 A/B 测试变体与适应度评分迭代提示词
- 对候选提示词做安全校验后再部署

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L10: evolve-mcp is an MCP (Model Context Protocol) server that enables autonomous self-improvement for AI agents. It wor
> L151: │   ├── server.py        # FastMCP server with 21 tools

## 星数曲线

```mermaid
xychart-beta
    title "privkeyio/evolve-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `419239e2ee0f` · [字段定义](../../DATASET.md)*
