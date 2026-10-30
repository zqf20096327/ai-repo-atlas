# kombohq/company-brain

⭐ 27 · TypeScript · MIT · 推送 2026-07-08 · [GitHub](https://github.com/kombohq/company-brain) · [官网](https://github.com/kombohq/company-brain/blob/main/docs/getting-started.md) · 组织维护

**将公司数据源同步为 Markdown 存入 Git 的模板，供 AI 编程代理检索**

一个 TypeScript 仓库模板：各数据源在 src/connectors 下有同步脚本，把 Notion、Zendesk、Granola 等来源的数据写为 context/ 目录下的 Markdown，由 GitHub Actions 定时运行并提交回仓库；AI 编程代理通过读取 AGENTS.md 与 .agents/skills/ 技能了解仓库内容并用 grep 等方式检索。全部基于 Bun 运行，无构建步骤；要求仓库保持私有，自动提交工作流拒绝在公开仓库运行。

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

- 连接器将 Notion/Zendesk/Granola 等来源数据写为 agent 友好的 Markdown
- GitHub Actions 定时同步并提交，数据以主分支为唯一事实来源
- 技能通过 .claude/.codex/.cursor 符号链接共享给各代理工具
- 全部基于 Bun 运行，无构建步骤

## 适用场景

- 为公司 AI 编程代理构建可 grep 的长期知识库
- 把 CRM、工单、会议记录等多源数据合并为统一上下文
- 在不引入新服务的前提下让 Cursor/Claude 读取公司业务数据

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L11: The idea is simple: instead of giving an agent a pile of MCP servers and hoping it searches them well, you **pull t
> L35: - Each **data source** has a small sync script under `src/connectors/ /` that fetches data and writes it into `cont

## 星数曲线

```mermaid
xychart-beta
    title "kombohq/company-brain 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-30 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c5346d8b5870` · [字段定义](../../DATASET.md)*
