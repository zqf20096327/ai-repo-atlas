# Blackdesk-ai/blackdesk

⭐ 15 · Go · Apache-2.0 · 推送 2026-04-28 · [GitHub](https://github.com/Blackdesk-ai/blackdesk) · [官网](https://blackdesk.ai/) · 组织维护

**开源终端行情研究台：行情/新闻/筛选器与本地 AI 连接器**

本地优先、键盘操作的市场研究终端（TUI），将个股报价、图表、技术指标、新闻、基本面、财报、内部人交易与筛选器整合在同一终端界面，并提供面向本地 AI 编程工具（Codex、Claude Code、Opencode）的连接器，将市场上下文提供给这些模型。通过 curl 安装脚本分发二进制，支持 macOS/Linux/Windows，采用可替换的行情数据源与连接器架构。声明为研究工具，不提供投资建议或交易执行；项目处于活跃开发期，功能与安装渠道可能变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 报价/市场/新闻/筛选器/AI 五个产品面整合于单一终端界面
- 本地 AI 连接器当前支持 Codex、Claude Code、Opencode
- 可替换的行情数据源与连接器架构
- curl 脚本安装二进制，含 blackdesk upgrade 自升级命令

## 适用场景

- 在一个键盘操作终端中完成个股研究与市场扫描，不依赖浏览器多标签
- 把行情上下文交给本地 Codex / Claude Code / Opencode 做 AI 辅助分析
- 跟踪动股、新闻流与筛选器发现交易标的

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L7:  Quotes, charts, technicals, news, fundamentals, statements, insiders, screeners, and local AI connectors in one key
> L62: - `AI`: local connectors targeted with desk-aware market context
> L63:  currently `Codex`, `Claude Code`, and `Opencode`

## 星数曲线

```mermaid
xychart-beta
    title "Blackdesk-ai/blackdesk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a5f1cc786c89` · [字段定义](../../DATASET.md)*
