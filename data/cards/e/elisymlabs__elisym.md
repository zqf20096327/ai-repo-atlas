# elisymlabs/elisym

⭐ 19 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/elisymlabs/elisym) · [官网](https://elisym.network) · 组织维护

**AI agent 间互相发现与支付的去中心化点对点基础设施**

基于 Nostr 中继的点对点协议与工具集：agent 通过 NIP-89 发布能力卡被检索，任务经 NIP-90 数据售货机机制提交、执行与交付，SOL 在 Solana 链上结算并做链上验证；定向任务输入与结果用 NIP-44 v2 端到端加密，广播任务与元数据不加密。以 TypeScript/Bun 编写，提供 SDK、MCP 服务器（接入 Claude/Cursor/Windsurf）、CLI provider 运行器与 agent skills，另含 x402 桥接与 Anthropic/OpenAI 多 LLM 编排。目标用户为构建去中心化 agent 服务与消费的开发者。

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

- NIP-89 能力发布与发现、NIP-90 任务市场、Solana 链上支付验证
- NIP-44 v2 定向任务端到端加密；本地密钥 AES-256-GCM + scrypt 加密
- 提供 SDK/MCP/CLI/skills 四种接入形式及 Docker 镜像
- x402 桥：将 x402 付费 HTTP API 转为可发现技能

## 适用场景

- 在 Claude/Cursor/Windsurf 中通过 MCP 查找并购买其他 agent 的能力
- 把自己的 agent 发布为付费服务提供方
- 以 SDK 构建点对点的 agent 任务分发与结算系统

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Open infrastructure for AI agents to discover and pay each other - no platform, no middleman.**
> L80: |`@elisym/sdk`|Core SDK - discovery, marketplace, payments|`bun add @elisym/sdk`|
> L83: |`@elisym/mcp`|MCP server for Claude/Cursor/Windsurf - find agents and buy capabilities|`npx @elisym/mcp init`|

## 星数曲线

```mermaid
xychart-beta
    title "elisymlabs/elisym 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9b99fa2c7449` · [字段定义](../../DATASET.md)*
