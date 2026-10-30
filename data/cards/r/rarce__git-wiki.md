# rarce/git-wiki

⭐ 22 · Shell · MIT · 推送 2026-06-04 · [GitHub](https://github.com/rarce/git-wiki) · 个人维护

**在自有 git 仓库中自维护知识 wiki 的 Agent 技能**

实现 Karpathy LLM-wiki 模式的 Agent Skills 技能：agent 摄取来源文献后自行撰写与维护 wiki 页面（pages/people/concepts），通过 index.md 目录与 append-only 的 log.md 导航，用 qmd 在设备端做 BM25+向量+LLM 重排的混合检索，并带 lint 检查过期日期、孤儿页、断链与矛盾。数据即用户自己的 git 仓库，默认本地提交、可选发布到 GitHub，无服务器与外部 DB。需在 Agent-Skills 兼容的 agent（Claude Code、Cursor、Copilot 等）中使用，依赖 bash、git、qmd，GitHub 模式还需 gh。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层结构：不可变 sources/、LLM 维护的 wiki 页面、CLAUDE.md+SKILL.md 约定
- qmd 设备端混合检索（BM25+向量+LLM 重排），不上传 embedding
- lint 检查过期日期、孤儿页、断链、索引漂移与矛盾
- wiki 即 git 仓库，diff 即变更日志，支持 WIKI_SUBDIR 多用途仓库共存

## 适用场景

- 让 agent 记住我读过的论文、文章与文档并可检索引用
- 把个人知识库保存在自己控制的 git 仓库里而非厂商 DB
- 在同一个仓库中让 wiki 与代码文档共存

## 场景标签

`知识库管理` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L8: **A self-maintaining knowledge wiki that lives in your own git repo.** Your agent ingests sources, writes the pages,
> L22: - **Agent-Skills standard** — works with Claude Code, Cursor, Codex, Copilot, or any [Agent-Skills-compatible agent
> L65: > **This repo hosts the skill, not a wiki.** Installing it gives your agent

## 星数曲线

```mermaid
xychart-beta
    title "rarce/git-wiki 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0fce0e523e6a` · [字段定义](../../DATASET.md)*
