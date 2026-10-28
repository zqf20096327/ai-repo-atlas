# skainguyen1412/antigravity-superpowers

⭐ 330 · JavaScript · 推送 2026-02-26 · [GitHub](https://github.com/skainguyen1412/antigravity-superpowers) · 个人维护

**将 Superpowers 技能工作流移植到 Antigravity 的 13 技能包**

面向 Antigravity 平台的 Superpowers 工作流移植：原为 Claude Code 设计的技能系统（头脑风暴、写计划、TDD、代码评审、验证等），因原仓库不支持 Antigravity 且无官方移植计划而由作者自行移植。保留 14 个原始技能中的 12 个，另 2 个依赖并行子代理的技能合并为新的 single-flow-task-execution 顺序执行技能，共 13 个技能；平台特定引用（工具名、路径）做了翻译，任务追踪改用 docs/plans/task.md 活表。通过 npx 或全局 npm 安装 CLI，运行 init 将 .agent profile 复制到项目根，Antigravity 自动加载并按请求路由技能；附带 workflows、评审 agent profile 与自动化验证测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个技能覆盖开发全生命周期（头脑风暴/计划/TDD/评审/验证）
- 保留 12/14 原始技能，2 个并行子代理技能合并为顺序执行的 single-flow-task-execution
- npx 一条命令初始化 .agent profile，Antigravity 自动加载
- 附带 .agent/tests 自动化 profile 验证（技能存在性、frontmatter、遗留模式检测）

## 适用场景

- 在 Antigravity 项目中使用 Superpowers 的结构化 AI 开发工作流
- 让 AI 编码助手按 TDD、先规划后编码、先验证后宣称完成的纪律执行任务
- 曾在 Claude Code 上使用 Superpowers、迁移到 Antigravity 后延续同一套流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L12: Superpowers is an incredible skill-based workflow system that gives AI coding assistants structured, reliable behav
> L14: **This project ports that entire system to Antigravity**, preserving the original flow as faithfully as possible. T
> L83: The CLI copies a complete `.agent` profile into your project root. Once initialized, Antigravity picks up the profi

## 星数曲线

```mermaid
xychart-beta
    title "skainguyen1412/antigravity-superpowers 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 328 --> 331
    line [329, 330, 330]
```

2026-10-18 329 → 2026-10-28 330（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `40c5a8117d55` · [字段定义](../../DATASET.md)*
