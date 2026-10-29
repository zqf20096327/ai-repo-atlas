# molecule-dev/molecule

⭐ 44 · TypeScript · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/molecule-dev/molecule) · [官网](https://www.molecule.dev/) · 组织维护

**AI 可正确组装的开源全栈 TypeScript 包生态与脚手架工具**

提供 1,000+ 个 Apache-2.0 的 @molecule/* npm 包，覆盖数据库、认证、支付、邮件、AI、分析等 80+ 类后端与前端关注点；所有 provider 位于抽象接口之后，通过 bond 在启动时注入，换数据库或框架只需改一行 import。配套工具包括 molecule.dev 在线 IDE 的 Synthase agent（描述应用即生成完整 TypeScript 项目）、mlcl CLI 与 molecule MCP server，供 AI 编码 agent 调用。生成项目可随时导出代码、数据库 dump 与 .env 在任意环境运行。当前仅支持 TypeScript/Node。

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

- 1,000+ Apache-2.0 npm 包，核心接口+bond 实现的 provider 可换架构
- Synthase / mlcl CLI / molecule MCP server 三种组装方式
- 生成代码经类型检查、lint 与单元/集成/E2E 测试
- 一键导出项目代码、数据库 dump 与 .env 文件

## 适用场景

- 通过描述应用让 AI agent 生成可导出的全栈 TypeScript 项目
- 在 PostgreSQL/MySQL/SQLite 等供应商之间一行切换
- 为 AI 编码 agent 提供结构化工具与 AGENTS.md 约定

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L12: - **What it is.** An AI-first, open-source ecosystem of 1,000+ composable `@molecule/*` packages (Apache-2.0, on np
> L20: - **If you are an AI agent.** Read a package's `README.md` (generated from its source), call the core interface and
> L120: For AI agents: `npx mlcl mcp install` registers the molecule MCP server (search, scaffold, add, swap, deploy, mana

## 星数曲线

```mermaid
xychart-beta
    title "molecule-dev/molecule 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `297b12c5e978` · [字段定义](../../DATASET.md)*
