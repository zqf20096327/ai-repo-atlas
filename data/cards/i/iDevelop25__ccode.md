# iDevelop25/ccode

⭐ 16 · TypeScript · 推送 2026-03-13 · [GitHub](https://github.com/iDevelop25/ccode) · 个人维护

**为 AI 辅助开发生成并同步项目上下文的 CLI 工具**

Node.js 全局安装的命令行工具：通过交互式向导和 AI（Gemini 或 Claude）在仓库内生成项目上下文（愿景、架构、规则、任务清单），存于 .ccode/ 目录，并按各工具格式同步为 AGENTS.md、CLAUDE.md、GEMINI.md、.cursorrules、copilot-instructions.md 等文件。支持文件变更监听的持续会话、基于实际文件的 AI 任务验收核验、上下文导出与项目健康检查。上下文深度按项目复杂度分级。给使用多种 AI 编程工具的开发者使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次生成并同步到 5+ 种 AI 编码工具的上下文文件（AGENTS.md/CLAUDE.md/.cursorrules 等）
- 以 .ccode/ 为单一事实来源派生多格式输出
- 基于实际项目文件的任务验收核验（ccode verify）
- 自动检测 AI 提供商：Gemini CLI OAuth、环境变量或手动向导

## 适用场景

- 我在多个 AI 编码工具间切换，希望项目上下文保持同步
- 新会话不用每次向 AI 重新解释项目架构
- 用验收标准核验任务是否在项目文件中真实完成

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L26: Then it **syncs that context to every major AI tool** automatically.
> L32: This is what makes CCODE different. One command generates context files for **every major AI tool**:

## 星数曲线

```mermaid
xychart-beta
    title "iDevelop25/ccode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1665d9244e6d` · [字段定义](../../DATASET.md)*
