# MaestroAgent/maestro

⭐ 26 · TypeScript · MIT · 推送 2026-03-24 · [GitHub](https://github.com/MaestroAgent/maestro) · 组织维护

**面向收入运营的开源多智能体平台，AI 代理团队协同工作**

基于多智能体编排运行时的 RevOps 平台：提供管道管理、内容创作、线索资格评估等专职代理，代理间可通过 delegate_to_agent 横向协作，编排器只负责初始路由。内置 CRM（SQLite 存储联系人/公司/交易），支持 CLI、REST API、Telegram、Slack 多通道接入，具备持久记忆、按代理/会话的 token 成本追踪与预算守护。前置要求 Node.js 22+ 与 Anthropic API key，提供 Docker 与本地 npm 两种运行方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扁平代理架构：任意代理可横向委托协作，编排器仅做初始路由
- 内置 SQLite CRM 与持久记忆，数据跨重启保留
- CLI / REST API / Telegram / Slack 多通道接入
- 按代理、按会话的 token 成本追踪与预算守护

## 适用场景

- 让销售与营销 AI 代理团队处理管道管理和线索资格评估
- 通过 Telegram/Slack/CLI 等渠道按需调用专职代理
- 跟踪各代理会话的 token 成本并设置预算上限

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7:  An AI-native RevOps platform — sales and marketing agents that work as a coordinated team. Like having a full reven
> L13: Maestro is an open-source platform of specialized AI agents for revenue operations, built on a multi-agent orchestr

## 星数曲线

```mermaid
xychart-beta
    title "MaestroAgent/maestro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f1b667f70a99` · [字段定义](../../DATASET.md)*
