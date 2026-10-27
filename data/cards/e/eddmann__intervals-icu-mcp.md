# eddmann/intervals-icu-mcp

⭐ 37 · Python · MIT · 推送 2025-11-06 · [GitHub](https://github.com/eddmann/intervals-icu-mcp) · 个人维护

**让 Claude 等 LLM 操作 Intervals.icu 训练数据的 MCP 服务器**

基于 Model Context Protocol 的服务器，通过 48 个工具（9 类）、1 个资源与 6 个提示模板，让 Claude 等 LLM 读取和操作用户的 Intervals.icu 账户：活动查询与分析、CTL/ATL/TSB 体能指标、HRV/睡眠等健康数据、日历与训练计划批量管理、功率/心率/配速曲线、装备管理与运动阈值设置。采用 API Key + Basic Auth 认证，凭据存于 .env；支持 uv 或 Docker 两种部署方式，需 Python 3.11+。项目声明与 Intervals.icu 无官方关联。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 48 个工具覆盖活动、分析、健康、日历、装备等 9 类操作
- 提供运动员档案 MCP 资源与 6 个查询提示模板
- 支持 uv 与 Docker 两种安装运行方式
- API Key + Basic Auth 认证，凭据持久化到 .env

## 适用场景

- 用自然语言查询我的骑行/跑步活动与功率数据
- 让 AI 评估我的恢复状态与训练负荷（CTL/ATL/TSB）
- 通过对话批量创建和管理训练计划
- 用 AI 协助制定基于当前体能的周训练安排

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: A Model Context Protocol (MCP) server for Intervals.icu integration. Access your training data, wellness metrics, an
> L11: This MCP server provides 48 tools to interact with your Intervals.icu account, organized into 9 categories:
> L103: ## Claude Desktop Configuration

## 星数曲线

```mermaid
xychart-beta
    title "eddmann/intervals-icu-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2ceb1c2b0837` · [字段定义](../../DATASET.md)*
