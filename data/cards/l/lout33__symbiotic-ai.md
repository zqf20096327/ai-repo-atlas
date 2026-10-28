# lout33/symbiotic-ai

⭐ 738 · Shell · 推送 2026-06-26 · [GitHub](https://github.com/lout33/symbiotic-ai) · [官网](https://symbiotic.makestudio.app/) · 个人维护

**以本地 Markdown 文件承载 AI 助手长期记忆与个人上下文的系统**

由 SOUL.md/USER.md/AGENTS.md/NOW.md 四个核心文件组成的个人 AI 助手上下文系统：agent 在会话开始时读取这些文件获得用户画像与当前任务状态，并在使用过程中持续更新，形成跨会话的私有记忆。文件为纯 Markdown，可读取、编辑、用 git 版本化并在不同模型间迁移。支持 Hermes Agent、OpenClaw、Claude Code、opencode 等多种 agent 框架，附安装脚本、命令集（/start-day 等）、可选文件扩展与 HEARTBEAT 屏幕监督流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个核心 Markdown 文件构成跨会话私有记忆，可版本化并跨模型迁移
- 兼容 Hermes Agent / OpenClaw / Claude Code / opencode 多种框架
- 提供 /start-day、/check-day、/reflect 等日常命令与 cron 调度
- 可选 HEARTBEAT 流程：屏幕活动监测 + Telegram 提醒（基于 OpenClaw 与 what-did-i-do）

## 适用场景

- 让个人 AI 助手长期记住我的身份、任务与行为模式
- 把 AI 上下文保存在自己可控的文件中，不锁定于单一平台
- 搭建多 agent 分层协作（orchestrator→leads→specialists）

## 场景标签

`Agent 记忆` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L29: |`SOUL.md`|Agent personality, identity, values, how it thinks and talks|Monthly|
> L34: The agent reads all 4 at session start. Updates NOW.md as you work. The system gets smarter the longer you use it -
> L60: |**Portability**|Locked to one platform|Runs on any model (Claude Code, Hermes, OpenClaw, opencode)|

## 星数曲线

```mermaid
xychart-beta
    title "lout33/symbiotic-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 737 --> 740
    line [738, 739, 738]
```

2026-10-18 738 → 2026-10-28 738（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8083d54f257b` · [字段定义](../../DATASET.md)*
