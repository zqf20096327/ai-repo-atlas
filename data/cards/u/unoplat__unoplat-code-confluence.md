# unoplat/unoplat-code-confluence

⭐ 94 · Python · NOASSERTION · 推送 2026-10-07 · [GitHub](https://github.com/unoplat/unoplat-code-confluence) · [官网](https://docs.unoplat.io/) · 组织维护

**为代码仓库自动生成维护 AGENTS.md 的代码上下文引擎**

面向 AI 编码 agent 的代码上下文引擎：解析代码仓库，自动生成机器可读的 AGENTS.md 文件，涵盖工程工作流命令、业务逻辑与领域实体、入口点与 API 端点、外部依赖角色等结构化上下文，供编码 agent 用作精确事实来源。采用 Tree-sitter 模块化语法提取与框架感知解析，通过工作流编排器处理以保证可扩展与可审计；当前处于 alpha 阶段，支持 Python 与 TypeScript 代码库。附带可移植 agent skill，经 npx skills CLI 安装后可教兼容 agent 使用 ucc 命令行摄取仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自动生成并维护每仓库的 AGENTS.md（工程命令/业务逻辑/入口端点/依赖）
- Tree-sitter 模块化语法提取，支持可扩展的语言与框架感知解析
- 内置可移植 agent skill，兼容 agent 可经 npx skills CLI 安装
- 提供 ucc agent-md <repo_url> 单命令流程

## 适用场景

- 让 AI 编码 agent 在存量代码库中减少探索消耗、减少幻觉
- 多仓库场景下维护跨库依赖的统一上下文索引
- 为组织内私有系统生成 agent 可用的 onboard 文档

## 场景标签

 · 领域:开发者工具/代码上下文

## 证据(README 行号)

> L4:  Always keep your agents ready with all the context required per repository.
> L58: **What's in the demo:** automatic `AGENTS.md` generation per repo and an org index that gives any coding agent a pr
> L82: Auto-generates machine-readable `AGENTS.md` files per repo to give coding agents a **precise source of truth**:

## 星数曲线

```mermaid
xychart-beta
    title "unoplat/unoplat-code-confluence 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 93 --> 95
    line [94, 94]
```

2026-10-18 94 → 2026-10-27 94（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5a2b5add0ae8` · [字段定义](../../DATASET.md)*
