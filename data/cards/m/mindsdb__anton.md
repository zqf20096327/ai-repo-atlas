# mindsdb/anton

⭐ 757 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/mindsdb/anton) · [官网](https://mindsdb.github.io/anton/) · 组织维护

**自我改进的通用任务 agent，替用户完成发邮件、报表、自动化等实际工作**

由 MindsHub 团队维护的开源 agentic harness，是 MindsHub Cowork 的默认 agent，也可在终端独立运行，支持任意模型（Anthropic/OpenAI BYOK、MindsHub 路由及 Together/Groq/Ollama/vLLM 等 OpenAI 兼容端点）。用户描述目标后由 agent 自行拆解步骤：连接 Gmail/日历/数据库，现场写代码并隔离执行，交付报表、仪表盘或集成。内置凭据保险库、多层记忆（会话/语义/长期）与 web_search/web_fetch 工具。提供 curl/PowerShell 一键安装脚本。

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

- 描述目标即执行：现场写代码、隔离执行环境完成数据分析与集成构建
- 多层记忆与持续学习（episodes/rules/lessons/topics 工作区结构）
- 凭据保险库防止 secrets 暴露给 LLM
- web_search/web_fetch 按提供商自动路由，兼容任意 OpenAI 兼容端点

## 适用场景

- 让 agent 清理邮箱、管理日历与 CRM 等重复性事务
- 自动生成投研组合仪表盘与定时报表
- 让 agent 自己编写并部署 WhatsApp/Telegram 集成
- 连接数据库与 API 做数据管道原型与系统管理

## 场景标签

`AI 助手` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L14: Anton is the open-source agentic harness that powers **MindsHub Cowork** — a self-improving AI agent you can hand a
> L16: Hand it real work: create and send reports, clear your inbox, manage your calendar and CRM, book flights, and more.

## 星数曲线

```mermaid
xychart-beta
    title "mindsdb/anton 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 756 --> 758
    line [757, 757]
```

2026-10-18 757 → 2026-10-26 757（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `a3a35cbe331e` · [字段定义](../../DATASET.md)*
