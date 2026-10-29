# shidesheng0218/repo-ready

⭐ 28 · JavaScript · MIT · 推送 2026-07-06 · [GitHub](https://github.com/shidesheng0218/repo-ready) · [官网](https://www.npmjs.com/package/@shidesheng0218/repo-ready) · 个人维护 · 中文 README

**检查仓库是否适合 AI 编程代理协作的 CLI 工具**

CLI 优先的 AI 编程代理就绪度检查与修复工具：静态扫描仓库，检查代理指令文件（AGENTS.md/CLAUDE.md/.cursor/rules）、验证命令、README 质量、CI、上下文质量与危险脚本等区域，输出 0-100 评分及信号依据，并生成分为安全自动/需审查/仅手动的修复计划，可创建 Fix PR。默认完全离线、不执行仓库脚本、不上传源码；AI 增强为可选项（需 OPENAI_API_KEY 或 ANTHROPIC_API_KEY）。提供 GitHub Action 集成与可选自托管 Web 报告。

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

- 静态扫描输出评分与证据链，不执行仓库脚本
- 修复计划按安全自动/需审查/仅手动分组，支持 --dry-run 与 Fix PR
- 默认离线无 AI API key，AI 增强可选且仅发送元数据
- 提供 GitHub Action 与可选自托管 Web 报告（badge/分享卡）

## 适用场景

- 在引入 Codex/Claude Code/Cursor 前检查仓库就绪度
- 生成并执行可审查的仓库修复计划（补 AGENTS.md、README 等）
- 在 CI 中以评分门禁拦截仓库质量回退

## 场景标签

 · 领域:开发者工具/代码质量

## 证据(README 行号)

> L10: > **Make your repo ready for Codex, Claude Code, Cursor, and contributors.**
> L20: RepoReady is a **CLI-first AI coding agent readiness checker and fixer**. It scans your repository, explains why ag
> L89: |**Agent Failure Risk**|Predicts why Codex, Claude Code, Cursor, or similar agents may fail in your repo.|

## 星数曲线

```mermaid
xychart-beta
    title "shidesheng0218/repo-ready 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9fb2d5a64e47` · [字段定义](../../DATASET.md)*
