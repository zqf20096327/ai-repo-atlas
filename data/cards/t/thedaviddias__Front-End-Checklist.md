# thedaviddias/Front-End-Checklist

⭐ 74,497 · MDX · MIT · 推送 2026-10-06 · [GitHub](https://github.com/thedaviddias/Front-End-Checklist) · [官网](https://frontendchecklist.io) · 个人维护

**为开发者与 AI agent 提供前端质量检查清单与规则库**

将前端最佳实践整理为 386 条规则、11 个类别的检查清单，覆盖 HTML、CSS、JavaScript、性能、可访问性、SEO、安全等，每条规则按 Critical/High/Medium/Low 分级。提供三种使用路径：网站在线浏览与筛选、MCP 服务器（托管端点与本地 stdio 服务器，暴露 11 个工具如 review_code、audit_url、search_rules）供 agent 做代码审查与 URL 审计，以及 npx 安装的 skills 形式审计工作流。规则贡献通过 pnpm 脚本本地开发与校验。

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

## 动量与使用信号

- 维护:`active` — 距上次 push 11.8 天,年发版 1,112 位贡献者
- 涨星:近 1 天 **+12**(自 20261016 起算)
- 安装:npm 包 `skills` 月下载 23,786,800
- 平台:— · 协议:MCP

## 能力要点

- 386 条规则覆盖 11 个活跃类别，按四级优先级标注
- 托管 MCP 服务器暴露 11 个工具，支持代码审查与公开 URL 审计
- 提供 npx 安装的 skills 形式审计工作流（如 https 专项）
- 规则页含解释、修复指引、验证步骤与 AI prompts

## 适用场景

- 上线前按类别逐项审计前端项目的可访问性、SEO 与安全
- 让支持 MCP 的 agent 对组件代码或公开页面做前端质量审查
- 代码评审时按优先级核对清单项

## 场景标签

`代码审查` `精选清单` · 领域:编码与开发

## 证据(README 行号)

> L11: Front-End Checklist is the open-source front-end quality system for humans and AI agents. It turns front-end best p
> L27: - `11` MCP tools exposed by the hosted server
> L66: Connect an MCP-capable agent to Front-End Checklist for frontend code review, structured rule lookup, audits, and r

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `8f524cf13d0f` · [字段定义](../../DATASET.md)*
