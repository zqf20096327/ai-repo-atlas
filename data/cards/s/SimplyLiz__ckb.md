# SimplyLiz/ckb

⭐ 111 · Go · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/SimplyLiz/ckb) · [官网](https://github.com/SimplyLiz/CodeMCP/wiki) · 个人维护

**把代码库变成可查询知识库的 MCP 服务，供 AI 助手做代码导航与影响分析**

CKB 将代码库转化为可查询的知识库，通过 SCIP 索引与 tree-sitter 解析提供符号导航、调用图、影响分析（blast radius 与风险评分）、死代码检测、所有权查询与密钥扫描等能力。开发者可通过 CLI、HTTP API 和 MCP 三种方式使用，MCP 可接入 Claude Code、Cursor、Windsurf、VS Code、Grok 等 AI 编码工具，并提供 110+ 工具与 preset 机制减少 token 消耗。语言支持分四个层级：Go 为 Tier 1 且增量索引仅限 Go，C/C++ 需 compile_commands.json。可通过 npm、Homebrew 或 Go 源码构建安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SCIP 索引驱动的符号导航、调用图与影响分析（含风险评分）
- MCP/CLI/HTTP API 三种使用方式，支持 Claude Code、Cursor、Windsurf 等工具
- preset 机制按需加载工具集，降低 token 开销
- 21 项质量检查的 PR 审查模式，可在无 LLM 的 CI 中运行

## 适用场景

- 让 AI 编码助手精确回答改动影响范围与调用关系
- PR 审查时自动检查密钥泄露、破坏性变更与死代码
- 查询代码所有权、推荐 reviewer 并检测漂移
- 通过 CLI 或 HTTP API 在脚本与 CI/CD 中查询代码结构

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L12: CKB transforms your codebase into a queryable knowledge base. Ask questions, understand impact, find owners, detect
> L44: 🔗 **Integrate** — CLI, HTTP API, MCP for AI tools, CI/CD pipelines, custom scripts
> L294: ## MCP Integration
> L296: CKB works with any MCP-compatible AI coding tool.

## 星数曲线

```mermaid
xychart-beta
    title "SimplyLiz/ckb 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 109 --> 112
    line [110, 111, 111]
```

2026-10-18 110 → 2026-10-28 111（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `aff1dcadb9b1` · [字段定义](../../DATASET.md)*
