# rlespinasse/agent-skills

⭐ 13 · Just · MIT · 推送 2026-10-25 · [GitHub](https://github.com/rlespinasse/agent-skills) · 个人维护

**面向 AI 编码助手的 Agent Skills 技能集合（9 个技能）**

遵循 agentskills.io 规范的 Agent Skills 合集，提供 9 个技能：conventional-commit（规范提交信息）、diataxis（文档结构分类）、drawio-export-tools（导出工具选型）、french-language（法语写作规范）、local-branches-status（分支状态报告）、pin-github-actions（Actions SHA 固定）、verify-pr-logs（CI 日志诊断）、verify-readme-features（README 功能核验）。技能兼容 Claude Code、Cursor、VS Code、GitHub Copilot、Gemini CLI 等助手，可通过 npx 命令或 Claude Code 插件市场安装。

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

- 9 个覆盖 git 提交、文档、CI、安全等方面的 Agent Skills
- 兼容 Claude Code、Cursor、VS Code、GitHub Copilot、Gemini CLI
- npx skills add 一键安装全部或单个技能
- 含 Claude Code 插件市场安装方式

## 适用场景

- 让编码助手按 Conventional Commits 规范生成提交信息
- 让助手核验 README 功能列表与代码实现是否一致
- 将 GitHub Actions 固定到 commit SHA 以提升供应链安全
- 诊断 PR 上 CI 失败并指导修复

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A collection of Agent Skills for AI coding assistants.
> L130: - And other AI coding assistants supporting the Agent Skills specification
> L143: These skills follow the Agent Skills specification

## 星数曲线

```mermaid
xychart-beta
    title "rlespinasse/agent-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ca60319f10c6` · [字段定义](../../DATASET.md)*
