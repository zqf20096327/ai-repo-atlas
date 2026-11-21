# luizgustavosaraiva/hermes-profiles

⭐ 4 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/luizgustavosaraiva/hermes-profiles) · [官网](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions) · 个人维护

**为 Hermes Agent 提供一键安装的现成 agent 配置包**

面向 Nous Research 的 Hermes Agent 框架，将完整 agent 以 profile 发行版形式打包：SOUL.md 人格、config、skills、模板随版本一起分发，用户通过一条 shell 命令或 git clone 手动安装。更新机制保留用户的 memories、sessions、.env 与 local/ 目录不被覆盖；每个 profile 提供 EN/PT-BR 双语文档，并在 CI 中校验 manifest、结构与泄露的密钥。目前收录 recruiter 一个 profile，用于读取仓库并组建多 agent 团队与 Kanban 板。

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

- SOUL/config/skills/模板整体打包的 profile 发行版
- 安装脚本更新时不覆盖 memories、sessions、.env 与 local/
- CI 校验 manifest、结构与密钥泄露
- 全部 profile 提供 EN 与 PT-BR 双语文档

## 适用场景

- 为 Hermes Agent 快速装配现成的多 agent 团队
- 读取代码仓库并自动生成 orchestrator+specialists 团队与 Kanban 板
- 以可更新方式维护个人 agent 配置而不丢失会话记忆

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Ready-made, battle-tested agents for Hermes Agent.**
> L110: Built on Hermes Agent by
> L111: Nous Research. Not affiliated with Nous Research.

## 星数曲线

```mermaid
xychart-beta
    title "luizgustavosaraiva/hermes-profiles 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-21"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-08 4 → 2026-11-21 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e797c2ab43ff` · [字段定义](../../DATASET.md)*
