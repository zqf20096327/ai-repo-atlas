# ximing/aimo

⭐ 27 · TypeScript · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/ximing/aimo) · [官网](https://aimo.plus) · 个人维护 · 中文 README

**AI First 自托管卡片笔记：AI 负责检索、关联与复习**

AIMO 是一张卡片一个想法的自托管笔记应用，AI 作为内置能力提供智能摘要、基于 OpenAI Embedding 的语义搜索、笔记间智能关联与可视化知识图谱、每日推荐和间隔重复复习。数据存储在用户自己的机器（MySQL 存关系数据、LanceDB 存向量），也可作为 Agent 的私有记忆。支持 Docker 一键部署（自带 MySQL 编排）、Electron 桌面端（macOS/Windows/Linux）、Android APK 与 PWA，浏览器扩展开发中。本地开发需 Node.js 20+、pnpm、MySQL/MariaDB 与 OpenAI API Key。许可证为 BSL 1.1，禁止对外提供竞品 SaaS，四年后转 MIT，另可联系商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 OpenAI Embedding 的语义搜索（LanceDB 向量存储）
- AI 智能摘要、笔记关联图谱与间隔重复复习
- Docker Compose 一键部署，数据持久化在宿主机目录
- 多端支持：Web、Electron 桌面端、Android、PWA

## 适用场景

- 随手记录想法，用 AI 语义搜索和关联快速找回
- 通过间隔重复复习把笔记转化为长期记忆
- 自托管个人知识库，数据留在自己的机器上
- 给 Agent 提供私有记忆存储

## 场景标签

 · 领域:知识管理/笔记应用

## 证据(README 行号)

> L14: AI First 卡片笔记。随手记下想法，检索、关联和复习交给 AI；数据留在自己的机器上，也可以给 Agent 当私有记忆用。
> L33: - **智能摘要** - AI 自动生成笔记摘要，快速提炼关键信息
> L34: - **语义搜索** - 基于 OpenAI Embedding 的向量搜索，理解含义而非匹配关键词

## 星数曲线

```mermaid
xychart-beta
    title "ximing/aimo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `01f29db30922` · [字段定义](../../DATASET.md)*
