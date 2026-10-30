# galimba/agentic-memory-vault

⭐ 15 · Shell · Apache-2.0 · 推送 2026-07-10 · [GitHub](https://github.com/galimba/agentic-memory-vault) · 个人维护

**给 AI agent 与人类团队共用的 git+Markdown 记忆库模板**

基于 git 与 Markdown 的组织级知识库脚手架：克隆模板并初始化后，AI agent（Claude Code、Codex、Copilot、Cursor）与人类团队在由 YAML frontmatter 与 wikilinks 组织的目录上执行三种操作——INGEST（把 raw/ 源文档加工为结构化 wiki 页）、QUERY（基于索引回答并附 wikilink 引用）、LINT（检查矛盾、孤儿页与过期内容）。15 条硬规则由 git hooks 强制执行，230 个预批准标签。核心流程只需 bash/git/Unix 工具，python3 仅为部分审计工具所需。无数据库、无外部服务，检索为确定性索引式而非向量搜索。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- INGEST/QUERY/LINT 三操作的 vault 架构
- 15 条由 git hooks 强制的硬规则与 10 条可配置软规则
- 多平台 agent 配置适配（Claude Code/Codex/Copilot/Cursor，以 AGENTS.md 为规范）
- 230 个预批准标签、19 个前缀类别的标签体系

## 适用场景

- 为团队 AI agent 建立可审计、可 diff/回滚的机构记忆库
- 让 agent 把源文档加工成结构化 wiki 并基于其回答问题
- 用 git hooks 与 lint 规则维护知识库一致性

## 场景标签

`知识库管理` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L12: Memory Vault is a git-based knowledge management system designed for AI agents
> L21: Agents process sources into wiki pages, answer questions from the knowledge base,

## 星数曲线

```mermaid
xychart-beta
    title "galimba/agentic-memory-vault 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3cbc944e3743` · [字段定义](../../DATASET.md)*
