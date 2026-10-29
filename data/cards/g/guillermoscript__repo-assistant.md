# guillermoscript/repo-assistant

⭐ 39 · TypeScript · ISC · 推送 2026-05-03 · [GitHub](https://github.com/guillermoscript/repo-assistant) · [官网](https://guillermoscript.github.io/blog/posts/repo-assistant-ai) · 个人维护

**GitHub issue 分诊机器人：嵌入检索 + LLM 判定重复并自动打标**

以 GitHub Action 或 Probot 服务运行的 issue 分诊机器人：新 issue 的标题与正文经 OpenAI 嵌入存入用户自备的 Postgres+pgvector（Neon/Supabase 等），经 HNSW 余弦相似度（≥0.65）检索候选后由 LLM 判定是否重复并输出 0-100 置信分，按阈值打 duplicate/possible-duplicate 标签或转为自动分类打标，支持跨语言重复识别与 72 小时后自动关闭（可选）。还提供 @bot dup/notdup/quality/relabel 评论命令与存量 issue 同步。面向开源仓库维护者，需自备 OpenAI API key 与 pgvector 数据库，处于初期阶段（当前本地运行）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 两阶段检索：嵌入召回（≥0.65）+ LLM 语义判定，输出 0-100 置信分
- 识别相同、改写与跨语言重复，置信分三档分流（duplicate/possible-duplicate/自动打标）
- @bot dup/notdup/quality/relabel 评论命令与存量 issue 同步
- 数据存用户自己的 Postgres，AI 调用走用户自己的 key，无共享后端

## 适用场景

- 开源仓库自动识别并关联合并重复 issue
- 为无标签 issue 自动分类（bug/enhancement/documentation 等）
- 维护者在 issue 线程里用 @bot 命令复核或改标

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L9: 3. **An LLM judges** the top candidates and emits a 0-100 confidence score:
> L140: - **Vercel AI SDK** for both `embed` (single-issue match) and `embedMany` (chunk batching), and `generateText` + `

## 星数曲线

```mermaid
xychart-beta
    title "guillermoscript/repo-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-29 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6c42b12daf14` · [字段定义](../../DATASET.md)*
