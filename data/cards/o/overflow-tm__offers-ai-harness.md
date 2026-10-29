# overflow-tm/offers-ai-harness

⭐ 18 · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/overflow-tm/offers-ai-harness) · [官网](https://service.offers.jp/worker/ai-harness/) · 组织维护

**让 AI 编码代理直接使用 Offers 转职平台的技能集**

为 Claude Code、Codex CLI 等 AI 编码代理提供的插件/技能集：通过 MCP 服务器（mcp.offers.jp/worker）连接 Offers 转职平台，提供三个技能——按个人资料检索并分析匹配求人、按技能集算出年收相場并建议加薪技能、审阅并（经用户批准后）更新 Offers 个人资料。认证采用 OAuth 2.1 + PKCE，首次使用需浏览器认证；处理年收、职历、住址等个人数据，数据会进入代理的会话上下文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个技能：求人匹配分析、年收相場计算、个人资料审阅与更新
- 通过 MCP 服务器（mcp.offers.jp/worker）与 OAuth 2.1+PKCE 认证接入
- 个人资料更新仅在用户明确批准时执行
- 支持 Claude Code 插件市场、Codex CLI、gh skills 三种安装方式

## 适用场景

- 在 Claude Code 中用自然语言查找匹配自己技能的求人
- 了解自己的技能集在求人市场的年收行情与提升方向
- 让 AI 审阅并代为更新 Offers 个人资料

## 场景标签

 · 领域:职业服务/Agent 工具

## 证据(README 行号)

> L5: このリポジトリは、あなたが普段使っている AI コーディングエージェント（Claude Code, Codex CLI など）から Offers の機能を直接利用するための Skill セットを提供します。
> L74: このプラグインを使用すると、AI エージェントが Offers MCP サーバー（`https://mcp.offers.jp/worker`）と通信し、以下のデータを処理します。ご利用前に必ずご確認ください。

## 星数曲线

```mermaid
xychart-beta
    title "overflow-tm/offers-ai-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7a32afaa6fc5` · [字段定义](../../DATASET.md)*
