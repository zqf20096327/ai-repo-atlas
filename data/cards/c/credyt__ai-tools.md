# credyt/ai-tools

⭐ 52 · Python · 推送 2026-05-13 · [GitHub](https://github.com/credyt/ai-tools) · [官网](https://credyt.ai/for/vibe-coders) · 组织维护

**给开发者用的 Credyt AI 计费集成技能与 MCP 接入包**

Credyt（面向 AI 产品的实时用量计费基础设施）官方提供的 agent 技能仓库：通过 skills.sh 或 Claude Code 插件安装 4 个技能，覆盖定价策略引导、计费配置、端到端计费验证与应用代码集成；需先连接 Credyt MCP 服务器（API key 鉴权），支持 Claude Code、Cursor、Codex、Gemini、Copilot 等 agent。Claude Desktop 可直连 MCP 服务器对话式管理，但技能文件需手动上传。

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

- 4 个技能：pricing-strategy / billing-setup / billing-verification / billing-integration
- npx skills add 一条命令安装，兼容任何支持 MCP 的 agent
- Claude Code 插件将技能暴露为斜杠命令，上架 Anthropic marketplace
- 端到端计费验证：创建测试客户、充值、发送用量事件并核对扣费

## 适用场景

- 在 Claude Code / Cursor 等 agent 中直接配置 Credyt 计费
- 用对话引导完成定价策略与产品计费设置
- 变更后跑端到端计费验证排查问题

## 场景标签

 · 领域:开发者工具/计费基础设施

## 证据(README 行号)

> L3: Set up and integrate Credyt — real-time monetization infrastructure for AI products — directly from your AI agent. F
> L42: - **skills.sh** (`npx skills add credyt/ai-tools`) — works with any AI agent that supports MCP.

## 星数曲线

```mermaid
xychart-beta
    title "credyt/ai-tools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-31 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9844ef10e6f3` · [字段定义](../../DATASET.md)*
