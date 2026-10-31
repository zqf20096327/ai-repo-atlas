# hskl18/boring-agent-memory

⭐ 20 · Python · MIT · 推送 2026-07-14 · [GitHub](https://github.com/hskl18/boring-agent-memory) · 个人维护

**给 AI agent 的本地文件 BM25 记忆召回层，附来源引用**

面向 agent 工作流的本地记忆召回基础设施：索引用户显式指定的可信文件（文档、runbook、ADR、bug 日志等），用 SQLite FTS5/BM25 排序，通过 memory_query() Python API、CLI 与 JSON-lines stdio 接口返回 source_path、行号引用与片段。支持哈希增量更新、秘密模式脱敏、过期检测与确定性评测夹具。不自动捕获对话，不依赖托管服务或嵌入 API；语义检索仅作为可选适配器。

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

- SQLite FTS5/BM25 索引可信本地文件，返回来源路径与行级引用
- 哈希增量更新与 dry-run 预览，索引变更可复现
- 索引前脱敏常见密钥模式并默认跳过 .env、密钥文件等路径
- 提供 CLI、Python API、JSON-lines stdio 三种接口与确定性评测夹具

## 适用场景

- 让编码 agent 召回项目规范与 ADR 决策
- 运维 agent 从本地 runbook 查规则而不全部载入上下文
- 把用户偏好与工作流规则放在版本控制的文档里供 agent 检索

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: It indexes canonical docs, skills, runbooks, bug logs, ADRs, ledgers, and sanitized reports with SQLite FTS5/BM25, 
> L65: - Provides CLI, Python API, and JSON-lines stdio interfaces.

## 星数曲线

```mermaid
xychart-beta
    title "hskl18/boring-agent-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5db948331864` · [字段定义](../../DATASET.md)*
