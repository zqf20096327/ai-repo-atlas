# 6missedcalls/personal-finance-skill

⭐ 28 · TypeScript · MIT · 推送 2026-02-27 · [GitHub](https://github.com/6missedcalls/personal-finance-skill) · [官网](https://agentskills.io) · 个人维护

**面向 AI agent 的个人金融技能包：75 个工具覆盖银行/交易/税务**

基于 Agent Skills Protocol 的个人金融技能，包含 7 个扩展、75 个工具：Plaid 银行账户接入、Alpaca 交易、IBKR 组合监控、税务引擎（15 种税表解析与 8 类计算器）、市场情报与社交情绪分析。所有计算由工具确定性完成，交易/转账/税务操作需经 finance_policy_check 策略门与人工确认；各来源数据规范化为共享数据模型。以 TypeScript/Node.js 编写，声明兼容 40 余种 AI agent（Claude Code、Cursor、Codex、OpenClaw、Windsurf 等），通过 npx skills add 安装或源码脚本接入 OpenClaw 插件体系。

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

- 7 扩展 75 工具：银行(Plaid)、交易(Alpaca)、组合(IBKR)、税务、市场情报、社交情绪
- 税务引擎含 15 种税表解析器与 8 类计算器（税负、TLH、wash sales、AMT 等）
- 所有操作经 finance_policy_check 策略门，实盘交易需人工确认，计算由工具而非 LLM 完成
- 612 个测试，55+ 测试文件

## 适用场景

- 让 AI agent 通过自然语言管理我的银行账户与投资组合
- 解析税表并做税损收割、季度预缴等税务计算
- 扫描交易异常、订阅扣费与余额波动并生成财务简报
- 聚合市场新闻、SEC 文件与社交情绪供投资参考

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: **75 tools** across **7 extensions** for banking, investing, tax optimization, market intelligence, social sentiment
> L29: - **Works with 40+ AI agents** — Claude Code, Cursor, Codex, OpenClaw, Windsurf, and more via the Agent Skills Prot
> L240: The onboard script builds all extensions, registers them as OpenClaw plugins, and installs the skill:

## 星数曲线

```mermaid
xychart-beta
    title "6missedcalls/personal-finance-skill 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-26", "2026-10-29"]
    y-axis "stars" 24 --> 29
    line [25, 26, 27, 28, 28]
```

2026-10-18 25 → 2026-10-29 28（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `38531b6170ac` · [字段定义](../../DATASET.md)*
