# madguyevans-creator/resale-agent-skill-hub

⭐ 95 · Python · MIT · 推送 2026-09-12 · [GitHub](https://github.com/madguyevans-creator/resale-agent-skill-hub) · 个人维护 · 中文 README

**二手转卖智能 Agent：8 个 Claude 技能 + MCP 服务器**

面向 C2C 二手交易的多平台转卖工具包：提供 8 个 Claude Code 技能与一个基于 JSON-RPC over stdio 的 MCP 服务器，可被 Claude Desktop、Cursor、VS Code 等 MCP 客户端调用。核心流程为照片识别商品（Anthropic Claude Vision）、浏览器登录绑定平台会话、比价定价、设定底价防护、自动发布/改价/下架，并以仅追加的 JSONL 透明日志记录每个 AI 决策。默认 mock 模式可无账号、无 API key 演示；真实模式需 ANTHROPIC_API_KEY 与平台账号绑定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 步流水线：照片识别→登录→比价→底价→发布→改价→跨平台下架
- 标准 MCP 服务器，Claude Desktop/Cursor/VS Code 等客户端可调用
- 价格防护拦截器与仅追加的决策审计日志（~/.broker/audit.jsonl）
- 默认 mock 模式：无 API key、无平台账号即可运行全流程演示

## 适用场景

- 拍照后让 Agent 自动识别商品、调研成交价并给出定价建议
- 一键在多平台发布二手商品，售出后自动下架其余平台
- 设定底价防止自动改价跌破预期

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: A collection of 8 Claude Code skills + an **MCP Server** implementing a **Multi-Platform Smart Resale Agent**: an AI
> L31: `broker-recognize` uses the **Anthropic API** (Claude Vision) to analyze product photos. Set your API key:
> L74: Open Claude Desktop, say "帮我卖掉这双鞋" + upload photo. Claude automatically calls 7 MCP tools in the correct order.

## 星数曲线

```mermaid
xychart-beta
    title "madguyevans-creator/resale-agent-skill-hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-25 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `db17094c120d` · [字段定义](../../DATASET.md)*
