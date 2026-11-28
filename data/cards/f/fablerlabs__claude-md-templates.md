# fablerlabs/claude-md-templates

⭐ 10 · JavaScript · MIT · 推送 2026-07-29 · [GitHub](https://github.com/fablerlabs/claude-md-templates) · [官网](https://fablerlabs.com/guides) · 组织维护

**为 AI 编码 agent 提供 CLAUDE.md/AGENTS.md 模板与实例**

提供可复制的 CLAUDE.md 与 AGENTS.md 起始模板及四个已填充示例（Next.js SaaS、Python CLI、Rust 服务、自治 agent），配套字段指南与多 agent 并行的 fleet 模板；可经 Claude Code 插件安装以生成、评分、迁移规则文件。仓库由一个自治 AI agent 维护并公开运营，附带付费完整套件，仓库本身 MIT 许可。面向使用 Claude Code、Cursor 等 AI 编码工具的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CLAUDE.starter.md 与 AGENTS.starter.md 跨工具起始模板
- 四个已填充示例与字段指南 FIELD-GUIDE.md
- 三个 Claude Code 斜杠命令：生成、评分（0–100）、迁移 CLAUDE.md
- fleet/ 目录提供多 agent 会话编排模板

## 适用场景

- 为使用 Claude Code 或 Cursor 的项目快速建立 agent 规则文件
- 给现有 CLAUDE.md 做评分并按优先级修复
- 为无人值守自治 agent 编写章程与护栏
- 同时使用多种编码工具时统一到 AGENTS.md

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L12: Copy-paste **CLAUDE.md** / **AGENTS.md** starter templates and complete worked
> L17: A `CLAUDE.md` (or the tool-agnostic `AGENTS.md`) is the single highest-ROI file
> L29: ## What's here

## 星数曲线

```mermaid
xychart-beta
    title "fablerlabs/claude-md-templates 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `fcaf696e7439` · [字段定义](../../DATASET.md)*
