# zifacorp/zifamem

⭐ 15 · Python · 推送 2026-07-21 · [GitHub](https://github.com/zifacorp/zifamem) · 组织维护

**AI 伴侣的情感长期记忆框架：记忆可强化、衰减与遗忘**

面向 AI 伴侣、角色扮演与关系型 agent 的情感长期记忆 Python SDK（alpha）。默认无 LLM 依赖：会话缓冲→摘要→L3 情感长期记忆→L4 用户画像的分层生命周期，提供记忆强化/衰减/遗忘 API 与组合语义、强度、重要度、近期性与情绪强度的召回排序；可选注入 OpenAI 兼容 LLMProvider 做提取，失败时回退启发式。本地存储为内存/JSON，数据库与向量适配器尚未实现，合并与反思循环仍在 TODO。附论文（arXiv 2607.17564）与两个 SKILL.md 格式 Agent Skills。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- L1-L4 分层记忆生命周期（会话缓冲/摘要/情感长期记忆/用户画像）
- 默认依赖启发式提取，无需 LLM；可选 OpenAI 兼容 Provider 并带回退
- 记忆强化/衰减/遗忘 API 与多因素情绪感知召回排序
- 可移植 Agent Skills（集成指南与记忆安全审计）

## 适用场景

- 让 AI 伴侣跨会话记住情感历史与关系演变
- 构建角色扮演、陪护、教练类 agent 的长期记忆层
- 为 agent 应用做记忆提取与召回的记忆安全审计

## 场景标签

 · 领域:LLM 基础设施/记忆层

## 证据(README 行号)

> L76: ZifaMem is an emotional long-term memory framework for AI agents, companions, and relationship-centered products.
> L171: - Agent-native interfaces for extraction, storage, retrieval, session consolidation, and prompt context assembly

## 星数曲线

```mermaid
xychart-beta
    title "zifacorp/zifamem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `d71b484d26cc` · [字段定义](../../DATASET.md)*
