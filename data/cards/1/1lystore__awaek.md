# 1lystore/awaek

⭐ 30 · Python · 推送 2026-05-24 · [GitHub](https://github.com/1lystore/awaek) · [官网](https://awaek.me) · 个人维护

**让 AI agent 对话式检索你的 X 收藏的本地技能包**

面向 Hermes Agent 与 OpenClaw 的 agent 技能：通过 xurl 官方 API 分页同步 X 收藏，存入本地 SQLite，做分类、长文切块、可信域名链接追踪并建本地搜索索引，生成可引用的证据包；agent 据此回答问题、起草推文/计划、总结收藏主题。无托管后端，X 认证保留在 xurl 中。安装需 agent 宿主、Python 3 与已认证的 xurl。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经 xurl 同步 X 收藏到本地 SQLite，无托管后端
- 收藏分类、长文切块、构建可引用的证据包
- 回答强制引用收藏证据并区分证据强弱
- 支持 Hermes Agent 与 OpenClaw 两种宿主

## 适用场景

- 把我收藏的 X 帖子变成可问答的私人知识库
- 基于收藏的帖子起草推文或产品发布计划
- 回顾自己反复收藏了哪些主题

## 场景标签

`RAG` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: Awaek turns your saved X posts into a personal AI you can chat with — running locally inside Hermes Agent or OpenCla
> L53: Under the hood, Awaek syncs via `xurl`, stores locally in SQLite, categorizes bookmarks, chunks long posts, tracks 
> L105: - Hermes Agent or OpenClaw

## 星数曲线

```mermaid
xychart-beta
    title "1lystore/awaek 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-30 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `52acd556aa01` · [字段定义](../../DATASET.md)*
