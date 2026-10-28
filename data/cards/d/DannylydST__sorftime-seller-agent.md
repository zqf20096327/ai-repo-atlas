# DannylydST/sorftime-seller-agent

⭐ 40 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/DannylydST/sorftime-seller-agent) · [官网](https://open-intl.sorftime.com) · 组织维护 · 中文 README

**面向跨境电商卖家的 AI 选品与市场情报 MCP 工具集**

Sorftime 出品的开源 MCP 技能/工具层：向任意 MCP 兼容 AI agent（Claude Code、Codex、Cursor、OpenClaw 等）提供 97 个工具，覆盖 Amazon、Walmart、TikTok Shop、Shopee、TEMU、1688 六平台的产品研究、竞品逆向 ASIN、关键词研究、FBA 利润计算与价格/销量监控。核心机制包括 Hidden Profit Index 算法、闭环选品工作流、7 个独立 AI 评审子 agent 投票，以及 4 级咨询式风险标记（不隐藏产品）。数据需在 open-intl.sorftime.com 注册账号，免费试用额度，超出按用量付费；自带 Python venv，Python 3.10+ 为唯一依赖。

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

- 97 个 MCP 工具，agent 无关设计，兼容 Claude Code/Codex/Cursor/OpenClaw 等
- 六平台数据：Amazon、Walmart、TikTok Shop、Shopee、TEMU、1688
- Hidden Profit Index 与 5D 信号评分选品工作流
- 7 个独立 AI 评审子 agent 加权投票产出 GO/CAUTION/NO-GO

## 适用场景

- 我是 Amazon 卖家，想用对话找蓝海产品和做竞品逆向分析
- 我在 Shopee/TikTok Shop 做类目调研和趋势监控
- 我想跨平台比价找套利机会并对接 1688 工厂货源
- 我是电商代运营，想批量分析客户竞品并自动监控价格销量

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L11: > Open source. Free trial. Works with any MCP-compatible AI agent — Claude Code, Codex, Cursor, OpenClaw, and more.
> L128: **Not a Claude Code plugin. Not an API wrapper.** A self-contained MCP bridge + intelligence layer that any MCP-co
> L140: - **MCP-first architecture** — 97 tools, auto-synced with Sorftime server. Pure MCP protocol.

## 星数曲线

```mermaid
xychart-beta
    title "DannylydST/sorftime-seller-agent 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24", "2026-10-28"]
    y-axis "stars" 35 --> 41
    line [36, 38, 39, 40]
```

2026-10-18 36 → 2026-10-28 40（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `617d67e45b0e` · [字段定义](../../DATASET.md)*
