# upbit-official/upbit-agent-skills

⭐ 38 · 推送 2026-09-01 · [GitHub](https://github.com/upbit-official/upbit-agent-skills) · 组织维护

**让 AI agent 通过自然语言调用 Upbit 交易所 API 的技能包**

Upbit（Dunamu）官方发布的 AI agent 技能集：通过 npx skills 命令安装到 Claude Code、Cursor、Codex 等编码 agent 中，使 agent 能以自然语言执行 Upbit 功能，如查询行情、查询余额、下单。集成基于 Upbit API 的 CLI（upbit-cli），API 凭证保存于 ~/.upbit/config 或环境变量。面向开发者与希望使用 AI 的交易者。目前为初始发布阶段，暂不接受公开 Issue/PR。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 提供 upbit 技能：通过 CLI 覆盖订单、行情、充提等 REST API 功能
- npx skills 一键安装至 Claude Code/Cursor/Codex 等编码 agent
- API 凭证支持配置文件与环境变量两种方式

## 适用场景

- 在编码 agent 中用自然语言查询 Upbit 行情与余额
- 让 AI agent 按上下文指令执行下单等交易任务
- 交易者借助 AI 搭建交易环境而无需从零写代码

## 场景标签

 · 领域:加密货币交易/开发者工具

## 证据(README 行号)

> L5: AI agent skills built on the Upbit API, for digital asset trading.
> L7: Upbit Skills enables AI agents to perform key Upbit functions through natural language, such as checking market data
> L9: This project is designed not only for professional developers but also for traders who are eager to leverage AI tech

## 星数曲线

```mermaid
xychart-beta
    title "upbit-official/upbit-agent-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-31 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `713ba2e8edab` · [字段定义](../../DATASET.md)*
