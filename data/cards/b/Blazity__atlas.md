# Blazity/atlas

⭐ 26 · JavaScript · MIT · 推送 2026-07-26 · [GitHub](https://github.com/Blazity/atlas) · [官网](https://blazity.com/atlas) · 组织维护

**为代码仓库生成共享 AI 上下文脚手架，供多种 coding agent 使用**

Atlas 是一个框架无关的 CLI 脚手架：一条 npx 命令在仓库中生成 AGENTS.md、CLAUDE.md 入口与 .ai/ 工作区（计划、研究、ADR、记忆、词汇表、评审结论的统一目录结构），由 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等读取共享。atlas doctor 以冻结退出码在 CI 中校验结构漂移，--fix 可确定性修复；atlas-review 技能产出带证据的评审结论文件。限制：不运行测试/评测，不是 agent 运行时，不生成代码；需 Node.js ≥20 与 git 仓库，Windows 未测试。运行时无网络调用、无遥测，仅一个依赖。

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

- 一条命令脚手架 AGENTS.md/CLAUDE.md 与 .ai/ 工作区，多 agent 共享同一上下文
- atlas doctor 冻结退出码 CI 门禁，--fix 确定性修复漂移
- atlas status 只读仪表盘，--json 输出稳定键供脚本使用
- atlas-review 技能把评审结论写入 .ai/results/ 留档

## 适用场景

- 为团队仓库建立多 coding agent 共享的统一文档结构与记忆
- 在 CI 中用结构门禁检测 AI 上下文工作区的漂移
- 让不同工具的计划、研究、评审产物落入同一目录树

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L19: Atlas (by Blazity) gives the repository one place for all of it: a unified documentation structure and plain-files 
> L148: It does **not** run your tests, evals, or policy checks (execution gates are where the standard points next, not w

## 星数曲线

```mermaid
xychart-beta
    title "Blazity/atlas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bba80a2f9b8e` · [字段定义](../../DATASET.md)*
