# agentscope-ai/ReMe

⭐ 3,828 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/agentscope-ai/ReMe) · [官网](https://reme.agentscope.io/) · 组织维护 · 中文 README

**面向 AI agent 的本地文件式长期记忆管理工具包**

ReMe 将对话与资源转化为可读、可编辑、可检索的 Markdown 记忆文件（带 frontmatter 与 wikilink），按 capture→index→consolidate→recall 循环维护工作区。默认 BM25 检索，嵌入语义检索为可选并需额外配置；基础文件操作与搜索无需 LLM 凭据。通过 CLI、HTTP、MCP 或 Python API 供多种 agent 运行时共享同一本地工作区，并提供针对 DeepSeek Harness、OpenClaw、Claude Code、Codex 等的插件。需要 Python 3.11+，支持 pip、源码与 Docker 部署。

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

- 记忆以普通 Markdown 文件存储，用户可直接查看、编辑与备份
- BM25 + 可选 embeddings + wikilink 扩展的行级检索
- 提供 MCP、HTTP、CLI、Python API 四种接入方式
- 支持多模态记忆：图像随对话上下文入库并保留来源

## 适用场景

- 为个人助手或编码 agent 添加跨会话长期记忆
- 多个 agent 共享同一份本地知识工作区
- 让 agent 定期整理对话为新知识与摘要节点

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L24: 🧠 ReMe turns conversations and resources into readable, editable, searchable, and interconnected Markdown memory. A
> L35: - **One memory workspace works across agents.** Personal assistants, coding agents, and other agent runtimes can sh
> L208: ReMe can run as a local memory service accessed through the CLI, HTTP API, or MCP server, or it can be embedded in

## 星数曲线

```mermaid
xychart-beta
    title "agentscope-ai/ReMe 星数(近 27 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-22", "2026-11-23"]
    y-axis "stars" 3637 --> 3846
    line [3654, 3664, 3671, 3678, 3680, 3683, 3693, 3701, 3707, 3720, 3724, 3729, 3733, 3680, 3770, 3784, 3792, 3796, 3798, 3802, 3807, 3812, 3813, 3820, 3827, 3829, 3828]
```

2026-10-21 3,654 → 2026-11-23 3,828（+174）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `691ead6b458d` · [字段定义](../../DATASET.md)*
