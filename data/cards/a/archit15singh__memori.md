# archit15singh/memori

⭐ 25 · Rust · MIT · 推送 2026-09-19 · [GitHub](https://github.com/archit15singh/memori) · [官网](https://archit15singh.github.io/posts/2026-02-28-designing-cli-tools-for-ai-agents/) · 个人维护

**给 AI 编程 Agent 的持久记忆层：单文件 SQLite 混合检索**

面向 AI 编程 Agent 的持久记忆工具：以单个 SQLite 文件存储文本、384 维向量与元数据，提供 FTS5 全文 + 余弦向量经 Reciprocal Rank Fusion 融合的混合检索，附带访问加权衰减排序（约 69 天半衰期）与余弦相似度去重（阈值 0.92）。嵌入模型 fastembed AllMiniLM-L6-V2 随二进制分发，无需 API key、无云端与 LLM 依赖。提供 pip/cargo 安装与 CLI，可一条命令接入 Claude Code，其他可执行 shell 的 Agent（Cursor、Copilot CLI 等）亦可调用。另带只读 Web 仪表盘与 JSONL 导入导出。

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

- 单文件 SQLite 存储 + FTS5/向量混合检索（RRF 融合）
- 内置 fastembed 嵌入模型，无 API key、无网络依赖
- 访问加权衰减排序与余弦相似度自动去重
- memori setup 一条命令接入 Claude Code，--json/--raw 面向 Agent 管道

## 适用场景

- 让编程 Agent 跨会话记住调试结论与架构决策
- 会话开始时一键加载相关历史上下文
- 备份/迁移 Agent 积累的记忆库（JSONL 无损往返）

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L10: > Persistent memory for AI coding agents — Rust + SQLite + FTS5 + vector search in a single file.
> L12: AI agents forget everything between sessions. Memori gives them a persistent memory layer that accumulates knowledg
> L131: Memori is agent-agnostic — any tool that can shell out can use it. Cursor, Windsurf, Copilot CLI, Aider, Continue,

## 星数曲线

```mermaid
xychart-beta
    title "archit15singh/memori 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e37cfdb6363d` · [字段定义](../../DATASET.md)*
