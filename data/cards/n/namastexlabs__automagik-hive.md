# namastexlabs/automagik-hive

⭐ 24 · Python · MIT · 推送 2025-12-17 · [GitHub](https://github.com/namastexlabs/automagik-hive) · [官网](https://deepwiki.com/namastexlabs/automagik-hive) · 组织维护

**为 Agno agent 框架提供项目脚手架与智能 CSV RAG 的生成工具**

基于 Agno 框架的脚手架层工具：通过 hive init 生成约定式 ai/ 项目结构，用 YAML 声明式配置定义 agent、团队与工作流，并内置一个 meta-agent 从自然语言需求生成配置（从 7+ 提供商中推荐模型）。知识库部分提供基于哈希的 CSV 增量加载（仅重嵌入变更行）。支持 PostgreSQL/PgVector 与 SQLite 后端、热重载开发服务器与自动生成 API。面向使用 Python 3.11+ 的开发者，需至少一个 AI 提供商 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言需求经 meta-agent 生成 agent YAML 配置
- 基于哈希的 CSV 增量 RAG 加载（仅重嵌入变更行）
- YAML 声明式配置与 hive init 项目脚手架、热重载开发服务器
- 支持 PostgreSQL/PgVector（混合搜索、HNSW）与 SQLite 双后端

## 适用场景

- 快速搭建 Agno agent 项目而无需手写 Python 样板
- 用 CSV FAQ 数据构建带增量更新的知识库 agent
- 从自然语言描述生成 agent 配置与模型/工具推荐

## 场景标签

`Agent 框架` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L18: **Hive doesn't compete with Agno - it makes it easier to use.**
> L27: **Built by practitioners** who got tired of manually setting up the same patterns. Powered entirely by Agno.
> L344: Like Create React App for React, Hive removes setup friction without replacing the framework.

## 星数曲线

```mermaid
xychart-beta
    title "namastexlabs/automagik-hive 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `9e1b959d238a` · [字段定义](../../DATASET.md)*
