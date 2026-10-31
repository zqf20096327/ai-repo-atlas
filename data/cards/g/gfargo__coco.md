# gfargo/coco

⭐ 14 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/gfargo/coco) · [官网](https://coco.griffen.codes) · 个人维护

**CLI git 助手：AI 生成提交信息、变更日志、代码审查与 PR**

面向使用 git 的开发者的终端工具，npm 包 git-coco、命令为 coco。核心功能：从暂存 diff 生成 Conventional Commits 格式提交信息，并可拆分大暂存区为多提交；生成变更日志、AI 代码审查（支持严重度门控用于 CI）、PR 标题与正文生成、终端 git 工作站（16 视图）。开箱支持 OpenAI、Anthropic、Gemini、Mistral、Azure OpenAI、AWS Bedrock、Ollama 七个提供商及 OpenAI 兼容端点，可用 Ollama 完全离线运行。另提供版本化 JSON/stdin 的 agent 接口与本地 stdio MCP 服务器（默认四个只读生成工具）。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从暂存 diff 生成 Conventional Commits 提交信息，支持 --split 拆分为逻辑多提交
- 七家 AI 提供商 + OpenAI 兼容端点，Ollama 可完全本地离线运行
- coco ui 终端工作站：16 视图、g-chord 导航、120+ 主题
- coco mcp 本地 stdio 服务器，默认只读，--allow-write 可选启用提交工具
- 提供 GitHub Action 复合动作用于 CI 代码审查，附 git hooks 与 pre-commit 集成

## 适用场景

- 让 AI 从暂存改动自动生成规范的提交信息
- 在 CI 中用 AI 代码审查按严重度门控拦截问题
- 通过 agent/MCP 接口让编码代理调用提交草稿与审查能力
- 离线（Ollama）环境下使用 AI git 工作流

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L10: **AI commits, changelogs, code review, PR creation, a structured agent/MCP API, and a full keyboard-driven git work
> L27: - 🤖 **Smart commits** — contextual AI messages from your staged diff, with Conventional Commits and commitlint vali

## 星数曲线

```mermaid
xychart-beta
    title "gfargo/coco 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `20f9b7482341` · [字段定义](../../DATASET.md)*
