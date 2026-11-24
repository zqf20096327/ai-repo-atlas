# mindsdb/anton

⭐ 756 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/mindsdb/anton) · [官网](https://mindsdb.github.io/anton/) · 组织维护

**可交任务的自改进 AI agent，供终端用户与开发者使用**

Anton 是驱动 MindsHub Cowork 的开源 agentic harness，也可独立运行于终端。用户以自然语言描述目标（发邮件、整理收件箱、出报告、订机票），agent 自行规划并执行：现场抓取数据、编写并运行代码、生成仪表盘。关键机制包括凭据保险库（防止密钥暴露给 LLM）、隔离代码执行、多层记忆与持续学习（session/语义/长期知识，写入 .anton/memory/）。它自行编写集成代码接入 WhatsApp、Telegram 等渠道。MIT 许可，收集匿名使用事件，可通过环境变量关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 凭据保险库隔离 secrets，不暴露给 LLM
- 多层记忆与持续学习（episodes/rules/lessons/topics 文件）
- web_search/web_fetch 工具按 LLM provider 原生路由或回退到 Exa/Brave
- 执行 scratchpad 动态充当所需工具，无需大量独立工具集

## 适用场景

- 让 agent 整理收件箱并处理退订
- 从多个数据库拉数并生成定期报告与仪表盘
- 让 agent 自己编写并部署 WhatsApp/Telegram 集成
- 监控数据源变化并自动执行工作流

## 场景标签

`工作流自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L14: Anton is the open-source agentic harness that powers **MindsHub Cowork** — a self-improving AI agent you can hand a
> L16: Hand it real work: create and send reports, clear your inbox, manage your calendar and CRM, book flights, and more.
> L90: - **Multi-layer memory & continuous learning** — session, semantic, and long-term knowledge. Anton remembers what i

## 星数曲线

```mermaid
xychart-beta
    title "mindsdb/anton 星数(近 6 点)"
    x-axis ["2026-10-22", "2026-10-28", "2026-11-01", "2026-11-06", "2026-11-20", "2026-11-24"]
    y-axis "stars" 755 --> 760
    line [757, 758, 759, 757, 756, 756]
```

2026-10-22 757 → 2026-11-24 756（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `4ae4c336985a` · [字段定义](../../DATASET.md)*
