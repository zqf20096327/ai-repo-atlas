# agentscope-ai/ReMe

⭐ 3,842 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/agentscope-ai/ReMe) · [官网](https://reme.agentscope.io/) · 组织维护 · 中文 README

**为 AI agent 提供本地文件式记忆管理的工具包**

ReMe 将对话与资源转化为 Markdown 形式的记忆文件（含 frontmatter 与 wikilink），供多个 agent 运行时（QwenPaw、DeepSeek Harness、Claude Code、Codex 等）共享同一本地工作区进行检索、维护与演化。核心机制包括 capture→index→consolidate→recall 生命周期、BM25 与可选嵌入检索、auto_memory/auto_dream 等后台任务，以及事件/cron 触发的 Proactive Runtime。通过 CLI、HTTP、MCP 或 Python API 接入，支持 pip、源码与 Docker 安装；嵌入检索默认关闭，需显式在配置中启用。

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

- 记忆以普通 Markdown 文件存储，用户与 agent 均可直接编辑、备份
- BM25、可选嵌入与 wikilink 扩展实现行级上下文检索
- capture→index→consolidate→recall 记忆生命周期（auto_memory/auto_index/auto_dream）
- 通过 SKILL.md、CLI、HTTP、MCP、Python API 接入多种 agent 运行时

## 适用场景

- 为多个 agent 提供共享的长期记忆工作区
- 让 agent 自动沉淀对话事实并按日程整理知识
- 为编码助手或个人助理添加自动回忆与对话记录能力

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L16:  A local-first, self-evolving personal knowledge base for AI agents.
> L202: ReMe can run as a local memory service accessed through the CLI, HTTP API, or MCP server, or it can be embedded in
> L206: |Agent|Recommended path|Available after integration|

## 星数曲线

```mermaid
xychart-beta
    title "agentscope-ai/ReMe 星数(近 26 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 3662 --> 3858
    line [3678, 3680, 3683, 3693, 3701, 3707, 3720, 3724, 3729, 3733, 3680, 3770, 3784, 3792, 3796, 3798, 3802, 3807, 3812, 3813, 3820, 3827, 3829, 3828, 3832, 3842]
```

2026-10-24 3,678 → 2026-11-26 3,842（+164）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `f0ce450e2ae5` · [字段定义](../../DATASET.md)*
