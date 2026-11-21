# ccarter01011/traxagent-claude-plugin

⭐ 74 · Python · MIT · 推送 2026-11-20 · [GitHub](https://github.com/ccarter01011/traxagent-claude-plugin) · [官网](https://www.traxagent.io) · 个人维护

**面向团队的 AI 支出审计 MCP 服务器与 Claude Code 插件**

提供只读 MCP 服务器与 Claude Code 插件，从 Anthropic、OpenAI、Gemini 等 API 与各 AI 工具的用量报告中汇总成本数据，按团队与个人归集，并由 AI 评审生成节约建议，每项附带月度金额与具体修改步骤。提供 /spend-audit 本地日志审计命令、演示数据服务器、支出上限预警与模型性价比对比。需要 TraxAgent 账户，MCP 服务器属于付费计划（每月 $100 以下支出免费）。

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

- 只读 MCP 服务器，OAuth 2.1 (PKCE) 登录，可接入 Claude/ChatGPT/Cursor/VS Code 等客户端
- 本地 /spend-audit 命令直接读取 Claude Code 会话日志，无需账户且数据不外发
- 按工作量排序的节约建议清单，可由 Claude 在仓库中执行修改并开 PR
- 支出上限预警（80%/100%）与 AI 工具注册表（密钥、席位、所有者）

## 适用场景

- 按团队/个人查询上月或上周的 AI 支出明细
- 生成跨供应商的 AI 成本削减优先级清单
- 排查某天支出突增的密钥、模型或循环原因
- 审查未使用超 30 天的 API 密钥与无主 AI 工具

## 场景标签

`LLM 可观测性` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L13: TraxAgent pulls them into one place every night, by team and by person. Then an AI review goes through your usage a
> L15: This repo is the Claude Code plugin. The same read-only server, `https://www.traxagent.io/mcp`, also works in Claud


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `9c588c5ab87e` · [字段定义](../../DATASET.md)*
