# hudikiller/roundtable

⭐ 3 · TypeScript · MIT · 推送 2026-10-12 · [GitHub](https://github.com/hudikiller/roundtable) · 个人维护 · 中文 README

**飞书群聊里的 AI 队友：记录全员讨论并转为可交付任务**

部署在 Feishu/Lark 群中的长期 agent：持续存储主时间线与话题的全部消息（含未 @ 机器人者），每次被提及接收增量上下文；按保守策略回应，默认不插话。每个话题对应独立工作区、Codex 线程与 Docker 沙箱，任务被派发到团队服务器或成员个人电脑上的 Runner，通过卡片实时展示进度并由人点击接受或驳回。业务仓库不被自动推送或合并；交付失败重试而不重跑模型。需自建飞书应用、Linux 服务器与 OpenAI Responses 兼容的模型服务。

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

- 群级长期记忆：导入完整历史、完整 transcript 写入 history.md、可增删记忆条目
- 话题即会话：独立工作区/Codex 线程/沙箱，主聊天中的旁支发言自动路由到对应任务
- Runner 机制：工作派发到团队服务器或成员笔记本，长轮询无需公网 IP
- 每任务 Docker 沙箱：非 root、只读根文件系统、能力全丢弃、出口走白名单代理

## 适用场景

- 团队讨论后让 bot 总结决议并生成 @ 分工清单
- 在群聊话题里用自然语言指派代码修改到自己的电脑执行
- 任务卡片上实时查看计划步骤、变更文件并通过按钮验收

## 场景标签

`Agent 记忆` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L5: An AI teammate for Feishu/Lark that listens to the whole room, speaks rarely, and turns discussions into delivered w
> L50: - **Isolation.** Each topic has its own workspace, Codex thread and sandbox.
> L63: - **One intent model for everything.** Grants, stop, progress, accept/reject, machine choice, model choice, attachm


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `52f4de811e4d` · [字段定义](../../DATASET.md)*
