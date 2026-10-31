# seaguntech/ui

⭐ 15 · TypeScript · MIT · 推送 2026-03-13 · [GitHub](https://github.com/seaguntech/ui) · [官网](https://ui.seaguntech.com) · 组织维护

**面向 Seaguntech 的开源 UI 组件库与组件注册表**

基于 shadcn/ui 之上构建的组件库与自定义注册表，发布三个公开包：design-system 提供 Tailwind v4 令牌、主题与基础样式；ui 提供 React 组件；cli 提供从 Seaguntech 注册表拉取组件的命令行工具。消费者可经 pnpm 安装组件包或用 CLI 按需添加组件；文档站点同时托管注册表 JSON（/r/*.json）。本地开发要求 Node.js >=20 与 pnpm 10.25.0。README 未描述 AI 相关功能，仅仓库主题标签含 ai。

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

- 三个公开包：design-system（Tailwind v4 令牌/主题）、ui（React 组件）、cli（组件拉取）
- CLI 支持从 Seaguntech 注册表按需添加组件
- 文档站点托管注册表 JSON（/r/*.json）并提供构建/校验命令

## 适用场景

- 在 React 项目中使用 Seaguntech 风格的 UI 组件与主题
- 通过 CLI 从注册表按需拉取单个组件
- 基于该体系构建并发布自己的组件注册表

## 场景标签

 · 领域:前端/设计系统

## 证据(README 行号)

> L5: - `@seaguntech/design-system`: Tailwind v4 tokens, themes, and base styles.
> L6: - `@seaguntech/ui`: reusable React UI components.

## 星数曲线

```mermaid
xychart-beta
    title "seaguntech/ui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 low · 依据 README sha `2c6a5bc0027a` · [字段定义](../../DATASET.md)*
