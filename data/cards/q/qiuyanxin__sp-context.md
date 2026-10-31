# qiuyanxin/sp-context

⭐ 14 · TypeScript · MIT · 推送 2026-04-08 · [GitHub](https://github.com/qiuyanxin/sp-context) · 个人维护 · 中文 README

**给 AI 编程 agent 提供团队知识持久记忆的 CLI 工具**

面向 Claude Code、Codex、Cursor 等 AI 编程 agent 的知识管理 CLI：以 Git 仓库存储团队决策、架构、经验等文档，用 BM25+CJK bigram 检索替代向量库与 RAG 管线。会话启动时由 hook 注入约 100 token 的目录概览，agent 按需通过 sp search/sp get 分层加载全文。提供 7 种文档类型、文档链接、数据治理命令（doctor/gc/schema）、Unix 管道组合，以及可选的 Claude Code 插件技能与自托管 HTTP 同步服务器（webhook/定时同步）。运行需 Bun 与 Git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Git + BM25 + CJK bigram 检索，无向量库与 RAG 管线
- 三层渐进加载：目录概览(~100 token)→摘要→全文
- sp doctor 8 项数据治理检查与过期文档批量归档
- 可选自托管同步服务器（GitHub webhook + HMAC 校验 + 定时同步）

## 适用场景

- 让我的编程 agent 每次会话都带上团队决策与经验知识
- 在团队内以 Git 仓库共享和同步知识库
- 为 Claude Code 安装插件获得知识捕获与质量检查技能

## 场景标签

`知识库管理` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: **sp-context** is a CLI that gives any AI coding agent (Claude Code, Codex, Cursor, etc.) persistent access to your 
> L7: No vector database. No embeddings. No RAG pipeline. Just Git + BM25 + about 100 tokens per session for the catalog o

## 星数曲线

```mermaid
xychart-beta
    title "qiuyanxin/sp-context 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9138c881447b` · [字段定义](../../DATASET.md)*
