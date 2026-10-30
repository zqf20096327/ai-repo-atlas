# RayP11/QuestChain

⭐ 15 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/RayP11/QuestChain) · 个人维护

**完全本地运行的自主 AI 助手：多智能体分工处理任务**

基于 Python 与 Ollama 的本地 AI 助手框架，全部运行在用户自有硬件上，支持小至 3B 参数的模型。功能包括文件读写、Shell 命令执行、网页搜索（Tavily 可选）、cron 定时任务、Telegram 远程访问、Kokoro TTS 语音输出与持久记忆。采用微智能体体系：协调者 Perseus 将工作路由给研究、知识、构建、规划等专职智能体，每个智能体有独立上下文与工具集，并以 RPG 升级系统（等级/成就/职业）呈现进展。提供 CLI、Web 与 Telegram 三种界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多智能体体系：协调者路由至研究/知识/构建/规划等专职智能体
- cron 定时任务、Telegram 远程访问、持久记忆与 TTS 语音输出
- 完全本地运行，支持小至 3B 参数的模型，无需云端
- 可委派编程任务给 Claude Code（可选）

## 适用场景

- 在本机 24/7 运行自主 AI 助手处理任务清单
- 定时执行摘要、整理等周期性工作并经 Telegram 汇报
- 让本地小模型以专职智能体分工完成文件、研究、编码任务

## 场景标签

`AI 助手` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L17: QuestChain is an AI assistant that runs entirely on your machine. No cloud, no subscriptions, no usage limits. Just
> L25: QuestChain is that framework: a party of micro agents all jam-packed with tool loadouts for specific tasks, fully a
> L203: Most AI tools assume cloud infrastructure and always-online connections. QuestChain runs on the hardware you alrea

## 星数曲线

```mermaid
xychart-beta
    title "RayP11/QuestChain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8b6f36d74cbf` · [字段定义](../../DATASET.md)*
