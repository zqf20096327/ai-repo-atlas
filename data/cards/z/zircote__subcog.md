# zircote/subcog

⭐ 29 · Rust · MIT · 推送 2026-08-03 · [GitHub](https://github.com/zircote/subcog) · 个人维护

**给 AI 编程助手的持久记忆系统：捕获并按需召回会话上下文**

用 Rust 编写的单二进制持久记忆系统，面向使用 AI 编程助手的开发者：以 CLI 和 MCP server 两种形式提供约 22 个工具，捕获编码会话中的决策、经验与上下文，存入 SQLite（FTS5 全文索引 + usearch HNSW 向量），支持 BM25+向量 RRF 融合的混合检索与知识图谱。内置 Claude Code 插件（覆盖 5 个 hooks），LLM 相关功能（隐式捕获、摘要合并）需自行提供 provider。另有按项目/分支/文件路径的分面过滤、分支 GC、密钥检测与 PII 过滤。安装途径含 Cargo、Homebrew、Docker、二进制与 npm。

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

- 单二进制（<100MB，冷启动 <10ms），SQLite/FTS5/usearch 三层存储架构
- BM25+向量混合检索（RRF 融合），all-MiniLM-L6-v2 本地生成 384 维嵌入
- MCP server 提供 ~22 个工具，覆盖 Claude Code 全部 5 个 hooks
- stdio/HTTP 双传输模式，支持 JWT 认证、静态加密与 GDPR 导出

## 适用场景

- 给 Claude Code 等 AI 编程助手接上跨会话记忆，开工时自动注入相关上下文
- 按项目、分支、文件路径检索团队历史决策与经验
- 本地或团队环境以 MCP server 方式为多个 agent 共享记忆库

## 场景标签

 · 领域:开发者工具/AI 记忆基础设施

## 证据(README 行号)

> L21: - **MCP server integration** for AI agent interoperability
> L106: ## MCP Server
> L199: ## Claude Code Hooks

## 星数曲线

```mermaid
xychart-beta
    title "zircote/subcog 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2043b714a7e0` · [字段定义](../../DATASET.md)*
