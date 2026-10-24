# appboypov/pew-pew-plaza-packs

⭐ 87 · Shell · MIT · 推送 2026-01-12 · [GitHub](https://github.com/appboypov/pew-pew-plaza-packs) · [官网](https://pewpewprompts.com) · 组织维护

**面向 Claude Code 的模块化 AI 项目管理/提示词工程框架**

由 pewpewprompts.com 维护的 AI 项目管理框架：以提示词、agent、workflow、模板、上下文文档的模块化组装为核心，通过 curl 一键安装到任意现有项目的 .pew/ 目录，并同步到 .claude/ 使 Claude Code 中启用 /plx: 系列斜杠命令。核心机制包括 wikilink 引用体系（[[引用]] 动态加载、![[嵌入]] 内联内容）、按 YAML 配置的 sync 流程、persona/template/block/instruction 等可复用组件分类，以及覆盖 issue/story/epic/路线图等项目管理场景的模板集。仅针对 Claude Code 生态设计。

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

- curl 单命令将框架组件安装进任意现有项目的 .pew/ 目录
- wikilink 架构：[[引用]] 动态加载与 ![[嵌入]] 内容内联
- 模板/块/persona/agent/workflow/指令的模块化组件体系
- 同步后在 Claude Code 中启用 /plx: 系列斜杠命令（创建/转换/Git 发布等）

## 适用场景

- 为 Claude Code 项目搭建结构化的提示词与 agent 工作流
- 用可复用模板与块管理 issue、story、路线图等项目文档
- 通过 persona 与指令组件固化团队约定和最佳实践

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: > AI-powered project management framework based on an opinionated view on effective prompts and a highly modular app
> L21: 1. Download all framework components into `.pew/` subdirectories
> L274: ./.pew/scripts/claude-code/sync-claude-code.sh       # Sync to Claude Code

## 星数曲线

```mermaid
xychart-beta
    title "appboypov/pew-pew-plaza-packs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-18 87 → 2026-10-24 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b29c7f18ddcb` · [字段定义](../../DATASET.md)*
