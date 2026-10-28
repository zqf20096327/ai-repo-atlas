# ClickHouse/alexeyprompts

⭐ 30 · HTML · NOASSERTION · 推送 2026-10-01 · [GitHub](https://github.com/ClickHouse/alexeyprompts) · [官网](https://clickhouse.com/blog/agentic-coding) · 组织维护

**用 ClickHouse 后端查看 Claude Code 会话历史的查看器**

由 ClickHouse 维护的 Claude Code 会话查看器：用 schema.sql 建库表，clickhouse-local 将 ~/.claude/projects 下的 .jsonl 会话上传至 ClickHouse（ReplacingMergeTree 去重），index.html 内嵌凭据直接在浏览器打开查询。支持 upload_incremental.sh 增量上传（适合 cron 定时与多机收集），可将 Codex 会话转换为 Claude Code 形状入库并在查看器中展示。README 提示会话含工具调用与文件片段等敏感信息，不建议公开分享。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- clickhouse-local 上传本地 .jsonl 会话到 ClickHouse（ReplacingMergeTree 去重，幂等）
- upload_incremental.sh 增量上传，支持多机收集与 cron 定时
- Codex 会话转换入库并折叠子代理线程为 sidechain
- 浏览器打开 index.html 即可用，可选用 Claude 运行分类脚本填充分类表

## 适用场景

- 在浏览器中查询和浏览自己的 Claude Code 会话历史
- 从多台机器收集会话并增量同步到 ClickHouse
- 同时归档查看 Codex 会话记录

## 场景标签

 · 领域:AI 开发工具/数据分析

## 证据(README 行号)

> L5: A viewer of Claude Code sessions with ClickHouse backend.
> L22: Upload your sessions:

## 星数曲线

```mermaid
xychart-beta
    title "ClickHouse/alexeyprompts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9cd0919ef09a` · [字段定义](../../DATASET.md)*
