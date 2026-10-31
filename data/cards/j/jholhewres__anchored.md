# jholhewres/anchored

⭐ 13 · Go · MIT · 推送 2026-10-17 · [GitHub](https://github.com/jholhewres/anchored) · 个人维护

**供多种 AI 编码 agent 共享的本地持久记忆（单二进制 MCP 服务器）**

Go 编写的单二进制本地记忆存储，通过 MCP 协议让 Claude Code、Cursor、Codex、OpenCode、Gemini CLI 等工具读写同一记忆库。提供 BM25、本地多语言嵌入、实体与知识图谱的检索（85k 条记忆约 0.2s），会话开始时按 token 预算注入上下文，后台整理低信号记忆并提出合并与矛盾标记。支持通过自托管 Anchored OSS 实例做团队共享，默认数据不出本机。首次运行下载约 470MB 本地嵌入模型。

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

- MCP 服务器与 CLI 合一的单二进制，anchored init 可接入 15+ 个宿主工具
- BM25 + 本地多语言嵌入 + 知识图谱检索
- 按 token 预算注入项目上下文并统计节省量
- dream 流程提出记忆合并并标记矛盾供人工审核

## 适用场景

- 在多个编码 agent 工具间保持项目决策与上下文的持久记忆
- 团队通过自托管实例共享项目记忆
- 会话开始时自动获取项目近况以减少重复说明

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L14: A local memory your coding agents share. Claude Code, Cursor, Codex,
> L22: - **One store for every tool**: the MCP server and the CLI are one binary, and `anchored init` wires it into more t

## 星数曲线

```mermaid
xychart-beta
    title "jholhewres/anchored 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c5aeb1e613b5` · [字段定义](../../DATASET.md)*
