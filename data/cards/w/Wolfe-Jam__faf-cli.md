# Wolfe-Jam/faf-cli

⭐ 43 · TypeScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/Wolfe-Jam/faf-cli) · [官网](https://faf.one) · 个人维护

**为 AI 编码代理生成并版本化项目上下文文件的 CLI**

命令行工具，从仓库真实技术栈检测并生成单一 project.faf 文件（IANA 注册的 vnd.faf+yaml 格式），再导出为 AGENTS.md、CLAUDE.md、GEMINI.md、.cursorrules 及 Copilot 所读文件，随 git 版本化管理。以 33 个 Mk4 槽位对上下文完整度打分（Trophy 100% 为目标档），提供 pre-commit 钩子、语义 diff、HTML 渲染、.fafm 便携代理记忆与 .fafa agent 身份卡片等子命令。通过 bunx/npx/pnpm/brew 安装，也可编译为单文件二进制。

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

- 单一 .faf 文件导出 AGENTS.md/CLAUDE.md/GEMINI.md/.cursorrules 等多种代理上下文文件
- 33 槽位 always-33 评分引擎（Rust WASM 内核），Trophy 100% 目标档
- 上下文随 git 版本化：faf diff/log 与 pre-commit 回归防护钩子
- .fafm 便携代理记忆与 .fafa agent 身份卡片（A2A/MCP Server Card）

## 适用场景

- 为自己的仓库生成并持续同步 AI 编码代理的项目上下文文件
- 从任意 GitHub 仓库一键生成 .faf 上下文
- 在 CI 中用评分与钩子防止项目上下文退化

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: **One `.faf` file → `AGENTS.md` · `CLAUDE.md` · `GEMINI.md` · `.cursorrules`,
> L85: |`faf export`|Author `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`|

## 星数曲线

```mermaid
xychart-beta
    title "Wolfe-Jam/faf-cli 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-27 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `590b153006ea` · [字段定义](../../DATASET.md)*
