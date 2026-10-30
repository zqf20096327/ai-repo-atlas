# BlockRunAI/blockrun-mcp

⭐ 391 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/BlockRunAI/blockrun-mcp) · [官网](https://www.npmjs.com/package/@blockrun/mcp) · 组织维护

**面向 AI agent 的实时数据与交易 MCP 服务器，按调用付费**

开源 MIT 许可的 Model Context Protocol 服务器，为 Claude 及任意 MCP 兼容 agent 提供 19 个工具：88 种 LLM 调用、图像/视频生成、预测市场数据、实时网页与 X 搜索、40 条链上查询，以及通过 Polymarket CLOB 下达 USDC 结算的真实交易。支付两种模式：自托管钱包（Solana/Base 上的 USDC，经 x402 协议按调用链上结算）或 BlockRun API key（账户额度计费）。支持按阈值的人审支出确认与预算上限环境变量。以 npm 包经 npx 运行，已验证/文档化 Claude Code、Codex CLI、Cursor、VS Code 等客户端接入方式。上下文开销 14.3K tokens（trading profile 下 5.4K）。

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

- 19 个工具覆盖 LLM、图像视频生成、市场数据、X 搜索、40 链上查询与 Polymarket 实盘交易
- x402 微支付：自托管钱包按调用 USDC 结算，无需账户；或 API key 账户额度模式
- 人审支出确认（BLOCKRUN_CONFIRM_SPEND）与预算上限（BLOCKRUN_BUDGET_LIMIT）机制
- 多 MCP 客户端接入验证：Claude Code、Codex CLI、OpenClaw 等已验证，另有多个文档化路径

## 适用场景

- 让 Claude Code 或其他 MCP 客户端查询实时行情、链上数据与 X 舆情
- 通过 agent 在 Polymarket 读取赔率并下达 USDC 结算的真实交易
- 团队用 API key 账户额度统一支付 agent 的数据调用成本

## 场景标签

`金融量化` `视频生成` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L42: > **BlockRun MCP** is an open-source Model Context Protocol server that gives Claude — and any MCP-compatible agent
> L7:  BlockRun MCP gives your agent 19 tools — markets, research, web search, images, video, on-chain data, and live Poly

## 星数曲线

```mermaid
xychart-beta
    title "BlockRunAI/blockrun-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 390 --> 393
    line [391, 392, 391]
```

2026-10-18 391 → 2026-10-30 391（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6b53ba66a22b` · [字段定义](../../DATASET.md)*
