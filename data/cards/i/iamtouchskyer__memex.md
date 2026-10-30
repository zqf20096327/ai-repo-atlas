# iamtouchskyer/memex

⭐ 144 · TypeScript · MIT · 推送 2026-09-08 · [GitHub](https://github.com/iamtouchskyer/memex) · [官网](https://memra.vercel.app) · 个人维护 · 中文 README

**AI 编程 agent 的持久记忆系统，跨会话保存知识卡片**

基于 Zettelkasten 方法为 AI 编程 agent 提供跨会话持久记忆：任务完成后将洞察保存为带双向链接的原子 markdown 知识卡片，下次会话开始前自动回顾相关卡片。不使用向量数据库与 embedding，卡片以 markdown 存于 ~/.memex/cards/，各平台共享同一目录，可通过 git 同步（支持 GitHub/GitLab）。以 MCP Server 或插件形式接入 Claude Code、VS Code Copilot、Cursor、Codex、Windsurf 等客户端，另提供 CLI 与本地可视化时间线。多数平台需 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Zettelkasten 原子知识卡片 + [[双向链接]]，无向量数据库/embedding
- 以 MCP Server（12 工具）或插件接入 Claude Code、Cursor、Codex 等多平台
- 各平台共享 ~/.memex/cards/ 目录，支持 git 跨设备同步
- CLI 与 memex serve 提供卡片搜索、读写与可视化时间线/图谱视图

## 适用场景

- 让 AI 编程 agent 跨会话记住项目知识与经验
- 在多个编辑器/AI 客户端间共享同一份记忆卡片库
- 用 git 同步知识卡片并在本地可视化浏览

## 场景标签

`Agent 记忆` `知识库管理` · 领域:Agent 开发

## 证据(README 行号)

> L5: Persistent memory for AI coding agents. Your agent remembers what it learned across sessions.
> L15: No vector database, no embeddings — just markdown files your agent (and you) can read.
> L27: |**Any MCP client**|MCP Server|12 MCP tools, zero config|

## 星数曲线

```mermaid
xychart-beta
    title "iamtouchskyer/memex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 143 --> 145
    line [144, 144]
```

2026-10-18 144 → 2026-10-30 144（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `10cb7f67d7d4` · [字段定义](../../DATASET.md)*
