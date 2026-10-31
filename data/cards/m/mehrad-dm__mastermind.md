# mehrad-dm/mastermind

⭐ 23 · Shell · MIT · 推送 2026-10-24 · [GitHub](https://github.com/mehrad-dm/mastermind) · [官网](https://mastermind.mehrad.me) · 个人维护

**给 Claude Code/Cursor/Codex 注入工程判断与自检纪律的 Markdown 规则包**

以纯 Markdown 知识文件形式接入 AI 编程工具的'大脑'：提供工程默认选型、决策方法、完成前端到端自检、学习代码库风格并沉淀 lessons。机制为小内核（CLAUDE.md）+ 按需加载的技能与领域包，预构建路由索引（无 AI、无网络生成）按任务指向所需文件，宣称每任务减少约 65% token。通过 npx 安装器按项目接线（.mastermind/.claude/.cursor/AGENTS.md），支持 monorepo 分 context、Claude Code 插件市场安装。官方仅支持 Claude Code、Cursor、Codex 三种工具；需 Bash、Git、Node 18+。自称 experimental、API 与默认值可能变化，效果在 evals/RESULTS.md 度量。

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

- 纯 Markdown + 无包依赖的 npm CLI（~11 KB packed），按项目隔离安装并可提交共享
- 预构建路由索引按任务加载所需文件，宣称实测每任务减少约 65% token
- 对 Claude Code / Cursor / Codex 三工具原生接线，monorepo 可按路径 glob 分 context
- 技能含 build/debug/qa/interview/persona 等，自动识别任务并应用，可持续自我改进（lessons.md）

## 适用场景

- 让 AI 编程助手在交付前自行验证工作，减少人工盯审
- 团队把共享的工程约定与经验教训（brain）随仓库提交给队友
- monorepo 中为不同技术栈的子应用加载各自的规则上下文

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L14: > **Make your AI coding assistant trustworthy.** MasterMind is plain Markdown that gives **Claude Code,
> L18: No service to run and no package dependencies, just text that loads into your AI (installing it and
> L51: - **No service to run, and no package dependencies.** The knowledge is plain Markdown in git:

## 星数曲线

```mermaid
xychart-beta
    title "mehrad-dm/mastermind 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9a562bec80c2` · [字段定义](../../DATASET.md)*
