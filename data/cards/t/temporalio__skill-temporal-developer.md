# temporalio/skill-temporal-developer

⭐ 235 · MIT · 推送 2026-10-23 · [GitHub](https://github.com/temporalio/skill-temporal-developer) · [官网](https://temporal.io/) · 组织维护

**面向编码代理的 Temporal 开发技能包（SKILL 知识资产）**

由 Temporal 官方（temporalio）维护的开发技能包：为 Claude Code、Cursor、OpenAI Codex 等编码代理提供构建 Temporal 应用所需的领域知识与指引。可作为插件安装（三个专属插件仓库），也可通过 npx skills 或手动 git clone 到 ~/.claude/skills 等目录直接安装。内容覆盖 7 种已支持的 Temporal SDK 语言（Python/TypeScript/Go/Java/.NET/Rust/Ruby），PHP 尚在开发中（未完成）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 打包为 Claude Code / Cursor / Codex 三种编码代理插件
- 支持 npx skills add 命令行安装与手动 git clone 安装
- 覆盖 7 种 Temporal SDK 语言（Rust 处于 Public Preview，PHP 进行中）

## 适用场景

- 让编码代理在开发 Temporal 应用时获得官方领域知识
- 为团队统一各编码代理的 Temporal 开发指引

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A comprehensive skill for developers to use when building Temporal applications.
> L11: This skill is packaged as a plugin for major coding agents, which provides a simple way to install and receive futu
> L25: 1. `npx skills add temporalio/skill-temporal-developer`

## 星数曲线

```mermaid
xychart-beta
    title "temporalio/skill-temporal-developer 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-24"]
    y-axis "stars" 231 --> 236
    line [232, 233, 235, 235]
```

2026-10-18 232 → 2026-10-24 235（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `704fd93fb30d` · [字段定义](../../DATASET.md)*
