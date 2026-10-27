# glaucia86/repocheckai

⭐ 121 · TypeScript · MIT · 推送 2026-07-08 · [GitHub](https://github.com/glaucia86/repocheckai) · [官网](https://glaucia86.github.io/repocheckai/) · 个人维护

**面向开发者的 GitHub 仓库健康分析 CLI，AI 产出诊断与修复建议**

基于 GitHub Copilot SDK 构建的 TypeScript Agentic CLI 工具，对 GitHub 仓库做 6 类健康检查（文档、开发体验、CI/CD、测试、治理、安全），输出健康分数与 P0/P1/P2 分级发现及修复步骤。提供 Quick Scan（GitHub API 读取最多 20 文件）与 Deep Analysis（Repomix 全源码扫描）两种模式，支持 20+ AI 模型选择（GPT/Claude 系列，部分依赖 Copilot 套餐）、斜杠命令交互界面、本地 Web UI，并可通过 --issue 参数自动创建带优先级标签的 GitHub issue。需 GitHub Copilot 订阅与 Node.js 24+，分析在本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 类健康检查，输出 P0/P1/P2 分级发现与修复步骤
- Quick Scan 与 Deep Analysis（Repomix 全源码扫描）两种模式
- --issue 自动创建带优先级标签的 GitHub issue
- 基于 GitHub Copilot SDK，支持 20+ 模型选择（premium 模型依赖 Copilot 套餐）

## 适用场景

- 我想让 AI 全面体检我的仓库并给出修复优先级
- 在 CI/CD 中自动化仓库健康检查并自动建 issue 追踪
- 团队协作中跟踪仓库文档、测试与安全的缺失项

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L6:  Built with the GitHub Copilot SDK — the same AI agent runtime that powers Copilot CLI.
> L42: **RepoCheckAI** is your repository's AI doctor that diagnoses issues and prescribes solutions. It performs comprehe
> L54: - **20+ AI Models** — including `auto`, GPT-4o, Claude Sonnet 4, GPT-5.5, Claude Opus 4.7, and more

## 星数曲线

```mermaid
xychart-beta
    title "glaucia86/repocheckai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 120 --> 122
    line [121, 121]
```

2026-10-18 121 → 2026-10-27 121（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2e0f3e7834dd` · [字段定义](../../DATASET.md)*
