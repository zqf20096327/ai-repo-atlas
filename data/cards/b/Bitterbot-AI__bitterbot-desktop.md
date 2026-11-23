# Bitterbot-AI/bitterbot-desktop

⭐ 2,480 · TypeScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/Bitterbot-AI/bitterbot-desktop) · [官网](https://bitterbot.ai) · 组织维护

**运行在本机的个人 AI 代理，持久记忆并可积累技能**

Bitterbot 是开源的个人代理应用，运行在用户自己的机器上，跨对话保留记忆，可经浏览器自动化、代码执行和即时通讯渠道执行任务。核心机制包括：文件与 SQLite 存储的记忆系统（canonical-facts 账本、语义检索、知识图谱）、默认每 2 小时运行的 Dream Engine（记忆整理、模拟、蒸馏等模式），以及技能进化管线——生成的技能需在保留任务上通过统计验证、金丝雀与回归监控后才被晋升。提供安装脚本、npm、Docker、源码四种安装方式，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 记忆、身份与技能以文件和 SQLite 形式存于本地磁盘，可检查与备份
- Dream Engine 定期整理记忆、蒸馏可复用技能，含多种后台模式
- 技能晋升需通过保留任务评测、回归与成本检查，暴露验证证据
- 支持 Control UI、WhatsApp、Telegram、Discord、Signal、Slack、邮件等多渠道

## 适用场景

- 让代理记住我的项目背景并在下次对话延续
- 定时汇总项目任务并通过 Telegram 发送报告
- 读取本地 CSV 并生成差异分析报告

## 场景标签

`AI 助手` `Agent 记忆` `浏览器自动化` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L27: Bitterbot runs on your machine, remembers context across conversations, and works through a real browser, code exec
> L6:  A personal agent with living memory, a dream engine, and skills that have to prove themselves.
> L31: Your agent's memory, identity, and skills live in files and SQLite on your disk. Inspect them. Back them up. Choose

## 星数曲线

```mermaid
xychart-beta
    title "Bitterbot-AI/bitterbot-desktop 星数(近 13 点)"
    x-axis ["2026-10-21", "2026-10-23", "2026-10-25", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23"]
    y-axis "stars" 2475 --> 2489
    line [2476, 2477, 2478, 2480, 2478, 2483, 2484, 2486, 2487, 2488, 2480, 2481, 2480]
```

2026-10-21 2,476 → 2026-11-23 2,480（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `dca93f18bbea` · [字段定义](../../DATASET.md)*
