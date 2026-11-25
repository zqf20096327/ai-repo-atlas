# ClickHouse/loom

⭐ 197 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/ClickHouse/loom) · [官网](https://clickhouse.github.io/loom/) · 组织维护 · 中文 README

**为 AI agent 提供共享长期记忆、文档检索与代码索引的自托管服务**

ClickHouse 出品的开源自托管 MCP 服务器：让多个 agent 共享长期记忆，记忆关联到文件与符号，在 agent 读写代码时浮现；提供带引文的文档检索（支持 PDF/docx/pptx）、代码索引、任务收件箱与多用户命名空间/令牌控制。数据存于 ClickHouse，可选 Postgres。经 Docker 安装脚本或 Helm 部署，默认本地嵌入模型可无密钥启动，通过 Python/TypeScript SDK 或插件接入 Claude Code、Codex、Cursor、VS Code。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨 agent/跨会话的共享长期记忆，记忆链接到代码并随重构追踪
- 带引用来源的文档检索（RAG），支持 PDF/.docx/.pptx
- MCP server 及 Claude Code、Codex、Cursor、VS Code 插件，Python/TypeScript SDK
- 自托管：Docker 安装脚本或 Kubernetes Helm chart，数据存于 ClickHouse

## 适用场景

- 让团队多个编码 agent 共享跨会话的经验与项目上下文
- 为自己的 agent 应用添加按用户的长期记忆
- 对仓库建立代码索引供 agent 查询定义、调用方与变更影响
- 多 agent 工作流中通过任务收件箱交接工作并保留审计记录

## 场景标签

`Agent 记忆` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L26: Loom is an open-source, self-hosted MCP server that gives your agents long-term, shared
> L31: Agents connect through MCP, HTTP, Python or TypeScript. Self-host with Docker or
> L46: - **A multi-user MCP memory server** with namespaces, roles and tokens.

## 星数曲线

```mermaid
xychart-beta
    title "ClickHouse/loom 星数(近 13 点)"
    x-axis ["2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 0 --> 216
    line [5, 8, 16, 55, 103, 135, 149, 166, 167, 173, 179, 191, 197]
```

2026-11-11 5 → 2026-11-25 197（+192）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `b5e396e1bed5` · [字段定义](../../DATASET.md)*
