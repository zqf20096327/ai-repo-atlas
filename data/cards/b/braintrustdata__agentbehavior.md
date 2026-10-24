# braintrustdata/agentbehavior

⭐ 361 · TypeScript · Apache-2.0 · 推送 2026-07-29 · [GitHub](https://github.com/braintrustdata/agentbehavior) · [官网](https://www.agentbehavior.dev/) · 组织维护

**定义与评估 AI agent 行为的开放标准（BEHAVIOR.md）**

由 Braintrust 维护的 Behavior Specs 开放标准：用带 YAML frontmatter 的 BEHAVIOR.md 文件描述 agent 在整段轨迹中应表现的行为（收集上下文、决策、行动、恢复），文件存于 .agents/behaviors/ 目录。标准先于评审、评分与评测存在，作为审阅 trace、设计 eval、对齐 prompt 的统一依据。仓库同时提供 TypeScript CLI（packages/agentbehavior）校验 spec 结构，并在示例中演示对录制轨迹按 true/false/na 约定评判。使用需克隆仓库后 pnpm 安装构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BEHAVIOR.md 开放格式：YAML frontmatter + 自由 Markdown 描述
- spec 文件与被描述 agent 同目录存放（.agents/behaviors/）
- CLI 校验 spec 结构（pnpm exec agentbehavior validate）
- 示例给出对录制轨迹的 true/false/na 评判约定

## 适用场景

- 为长时程 agent 写下行为标准，作为评测评据的唯一事实来源
- 用 CLI 校验团队行为 spec 的结构合法性
- 对照 spec 审阅 agent 轨迹与对齐 prompt

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: **Behavior specs** are an open standard for defining and evaluating how an AI agent should behave across a whole tra
> L9: A modern agent can work for hours and make hundreds of decisions in a single trajectory, and you cannot reduce that 
> L47: 3. Evaluate traces against your specs. The runnable examples show a `true`/`false`/`na` judging convention over rec

## 星数曲线

```mermaid
xychart-beta
    title "braintrustdata/agentbehavior 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 359 --> 362
    line [360, 361, 361]
```

2026-10-18 360 → 2026-10-24 361（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `6d9c98a6f6e4` · [字段定义](../../DATASET.md)*
