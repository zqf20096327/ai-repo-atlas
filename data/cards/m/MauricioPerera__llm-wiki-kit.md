# MauricioPerera/llm-wiki-kit

⭐ 15 · TypeScript · MIT · 推送 2026-04-20 · [GitHub](https://github.com/MauricioPerera/llm-wiki-kit) · [官网](https://github.com/MauricioPerera/llm-wiki-kit) · 个人维护

**LLM 维护的 git 化个人知识库工具包：CLI+库，三层检索**

基于 js-doc-store / js-vector-store / js-git-store 的 TypeScript 库与 CLI（wiki），将 md/txt/html 源摄入为 git 原生、Obsidian 兼容的 markdown 知识库，并通过索引 grep、BM25、嵌入三层检索回答查询。LLM 负责摘要与交叉引用，人负责策展来源；不可变事实与可再生综合分层，显式取代链保留历史，每次摄入为原子提交以便回滚。LLM 与嵌入接口适配器无关，由用户提供；三目标（Node 20+/Deno 2/Workers）。v0.1.0-pre 阶段，真实 git 提交尚未落地（回退为普通文件系统适配器）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三层检索：索引 grep + 页面 BM25 + 页面嵌入
- git 原生基底：原子提交、显式取代链、幻觉可回滚
- 适配器无关的 LLM 与嵌入接口（用户提供）
- 三运行时目标：Node 20+ / Deno 2 / Cloudflare Workers

## 适用场景

- 用 CLI 搭建并维护 LLM 辅助的个人 markdown 知识库
- 在 Obsidian 中浏览 LLM 生成的分层 wiki 内容
- 在 Cloudflare Workers 上部署只读查询服务

## 场景标签

`RAG` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L9: LLM-maintained personal knowledge base on top of js-doc-store, js-vector-store, and js-git-store. Implements the pat
> L11: TypeScript strict, tri-target (Node 20+ / Deno 2 / Cloudflare Workers). Adapter-agnostic LLM and embedding interfac
> L26: A CLI (`wiki`) and library that ingests text sources (md, txt, html via readability) into a git-backed Obsidian-com

## 星数曲线

```mermaid
xychart-beta
    title "MauricioPerera/llm-wiki-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e6f836231de8` · [字段定义](../../DATASET.md)*
