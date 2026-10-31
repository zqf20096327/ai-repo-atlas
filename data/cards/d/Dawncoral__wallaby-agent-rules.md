# Dawncoral/wallaby-agent-rules

⭐ 14 · Python · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/Dawncoral/wallaby-agent-rules) · 个人维护 · 中文 README

**给 AI 编码工具的文件式长期记忆与项目地图系统**

面向任意 AI 编码工具（Claude Code、Codex、Cursor、Copilot、Gemini CLI 等）的文件式记忆系统：通过两段粘贴式提示词和五个 Markdown 文件（AGENTS.md/CLAUDE.md 入口、MEMORY.md 事实记忆、NOW.md 当前状态、INDEX.md 项目地图）让 AI 每次会话读取记忆。配套零依赖 Python 脚本做每周健康检查与对账审计，另有可选治理 CLI（变更传导、前提检查、矛盾历史）与可安装的 Hermes 技能包。无向量库、无服务依赖，内容均为可 git diff 的纯文本。附带推广其自家 OpenAI 兼容 API 中转服务 wallabytoken.com。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个粘贴式提示词 + 五个纯文本文件即可为任意 AI 编码工具建立长期记忆
- 零依赖健康检查脚本（十项扫描）与对账审计脚本
- 变更传导/前提检查/矛盾历史的治理 CLI
- 前两周信任构建模式：新记忆需人工批准后转正

## 适用场景

- 我的 AI 编码助手隔几周就忘记之前定下的决策，想给它持久记忆
- 希望随时查找项目文件与当前状态，而不是反复搜索
- 团队交接项目时留下结构化的记忆、日志与失败记录

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: wallaby-agent-rules — long-term memory and a project map for any AI coding tool
> L93: No plugin, no MCP server, no install — the entry file is the integration. Each tool reads its own; the setup interv
> L115: Everything is plain Markdown you can read, `git diff`, and edit. No vector store, no service, no lock-in.

## 星数曲线

```mermaid
xychart-beta
    title "Dawncoral/wallaby-agent-rules 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `46f4bb6260cc` · [字段定义](../../DATASET.md)*
