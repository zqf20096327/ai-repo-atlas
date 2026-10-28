# Query-farm/openprompt

⭐ 62 · C++ · MIT · 推送 2026-10-22 · [GitHub](https://github.com/Query-farm/openprompt) · [官网](https://duckdb.org/community_extensions/extensions/open_prompt.html) · 组织维护

**在 SQL 中调用 LLM 的 DuckDB 社区扩展**

DuckDB 社区扩展 open_prompt：提供 open_prompt() SQL 函数，向兼容 /v1/chat/completions 的 OpenAI 风格 API 端点（如 Ollama/OpenAI 等）发送提示并取回补全结果。配置项包括 API URL、可选鉴权 token、模型名与超时，可通过 SET VARIABLE、环境变量或 DuckDB SECRETS 持久化设置；支持基于 schema 的 JSON 结构化输出（小模型走 system_prompt 尽力模式）。面向使用 DuckDB 的开发者，README 标注为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- open_prompt() SQL 函数直接查询补全 API 端点
- 兼容 /v1/chat/completions 的端点（Ollama/OpenAI 等）
- SET VARIABLE / 环境变量 / DuckDB SECRETS 三种配置方式
- 支持 schema 驱动的 JSON 结构化输出

## 适用场景

- 在 DuckDB 查询流程中直接调用 LLM 生成文本
- 配合本地 Ollama 在 SQL 里做批量提示推理
- 以 JSON schema 约束模型输出结构化数据

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L1: # DuckDB Open Prompt Extension
> L2: Simple extension to query OpenAI Completion API endpoints such as Ollama/OpenAI/etc
> L13: - `open_prompt(prompt)`

## 星数曲线

```mermaid
xychart-beta
    title "Query-farm/openprompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-28 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `976b6d253f05` · [字段定义](../../DATASET.md)*
