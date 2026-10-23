# explorium-ai/vibeprospecting-plugin

⭐ 237 · Shell · MIT · 推送 2026-10-11 · [GitHub](https://github.com/explorium-ai/vibeprospecting-plugin) · [官网](https://www.vibeprospecting.ai) · 组织维护

**面向 AI agent 的 B2B 数据插件：搜索公司与联系人并建线索名单**

由 Explorium 构建的 GTM 数据插件，作为其 B2B 数据平台（1.5 亿公司、8 亿专业人士、50+ 数据源）的工作流层，可安装到 Claude Code、Claude Cowork、Claude Chat、OpenAI Codex、OpenClaw 等 agent 宿主。功能包括按属性筛选搜索公司与联系人、通过邮箱/LinkedIn URL 匹配到持久 ID、补全 CRM 记录缺失字段、按 ICP 条件构建线索与 ABM 名单并导出 CSV/JSON，以及查询招聘、融资等业务信号。通过各宿主的插件命令或 npx skills 安装，另提供独立 MCP 仓库与 Gemini CLI 扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按行业、规模、营收、技术栈等条件搜索公司与联系人
- 联系人/公司匹配到持久 Explorium ID 并补全字段
- 按 ICP 条件构建线索与 ABM 名单，导出 CSV/JSON
- 列出在 Anthropic 官方插件商店

## 适用场景

- 在 agent 内构建符合条件的潜在客户名单并导出
- 用邮箱或 LinkedIn URL 匹配并补全 CRM 记录
- 查询目标公司的招聘、融资等信号用于外联准备
- 清洗 CSV 名单：去重、匹配、补全后标准化导出

## 场景标签

 · 领域:B2B 销售/GTM 数据

## 证据(README 行号)

> L3: **Vibe Prospecting is a GTM data plugin for Claude Code, Claude Cowork, Claude Chat, OpenAI Codex, and OpenClaw that
> L45: Vibe Prospecting Plugin is a workflow layer for Explorium's B2B data platform. It lets users search companies, disc

## 星数曲线

```mermaid
xychart-beta
    title "explorium-ai/vibeprospecting-plugin 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23"]
    y-axis "stars" 195 --> 240
    line [198, 213, 230, 237]
```

2026-10-18 198 → 2026-10-23 237（+39）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0cc3ba33fe9a` · [字段定义](../../DATASET.md)*
