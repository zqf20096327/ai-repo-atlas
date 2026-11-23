# tedtanne/judge_jury_voter

⭐ 7 · Python · Apache-2.0 · 推送 2026-11-14 · [GitHub](https://github.com/tedtanne/judge_jury_voter) · [官网](https://tedtanner.org) · 个人维护

**多智能体代码/文档评审面板：评审、合议、投票并用纳什议价定修改清单**

以 Python 包形式提供的 AI 评审工具：一组按职业原型构建的 Judge 独立打分，Jury 阶段互相阅读匿名摘要后修订，Voter 汇总为决策与排序行动清单，Nash_Agent 在固定修订预算下用纳什议价解确定修复哪些发现；另有复用同一面板的 generate 起草循环。默认经 Claude Agent SDK 调用模型，也可配置 OpenAI/xAI/Gemini 或任何 OpenAI 兼容端点；支持 --repo、--url、PDF 等输入，可经 jjv-mcp 作为 MCP 服务器供任意客户端调用，运行花费由 --max-usd 等预算参数控制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Judge→Jury→Voter 三层评审流程与纳什议价 broker（Nash_Agent）确定修复清单
- 默认经 Claude Agent SDK 运行，支持 OpenAI/xAI/Gemini/本地 OpenAI 兼容端点
- jjv-mcp MCP 服务器支持任意客户端调用，免费工具不调用模型
- jjv render 生成浏览器可打开的评审过程页面，记录保存于 ~/.jjv/runs

## 适用场景

- 用多角色评审面板对设计文档、代码 diff 或网页给出评分与修改清单
- 从需求简报起草文档，由同一面板批评并修订
- 在 MCP 客户端中调用评审能力并限制花费预算

## 场景标签

`多智能体` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L9: A swarm of AI review agents. Each agent is an *archetype* of a best-in-the-business professional. Together they **re
> L11: JJV is not tied to one model. Judges run on Claude through the Agent SDK by default, or on OpenAI, xAI, Gemini or a

## 星数曲线

```mermaid
xychart-beta
    title "tedtanne/judge_jury_voter 星数(近 3 点)"
    x-axis ["2026-11-14", "2026-11-15", "2026-11-23"]
    y-axis "stars" 5 --> 8
    line [6, 7, 7]
```

2026-11-14 6 → 2026-11-23 7（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `05e202d2584e` · [字段定义](../../DATASET.md)*
