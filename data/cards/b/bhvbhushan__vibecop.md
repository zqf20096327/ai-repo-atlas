# bhvbhushan/vibecop

⭐ 57 · TypeScript · MIT · 推送 2026-04-08 · [GitHub](https://github.com/bhvbhushan/vibecop) · 个人维护

**面向 AI 编码时代的确定性代码质量检测工具包**

基于 ast-grep 的 tree-sitter AST 分析构建的 TypeScript/Node.js 静态检测工具，提供 35 个检测器，分质量/安全/正确性/测试四类，捕获 AI 编码代理常引入的问题（巨型函数、N+1 查询、不安全的 shell 执行、未固定版本的 LLM 模型名等）。无需 LLM，所有发现确定性可复现。可通过 PostToolUse hook 等方式集成进 Claude Code、Cursor、Codex 等 11 种 AI 编码工具，也可作为 MCP 服务器运行，另提供 GitHub Action PR 门禁与减少 token 消耗的上下文优化功能（Beta，需 bun 运行时）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 35 个确定性检测器（不依赖 LLM），基于 ast-grep AST 分析
- 集成 11 种 AI 编码工具（hook/rules/MCP 服务器三种方式）
- GitHub Action 用作 PR 质量门禁
- 上下文优化（Beta）：Claude Code 重读文件时以 AST 骨架替代，称可减少约 35% token

## 适用场景

- 在 Claude Code/Cursor 等 AI 编码工具中自动扫描每次编辑并让代理自纠
- CI 中用 GitHub Action 拦截 AI 生成代码的质量问题
- 作为 MCP 服务器向编码代理提供扫描与解释工具

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L9: AI code quality toolkit — deterministic linter for the AI coding era. 35 detectors catch the bugs AI agents introduc
> L11: Built on ast-grep for fast, tree-sitter-based AST analysis. No LLM required — every finding is deterministic and re
> L41: |**Claude Code**|PostToolUse hook|

## 星数曲线

```mermaid
xychart-beta
    title "bhvbhushan/vibecop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-26 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4c36cc50e789` · [字段定义](../../DATASET.md)*
