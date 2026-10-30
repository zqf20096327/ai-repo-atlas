# xChuCx/agent-memory

⭐ 15 · Go · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/xChuCx/agent-memory) · 个人维护

**面向 AI 编程 agent 的本地 git 化项目记忆（MCP+CLI）**

Go 编写的本地项目记忆服务，通过 MCP 协议（stdio JSON-RPC）向 Claude Code、Cursor、Codex、Gemini CLI 等编程 agent 提供三个工具：fetch_context 读取上下文包、propose_update 提交结构化记忆更新、status 报告健康状态。记忆以 Markdown 存于仓库内、git 同步，无云端与向量库；持久变更先 stage 供人工 review --diff 后 apply，写入前执行密钥/PII 扫描。提供完整 CLI，支持联邦只读知识库（如 arch-wiki）。安装方式为预编译二进制或 npx。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个 MCP 工具 + 完整 CLI，Markdown 为事实源、git 同步
- 持久变更 stage→review --diff→apply 人工审核门
- 写入前密钥/PII 扫描，支持分支感知与 section 级合并
- 联邦只读 landscape store（两层检索，来源+commit 标注）

## 适用场景

- 让 Claude Code/Cursor 等编程 agent 记住项目决策、约定与坑点
- 团队通过提交到仓库的 Markdown 共享 agent 记忆
- 接入 arch-wiki 等共享架构知识库供 agent 检索

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L15: Local, **git-native** project memory for AI coding agents. One MCP call in,
> L18: **No cloud, no vector DB** — Markdown is the source of truth and git is the
> L194: Exposed by `agent-memory mcp` over stdio JSON-RPC:

## 星数曲线

```mermaid
xychart-beta
    title "xChuCx/agent-memory 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d3611c2c6cb1` · [字段定义](../../DATASET.md)*
