# Jason-Cyr/AgenticProductTeam

⭐ 20 · TypeScript · MIT · 推送 2026-02-23 · [GitHub](https://github.com/Jason-Cyr/AgenticProductTeam) · 个人维护

**给 Claude Code 的多 agent 产品流程加速器：输入想法产出全套产品文档**

基于 TypeScript 的 agentic 产品生命周期工具：用户向 Claude Code 描述产品想法后，由 PM、Research、Design、Engineering 四个 agent 角色按阶段流水线依次产出 PRD、Research、PrototypeSpec、TechSpec 与 Backlog 等结构化文档，写入 ./artifacts/ 目录。以 Claude Code 作为交互界面，无需自定义 CLI；LLM 供应商通过 config/llm.json 在 Anthropic 与 OpenAI 间切换，可选接入 Figma MCP。支持逐阶段人工确认与自动推进两种模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四 agent 角色（PM/Research/Design/Engineering）分阶段产出 PRD、研究计划、原型规格、技术规格与 Backlog
- 以 Claude Code 为交互界面，通过 CLAUDE.md 指令驱动流水线
- LLM 供应商可在 Anthropic 与 OpenAI 间切换
- 支持人工逐阶段确认与质量检查自动推进两种模式

## 适用场景

- 从一句产品想法快速生成 PRD 与技术规格等全套文档
- 产品小队用多角色 agent 流程推进从需求到 Backlog 的文档产出
- 在 Claude Code 中以对话方式迭代更新已有产品文档

## 场景标签

`多智能体` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L3: An agentic product lifecycle accelerator. Give it a product idea, and it runs a staged pipeline across four agent ro
> L25: 3. Each stage runs an LLM-powered agent that reads prior artifacts and produces new ones

## 星数曲线

```mermaid
xychart-beta
    title "Jason-Cyr/AgenticProductTeam 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `237cce462091` · [字段定义](../../DATASET.md)*
