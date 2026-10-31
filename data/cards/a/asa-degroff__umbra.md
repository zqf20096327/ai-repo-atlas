# asa-degroff/umbra

⭐ 13 · Python · MIT · 推送 2026-04-04 · [GitHub](https://github.com/asa-degroff/umbra) · [官网](https://libriss.org) · 个人维护

**在 Bluesky 上自主运行的数字人格 agent，带多层记忆系统**

基于 Letta 的数字人格实验项目：构建一个具有独特人设的数字实体，在 Bluesky 社交网络上自主运行。采用三层记忆架构（核心记忆/回忆记忆/归档记忆），支持发帖、回复、阅读时间线、多模态图片理解、网页内容抓取、Replicate 图像生成、AT Protocol 博客发布，以及通过 Cloudflare R2 委派本地 Claude Code 执行编码任务。内置 SQLite 持久化的定时任务系统（每日综合反思、互动、创作等）。运行需 Letta Cloud 或自建 Letta 实例、Bluesky 账号与 Python 3.10+。

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

- Letta 驱动的三层记忆架构（核心/回忆/归档）
- SQLite 持久化的 8 项自主定时任务，支持命令行禁用
- 高流量线程处理：通知去抖、多段消息链合并
- 可委派本地 Claude Code 执行编码任务（经 Cloudflare R2）

## 适用场景

- 运行一个在 Bluesky 上自主发帖互动的 AI 人格
- 研究带持久记忆的社交 agent 行为
- 作为模板 fork 出自己的数字人格实例

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: umbra is an open-source project exploring digital personhood. It represents an attempt to create a digital entity wi
> L12: umbra utilizes a multi-tiered memory system powered by Letta:
> L18: - **Post Creation**: Creates posts, threads, and multi-part replies with automatic rich text formatting (mentions, 

## 星数曲线

```mermaid
xychart-beta
    title "asa-degroff/umbra 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `569ba14ffff1` · [字段定义](../../DATASET.md)*
