# Ikalus1988/MisakaNet

⭐ 567 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/Ikalus1988/MisakaNet) · [官网](https://misakanet.org) · 个人维护

**面向 AI 编码代理的 git 化失败教训记忆库，经 MCP 检索**

MisakaNet 是为 AI 编码代理提供的失败恢复知识层：每条教训是仓库中的 Markdown 文件，按 E0–E4 证据等级分级，经代码式评审后入库；检索默认用标准库 BM25，托管端点提供可关闭的语义回退（bge-m3 + Vectorize），本地无需向量数据库或服务器。通过 MCP server（本地 stdio 11 个工具、托管端点 8 个工具）、各客户端插件、Python 库或 GitHub Action 使用；无匹配时返回 no_match 与 intake 表单供提交新案例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1000+ 证据分级教训，E0 intake 到 E4 双客户端复用观测
- BM25 优先检索，托管端点提供可禁用的语义回退
- 多渠道接入：MCP server、Claude Code/Codex 插件、PyPI 库、GitHub Action
- 语料可下载引用，含版本化 bundle 与逐文件许可证

## 适用场景

- 编码代理遇到报错时先检索已有修复教训再行动
- 把 CI 失败自动匹配到最接近的教训并评论在 PR 上
- 向语料库提交新失败案例（intake）供后续代理复用

## 场景标签

`Agent 记忆` `编码 Agent` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L13: > MisakaNet is where that payment is kept: a git-backed **failure memory**. Every lesson is a Markdown
> L51: Every lesson is a Markdown file: reviewed like code, graded by evidence, retrieved with BM25 over the
> L58: |**Lessons**|failure-recovery knowledge base, open and auditable under `lessons/`|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `71079eb4a3b6` · [字段定义](../../DATASET.md)*
