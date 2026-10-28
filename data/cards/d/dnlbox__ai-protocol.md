# dnlbox/ai-protocol

⭐ 19 · Shell · MIT · 推送 2026-08-09 · [GitHub](https://github.com/dnlbox/ai-protocol) · 个人维护

**从概念文档驱动 AI agent 构建新项目的脚手架协议**

面向绿地项目的 harness 无关工作流协议：先用纯 markdown 概念文档（问题陈述、约束）固定意图，再经 `/concept-intake`、`/shape-concept`、`/plan-implementation` 等五个生命周期阶段生成执行契约 `AGENTS.md`、启动角色与生命周期技能，随后由 agent 在有界目标内自主规划、实现、验证并写入 `BUILD_STATE.md` 检查点。提供自愈、崩溃安全状态、工作区嵌套等机制；以 GitHub Release 的 starter ZIP 与 kickstart.sh 脚本安装，明确不适用于遗留单体的回填，作者自述为进行中的实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 概念先行：先在 markdown 中固化意图，再交由 agent 执行
- 九项执行机制：自愈、目标自主、持久状态（BUILD_STATE.md）、惰性技能加载等
- harness 无关：契约随仓库携带，可在 Cursor、Claude Code、Antigravity 间迁移
- starter 极小：AGENTS.md + 3 个角色 + 5 个技能，附 SHA256 校验的 Release ZIP 与 kickstart.sh

## 适用场景

- 绿地项目开工前先做概念推演，避免 prompt 链导致的需求漂移
- 让 AI 编码 agent 在有界目标内自主执行并保留可验证检查点
- monorepo 或多仓库工作区按层级组合契约与状态

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L19: Because the protocol handles the mechanics of how work gets executed (scope, authority, startup identity, self-heal
> L25: It shares the loop's instincts (durable, verifiable iteration with recovery), but it puts the thinking before the c

## 星数曲线

```mermaid
xychart-beta
    title "dnlbox/ai-protocol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0de9891e1607` · [字段定义](../../DATASET.md)*
