# lourencomaciel/sift-gateway

⭐ 32 · Python · MIT · 推送 2026-08-03 · [GitHub](https://github.com/lourencomaciel/sift-gateway) · [官网](https://pypi.org/project/sift-gateway/) · 个人维护

**AI 工具输出的可靠性网关：结构稳定、脱敏、分页完整的 JSON**

面向 MCP 客户端与 CLI agent 的输出可靠性层：代理上游 MCP 工具调用或 Shell 命令，将完整 JSON 持久化为 SQLite artifact，返回小结果（full）或带查询指引的引用（schema_ref），agent 可对存储数据运行 Python 代码做精确检索。提供显式分页续取契约（retrieval_status == COMPLETE）与默认开启的出站敏感信息脱敏。以 pipx 安装的 CLI 提供，支持 claude/cursor/vscode 等客户端配置初始化。README 报告 103 题基准结果。

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

- 上游工具输出持久化为 SQLite artifact，无损保留但不进入 prompt 上下文
- 对 artifact 运行 Python 代码查询，可跨整个分页链（scope=all_related）
- 显式分页续取与完成信号（pagination.retrieval_status == COMPLETE）
- 出站敏感信息脱敏默认开启

## 适用场景

- MCP 工具返回大 JSON 时避免撑爆上下文
- 确保 agent 在分页数据全部取完后才作答
- 对命令输出（如 kubectl）做可复现的 Python 精确分析
- 阻止工具输出中的敏感值回流到模型上下文

## 场景标签

 · 领域:AI agent 基础设施/工具网关

## 证据(README 行号)

> L9: Sift is a drop-in reliability layer for MCP and CLI tool output. It persists full payloads as artifacts, returns eit
> L17:   MCP tool call ──────────▶│                     │──────────▶ Upstream MCP server
> L56: - MCP: Sift is a reliability gateway for mirrored tool calls and artifact-based follow-up queries.

## 星数曲线

```mermaid
xychart-beta
    title "lourencomaciel/sift-gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1d2f13d4ce0a` · [字段定义](../../DATASET.md)*
