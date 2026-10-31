# MissiaL/avito-api

⭐ 15 · Python · NOASSERTION · 推送 2026-10-18 · [GitHub](https://github.com/MissiaL/avito-api) · 个人维护 · 中文 README

**让 AI agent 操作 Avito Business API 的技能包（SKILL.md+OpenAPI 快照）**

面向 Claude Code、Cursor、Copilot 等 30+ agent 客户端的 Agent Skill：打包 Avito Business API 的 OpenAPI 3.0 快照（248 路径/256 操作/27 分区）、原生分区文档、OAuth2 凭据助手，以及无需把约 2.2MB JSON 载入上下文即可检索端点定义的 CLI。用户配置 client_id/client_secret 环境变量后，agent 可代为管理商品、Messenger 聊天、配送、订单、招聘、统计与推广等。快照定格于 03.10.2026，官方目录此后再导出失败，方法新鲜度未验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 OpenAPI 3.0 快照：248 路径 / 256 操作 / 27 分区
- CLI 检索端点定义，避免将 ~2.2MB JSON 载入上下文
- OAuth2 凭据助手与按分区原生文档
- 适配 Claude Code、Cursor、Copilot、Goose 等 30+ agent 客户端

## 适用场景

- 让 AI agent 直接管理我的 Avito 商品与订单
- 通过对话操作 Avito Messenger 聊天与配送
- 构建 Avito API 集成时让 agent 查端点定义与文档

## 场景标签

 · 领域:电商/市场平台 API 工具

## 证据(README 行号)

> L3: Agent Skill в формате agentskills.io для работы с Avito Business API — управление объявлениями, чатами Messenger, Ав
> L28: Для других совместимых клиентов (Cursor, Goose, Copilot, OpenCode, OpenHands, Letta, и др. — полный список) — см. и

## 星数曲线

```mermaid
xychart-beta
    title "MissiaL/avito-api 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1e7caeb402c1` · [字段定义](../../DATASET.md)*
