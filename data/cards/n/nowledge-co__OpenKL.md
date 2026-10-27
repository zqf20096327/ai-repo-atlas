# nowledge-co/OpenKL

⭐ 124 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/nowledge-co/OpenKL) · [官网](https://nowled.ge/kl) · 组织维护

**给个人 AI agent 的本地优先知识与记忆层**

OpenKL 是面向个人 agent 的本地优先开源知识与记忆层，提供统一协议与实现，使任何 agent 可访问单一用户的知识。功能包括记忆管理（洞察/事实/笔记的时间组织）、外部语料 Grounding Store（自动分块）、基于 LadybugDB 的知识图谱、可复现引用、HNSW 向量搜索与跨记忆/语料的混合搜索，CLI 采用 pipe-first 设计并输出 citation-ready JSON。项目自述处于早期开发阶段；LadybugDB 迁移尚不提供，旧 Kuzu 安装需回退指定修订版使用。通过 uv 安装，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 记忆管理 + Grounding Store + LadybugDB 知识图谱三层结构
- 原生 HNSW 向量索引与跨记忆/语料混合搜索
- 可复现、可验证的引用机制（transient/persisted 两种模式）
- pipe-first CLI 与面向 agent 的 citation-ready JSON 输出

## 适用场景

- 为我的个人 AI agent 提供统一的本地记忆与知识存取层
- 在对话中引用可验证出处的记忆与文档片段
- 管理带有时间组织的用户洞察、事实与笔记

## 场景标签

`知识库管理` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: A local-first, open-source knowledge and memory layer for AI agents. OpenKL provides a unified protocol and implemen
> L11: - **Memory Management**: Distilled insights, facts, and user-provided notes with temporal organization

## 星数曲线

```mermaid
xychart-beta
    title "nowledge-co/OpenKL 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-10-27"]
    y-axis "stars" 123 --> 125
    line [124, 124]
```

2026-10-25 124 → 2026-10-27 124（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c76199555cfd` · [字段定义](../../DATASET.md)*
