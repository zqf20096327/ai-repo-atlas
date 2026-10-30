# dannwaneri/spec-writer

⭐ 29 · 推送 2026-03-18 · [GitHub](https://github.com/dannwaneri/spec-writer) · 个人维护

**把模糊需求转成规格、技术方案与任务拆解的 Claude Code 技能**

面向 AI 编程 agent 的 Agent Skills 标准技能：用户以 /spec-writer 加功能描述调用，一次性生成三段产出——技术无关的功能规格（含 Given/When/Then 验收标准）、技术方案（架构/数据模型/API 契约/测试策略）、以及可独立验证的有序任务拆解。关键机制是先生成后提问：不预先追问，而是在草稿中内联标注每个未明说的假设，末尾汇总为按影响分级（HIGH 等）的待审清单。同一技能文件可在 Claude Code、Cursor、Gemini CLI、Codex CLI 等遵循 Agent Skills 标准的 agent 上使用。安装方式为 git clone 到技能目录或手动复制 SKILL.md。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次调用生成 Spec、Plan、Tasks 三段结构化产出
- 先生成后提问：假设内联标注并按影响分级汇总
- 验收标准二元化，规格与技术方案分离
- 遵循 Agent Skills 标准，跨多种编程 agent 复用

## 适用场景

- 开发者在把需求交给 AI 编程 agent 前先生成明确规格
- 把模糊工单或 PRD 片段转成可验证的任务拆解
- 审查 agent 生成方案中的隐含假设，避免静默决策出错

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Claude Code skill that turns vague feature requests into structured specs, technical plans, and task breakdowns — 
> L117: spec-writer follows the Agent Skills specification, which means the same skill file works across Claude Code, Curs

## 星数曲线

```mermaid
xychart-beta
    title "dannwaneri/spec-writer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-30 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `fa91cc00a967` · [字段定义](../../DATASET.md)*
