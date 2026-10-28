# microsoft/Agent365-nodejs

⭐ 24 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/microsoft/Agent365-nodejs) · 组织维护

**微软 Agent 365 SDK（Node.js/TS）：为 M365/Teams 构建企业级 agent 提供扩展工具**

微软开源的 Node.js/TypeScript SDK，扩展 Microsoft 365 Agents SDK，为构建面向 M365、Teams、Copilot Studio 与 Webchat 的生产级 agent 提供四类能力：可观测性（追踪/缓存/监控）、通知服务、运行时工具与开发工具。包含 OpenAI、Claude/Anthropic、LangChain 的扩展包及 MCP 集成。项目处于活跃开发中，包以 @microsoft/agents-a365 前缀发布到 npm，源码用 pnpm 构建。

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

- 四类核心能力：可观测性、通知、运行时、开发工具
- 提供 OpenAI / Claude/Anthropic / LangChain 扩展包与 MCP 集成
- npm 包以 @microsoft/agents-a365 前缀发布
- 支持 M365、Teams、Copilot Studio、Webchat 平台的 agent 构建

## 适用场景

- 为企业 agent 应用接入追踪与监控能力
- 在 Teams/Copilot Studio 应用中添加 agent 通知服务
- 配合 OpenAI/LangChain 等生态构建 agent 工具链

## 场景标签

`Agent 框架` `LLM 可观测性` · 领域:Agent 开发

## 证据(README 行号)

> L13: The Microsoft Agent 365 SDK extends the Microsoft 365 Agents SDK with enterprise-grade capabilities for building so
> L17: - **Observability**: Comprehensive tracing, caching, and monitoring capabilities for agent applications
> L19: - **Runtime**: Core utilities and extensions for agent runtime operations

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/Agent365-nodejs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2594b02066c9` · [字段定义](../../DATASET.md)*
