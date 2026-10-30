# FlorianBruniaux/node-dep-scope

⭐ 19 · TypeScript · MIT · 推送 2026-09-01 · [GitHub](https://github.com/FlorianBruniaux/node-dep-scope) · 个人维护

**TS/JS 符号级依赖分析工具：标记原生替代并生成 LLM 迁移提示**

面向 TypeScript/JavaScript 项目的依赖分析 CLI 与 MCP 服务器：按符号级分析项目实际使用的依赖，输出 KEEP/REMOVE/RECODE_NATIVE 等判定，内置含 195 个包的原生替代数据库（含 e18e 微工具），支持重复依赖检测、传递依赖图分析与 monorepo workspace。可扫描 package.json/vitest/vite/next/storybook 等配置文件避免误判，并通过 MCP 服务器向 Claude Code、Cursor、Windsurf 提供 scan_project、generate_migration_prompt 等工具，在编辑器内生成迁移提示。需 Node.js >= 18 与 package.json 项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 符号级依赖分析与 195 包原生替代数据库（含 e18e）
- 重复依赖检测、传递依赖图分析与 monorepo workspace 支持
- MCP 服务器向 AI 编辑器提供 scan_project / generate_migration_prompt 等工具
- 自动扫描 vitest/vite/next/storybook 等配置文件减少误判

## 适用场景

- 审计遗留项目里可用原生 API 替代的依赖（如 lodash 函数）
- 合并多个功能重叠的库并生成上下文相关的重构提示
- 在 Claude Code / Cursor 等编辑器内直接查询依赖使用情况

## 场景标签

 · 领域:前端/开发工具

## 证据(README 行号)

> L14: **Symbol-level dependency analysis + LLM-ready migration prompts** for TypeScript/JavaScript projects.
> L156: dep-scope exposes a **Model Context Protocol server** so AI editors (Claude Code, Cursor, Windsurf) can query your

## 星数曲线

```mermaid
xychart-beta
    title "FlorianBruniaux/node-dep-scope 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3ade90412d40` · [字段定义](../../DATASET.md)*
