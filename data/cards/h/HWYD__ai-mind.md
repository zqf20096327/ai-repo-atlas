# HWYD/ai-mind

⭐ 21 · TypeScript · MIT · 推送 2026-10-08 · [GitHub](https://github.com/HWYD/ai-mind) · 个人维护 · 中文 README

**AI Native Runtime 骨架：验证聊天到 Tool/MCP/Agent 的运行时分层**

以可运行 Web 应用形式展示 AI 应用运行时如何分层与约束：从本地聊天闭环逐步演进到结构化 NDJSON 流协议、Tool Calling、Skill Runtime、local stdio 与 remote Streamable HTTP MCP 接入，以及带白名单能力与有限预算的受控 Agent（Tasklist、Delivery Chain、文生图）。使用 LangChain/LangGraph 构建调用链，Provider Registry 隔离 Ollama、Qwen、DeepSeek。自定位为 Runtime Skeleton/MVP，明确不替代生产级 Agent 平台。pnpm + Turborepo 工程，提供 Electron 桌面宿主（未签名实验版）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Capability Model 统一描述 Tool/Resource/Prompt，接入本地 stdio 与远程 Streamable HTTP MCP
- NDJSON 结构化流协议，前端展示 public-safe Tool Trace 与 Agent 过程
- 受控 Agent：明确入口、白名单能力、有限步骤与可观察过程
- Provider Registry 隔离 Ollama / Qwen / DeepSeek，Model Catalog 白名单选模

## 适用场景

- 研究 AI Runtime 从单轮聊天到 Agent 的分层与边界设计
- 作为 MCP 接入、流式协议与受控 Agent 的技术探索样例
- 参考其结构化流式交互与 public-safe Trace 的前端展示方案

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: AI Mind 是一个持续演进的 **AI Native Runtime Skeleton**。它通过一个可运行的 Web 应用，验证 AI 应用从单轮聊天走向能力接入、结构化流式协议、Skill Runtime、MCP 集成与受控
> L5: 它不是普通 AI Chat Demo，也不是完整商业化 Agent 平台；当前处于 Runtime Skeleton / MVP 阶段，适合作为 AI Runtime、AI 应用前端、MCP 接入和可观察流式交互的技术探索样例。
> L30: - LangChain 负责模型、Tool 等 LLM 应用能力的集成；v0.6.x 的普通聊天通过 LangChain createAgent(version='v2') 进入受控 Tool loop。

## 星数曲线

```mermaid
xychart-beta
    title "HWYD/ai-mind 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `8dc9cc160810` · [字段定义](../../DATASET.md)*
