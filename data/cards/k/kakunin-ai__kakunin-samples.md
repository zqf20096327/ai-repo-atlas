# kakunin-ai/kakunin-samples

⭐ 15 · Python · MIT · 推送 2026-07-09 · [GitHub](https://github.com/kakunin-ai/kakunin-samples) · [官网](https://www.kakunin.ai/docs) · 组织维护

**AI agent 身份与合规 API 的端到端运行示例集**

Kakunin 开源项目的可运行示例仓库，演示其合规 API 的完整接入：为 AI agent 注册并签发 X.509 加密身份证书、按 scope 限制工具调用、记录行为事件、生成 MiCA 与 EU AI Act 合规报告。示例覆盖 TypeScript、Python、curl、Go，以及 LangChain、LlamaIndex、CrewAI、AutoGen、Next.js、Vercel AI SDK、Mastra 等框架的守护类封装（如 KakununToolGuard）。运行需从控制台获取 API key，提供可复用的 GitHub Actions 工作流用于 CI 中签发证书。

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

- 覆盖 agent 注册、证书签发、行为事件、合规报告的完整生命周期示例
- LangChain/LlamaIndex/CrewAI/AutoGen 等 7 类框架的 scope 守护封装示例
- TypeScript/Python/curl/Go 四种语言基础接入示例
- 可复用的 GitHub Actions 工作流在 CI 中签发证书并输出 agent_id

## 适用场景

- 为 AI agent 系统接入 X.509 身份证书与实时行为监控
- 在多 agent 框架中按 scope 限制工具调用
- 生成符合 MiCA Art. 72 与 EU AI Act 的合规报告
- 在 CI 流水线中自动完成 agent 注册与证书签发

## 场景标签

 · 领域:AI agent 安全/合规基础设施

## 证据(README 行号)

> L10: End-to-end integration samples for the Kakunin AI agent compliance API.
> L14: **Kakunin issues X.509 cryptographic identities to AI agents, monitors their behaviour in real time, and generates 

## 星数曲线

```mermaid
xychart-beta
    title "kakunin-ai/kakunin-samples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ead1dae26a3d` · [字段定义](../../DATASET.md)*
