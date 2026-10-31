# pan94u/forge

⭐ 40 · Kotlin · NOASSERTION · 推送 2026-10-01 · [GitHub](https://github.com/pan94u/forge) · 个人维护

**AI 原生 IT 交付与治理基础设施：SuperAgent 全流程交付加评测护栏**

双层架构的软件交付平台：执行层为 Web IDE，含 SuperAgent 自主执行引擎（50 轮自主执行、24 个 MCP 工具、35 个 Skill、跨会话三层记忆）、质量基线检查与 HITL 审批；治理层为企业控制台（组织/成员/Provider 管理）。附 Forge Eval 持续评测模块，支持 Code/Model/Human 三类评分器、Pass@k 统计与回归检测，可评测外部 Agent。后端 Kotlin + Spring Boot 3，前端 Next.js 15，Docker Compose 7 容器部署，需 JDK 21 与至少一个模型 Provider API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SuperAgent 50 轮自主执行 + 24 个 MCP 工具 + 35 个 Skill 资产
- 三层跨会话记忆系统（Workspace/Stage/Session）
- Forge Eval：11 种代码断言、LLM-as-Judge、Pass@k 回归检测与生命周期管理
- 支持 Claude/Gemini/Qwen/Bedrock/MiniMax/OpenAI 兼容多 Provider

## 适用场景

- 用 1-2 人加 AI 完成规划到交付的软件开发生命周期
- 对 AI Agent 输出做持续评测与回归检测
- 企业统一管理组织、成员与 AI 模型 Provider

## 场景标签

`编码 Agent` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L17: - **Execution Layer (Web IDE)**: SuperAgent + 35 Skills + 24 MCP tools, three-loop architecture (human control loop
> L89: AI Agent outputs are non-deterministic. "It worked once" does not mean "it works reliably." Forge Eval is a **conti
> L133: |**External agent evaluation**|Configure SSE/REST endpoint (Dify, Coze, OpenAI-compatible, etc.)|Same scoring stan

## 星数曲线

```mermaid
xychart-beta
    title "pan94u/forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-31 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `61584bba7a14` · [字段定义](../../DATASET.md)*
