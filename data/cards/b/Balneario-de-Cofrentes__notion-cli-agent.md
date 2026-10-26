# Balneario-de-Cofrentes/notion-cli-agent

⭐ 90 · TypeScript · MIT · 推送 2026-09-09 · [GitHub](https://github.com/Balneario-de-Cofrentes/notion-cli-agent) · [官网](https://www.npmjs.com/package/notion-cli-agent) · 个人维护

**供 AI agent 调用的 Notion 命令行工具：读写工作区与批量操作**

面向 AI agent 优先设计的 Notion CLI，也可供人使用：通过自然语言查询转 Notion 过滤器（notion find）、批量执行多操作（notion batch）、--llm 紧凑输出模式、生成数据库专属 agent 提示词、页面摘要与结构化数据抽取。另含 Obsidian 双向同步、CSV/Markdown 导入、备份、数据库校验/健康检查、模板与关系图等功能。以 npm 全局安装提供，需 Node.js 22.12+ 与 Notion 集成令牌；仓库附 AgentSkills 兼容技能文件，工作区同步后可用数据库名替代 UUID。

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

- 自然语言查询转 Notion 过滤器（notion find，支持英/西语模式）
- --llm 紧凑输出模式与批量操作（get/create/update/delete/query/append）
- 附 AgentSkills 兼容技能文件与 workspace onboarding 映射
- Obsidian 双向同步、备份到 JSON/Markdown、数据库校验与健康评分

## 适用场景

- 让 AI agent 读写 Notion 工作区并执行批量任务
- 把 Notion 数据库导出到 Obsidian 或反向导入笔记
- 对 Notion 数据库做备份、查重与数据质量校验

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L8: notion-cli-agent is designed to be used by AI agents that need to read and write Notion workspaces — natural languag
> L40: - **`--llm` mode** — compact, structured output optimized for agent consumption

## 星数曲线

```mermaid
xychart-beta
    title "Balneario-de-Cofrentes/notion-cli-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 89 --> 91
    line [90, 90]
```

2026-10-18 90 → 2026-10-26 90（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `e1921d7af2f7` · [字段定义](../../DATASET.md)*
