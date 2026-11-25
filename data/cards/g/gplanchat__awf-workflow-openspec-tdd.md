# gplanchat/awf-workflow-openspec-tdd

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/gplanchat/awf-workflow-openspec-tdd) · 个人维护

**给开发者提供 OpenSpec 测试先行的 agent 工作流包**

一个 AWF 工作流包，将 OpenSpec 变更以测试先行方式落地：tasks.md 的每个代码切片依次经过 RED、GREEN 与评审，评审工具命令来自项目的语言注册表（.awf/languages.yaml）；阶段推进依赖测试运行器、静态分析、变异测试等工具的退出码而非 agent 自报。提供 flow-propose/flow-review/flow-apply-many 等工作流，EGM 七类评审人逐个以只读工具、无历史上下文运行，另可从 Claude Code marketplace 以 /flow:* 命令驱动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 阶段门禁依据工具退出码（测试/静态分析/变异测试），不采信 agent 报告
- EGM 七类评审人各以全新 agent、只读工具、无先前上下文运行
- 语言注册表驱动，示例覆盖 PHP、TypeScript、Three.js、Go、Rust
- (parallel) 任务组在各子 worktree 中并行执行

## 适用场景

- 让 agent 按 RED-GREEN-评审流程逐切片实现 OpenSpec 变更
- 多个变更并行应用并逐个合并回 main
- 在 Claude Code 会话中用 /flow:* 命令驱动提案、评审与归档

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: An AWF workflow pack that applies OpenSpec
> L9: testing), never on what the agent reports.
> L17: - an agent CLI that awf can drive, Claude Code by default

## 星数曲线

```mermaid
xychart-beta
    title "gplanchat/awf-workflow-openspec-tdd 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-22 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `eb39d68db960` · [字段定义](../../DATASET.md)*
