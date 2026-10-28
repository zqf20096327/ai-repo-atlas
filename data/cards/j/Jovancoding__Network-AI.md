# Jovancoding/Network-AI

⭐ 79 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/Jovancoding/Network-AI) · [官网](https://network-ai.org/) · 个人维护

**给多智能体开发者的 TypeScript 编排框架：共享状态、护栏与治理**

面向 TypeScript/Node.js 开发者的多智能体编排器：为任意 AI agent 技术栈提供带锁定的共享黑板（propose→validate→commit 防并行写冲突）、FSM 治理、token 预算、HMAC/Ed25519 审计与权限门控。提供 32 个框架适配器（LangChain、AutoGen、CrewAI、MCP 等），可作为 npm 库、MCP 服务器、CLI、Claude Code 插件或 Gemini CLI 扩展使用。v5.13 起 GovernedModelGateway 管理模型拒绝→回退→计费链；可选 ASI 严格模式提供证明携带动作、BFT 共识与停机开关，README 明确其非遏制证明，需配合 OS 级隔离。核心编排路径无需 LLM 调用即可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- propose→validate→commit 文件系统互斥的原子共享黑板
- 32 个框架适配器，无需胶水代码接入 LangChain/CrewAI/AutoGen/MCP 等
- FSM 治理、token 预算、签名审计日志与实时合规监控
- 可作为库、MCP 服务器、CLI、Claude Code 插件、Gemini CLI 扩展多种形态使用

## 适用场景

- 并行多智能体写共享状态时避免 last-write-wins 冲突
- 为不同框架的 agent 加统一的预算与权限治理
- 以 MCP 服务器或 CLI 形式接入现有 agent 工作流

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L26: Network-AI is a TypeScript/Node.js multi-agent orchestrator that adds coordination, guardrails, and governance to a
> L31: - **32 adapters** — LangChain (+ streaming), AutoGen, CrewAI, OpenAI Assistants, OpenAI Responses (Assistants succe
> L42: **Use Network-AI as:**

## 星数曲线

```mermaid
xychart-beta
    title "Jovancoding/Network-AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 77 --> 80
    line [78, 79, 79]
```

2026-10-18 78 → 2026-10-28 79（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d10ea7d8de70` · [字段定义](../../DATASET.md)*
