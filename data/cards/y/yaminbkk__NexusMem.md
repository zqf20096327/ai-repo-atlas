# yaminbkk/NexusMem

⭐ 15 · TypeScript · MIT · 推送 2026-09-27 · [GitHub](https://github.com/yaminbkk/NexusMem) · [官网](https://nexus-mem.vercel.app) · 个人维护

**把 shell 历史、git 与文档索引进本地 SQLite 的 MCP 记忆服务器**

面向编码 agent 的本地记忆层：将 shell 命令及退出码、git 提交与 diff、项目文档、可选的助手会话与 GitHub 议题索引进本地 SQLite，按 token 预算返回排序切片。检索用 BM25(FTS5)，Ollama 可用时叠加 sqlite-vec 向量检索并以 RRF 融合；查询路径无模型调用，数据全部留在磁盘。以 npx CLI 提供，可安装 shell hook 与 Claude Code hook，要求 Node 22+ 和 git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 索引 shell 命令与真实退出码、git diff、文档至本地 SQLite
- BM25 + 可选向量检索经 RRF 融合，输出 token 预算内的排序切片
- 失败→修复链：将非零退出命令与其后续修复命令关联
- MCP 服务器形式供编码 agent 查询，全程本地、无云端无遥测

## 适用场景

- 让编码 agent 查到我之前试过但失败的命令及其修复
- 跨会话保留 shell 历史这类终端滚动即失的信息
- 按 token 预算向 agent 提供带出处的项目历史上下文

## 场景标签

`Agent 记忆` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L16: NexusMem records what actually happened on your machine (shell commands and their exit codes, git
> L19: serves back a ranked, token-budgeted slice of it on demand. Everything stays on disk. No account, no
> L175: section compete on equal terms. Retrieval runs BM25 over FTS5 and, if an embedding model is

## 星数曲线

```mermaid
xychart-beta
    title "yaminbkk/NexusMem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9a1dc6ec1af0` · [字段定义](../../DATASET.md)*
