# Zyling-ai/ZyHive

⭐ 19 · Go · AGPL-3.0 · 推送 2026-08-02 · [GitHub](https://github.com/Zyling-ai/ZyHive) · [官网](https://zyling.ai) · 组织维护 · 中文 README

**自托管的多智能体团队管理与协作平台**

用 Go + Vue 3 实现的单机自托管系统，把 AI Agent 组织为具有身份、记忆、工具、工作区和协作关系的团队成员。功能包括：创建多个 AI 成员并配置模型/技能/工具权限、Web 管理界面对话与会话持久化、成员关系与受控派遣协作、Cron/Telegram/飞书/公开 Web 聊天入口、两层工具策略与 allow/deny/ask 审批、备份恢复与在线更新。面向个人、小团队和可控环境部署，明确声明不是多租户 SaaS 或企业级高可用平台；部分功能（如 aiteam 自治经济模块）默认关闭且属 Labs。采用 Draft-first 发布门禁，提供 SHA-256 校验与 cosign 可选签名验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AI 成员可配置身份、记忆、技能与工具权限，通过成员关系组织协作
- 全局与成员两层工具策略，支持 allow/deny/ask 审批与工具审计
- 多种运行入口：Cron、Telegram、飞书、公开 Web 聊天
- 一键安装脚本（macOS/Linux amd64/arm64），含 SHA-256 校验与 systemd/launchd 服务注册

## 适用场景

- 在自有服务器上搭建并可视化管理的多智能体团队
- 为不同任务配置不同身份与工具权限的 AI 成员并派遣协作
- 通过 Telegram、飞书或公开 Web 聊天与 AI 成员对话

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: > 自托管的 AI 团队操作系统：以团队为核心，把 AI Agent 组织为有身份、记忆、工具、工作区和协作关系的成员。
> L26: - 创建多个 AI 成员，分别配置身份、行为风格、模型、记忆、技能和工具权限；
> L28: - 通过成员关系、共享项目和受控派遣组织协作；

## 星数曲线

```mermaid
xychart-beta
    title "Zyling-ai/ZyHive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ecaf38205a60` · [字段定义](../../DATASET.md)*
