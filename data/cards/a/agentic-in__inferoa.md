# agentic-in/inferoa

⭐ 566 · TypeScript · Apache-2.0 · 推送 2026-06-18 · [GitHub](https://github.com/agentic-in/inferoa) · [官网](https://inferoa.agentic-in.ai) · 组织维护

**面向推理侧优化的 Agent Harness：递归长程循环与 Token 压力控制**

Inferoa 是一个基于 vLLM 生态构建的 Agent Harness 运行时，核心概念是 Loop Engineering：通过 /loop 运行持久的递归循环，携带目标、验证、决策、恢复与完成证据跨任务推进。其定位特色在推理侧（inference-native）：按成本/安全/隐私/能力做模型路由选择，维护前缀缓存纪律、压缩上下文、限制可变历史，并通过 /tokenmaxxing 命令展示 token 与成本压力。以 npm 全局安装提供，inferoa setup 配置端点、模型、API key 后启动 TUI 交互，也支持 --print 非交互模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- /loop 递归长程循环：目标、验证、决策、恢复与完成证据跨任务保持
- 前缀缓存纪律与有界上下文（压缩、摘要、受限历史与工具输出）
- 基于 vLLM 生态的智能模型路由（按成本、安全、隐私、能力、会话压力）
- /tokenmaxxing 命令展示前缀缓存复用与 token/成本压力

## 适用场景

- 通过 TUI 让 agent 在长程任务中自我修正直到工作被验证
- 在多模型/自托管 vLLM 路径间按成本与隐私选择推理路径
- 观察并控制 agent 会话的 token 与前缀缓存压力

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L19: Inferoa is an **Inference-native Tokenmaxxing Agent Harness for Loop
> L67: Inferoa is built on top of the vLLM ecosystem and extends tokenmaxxing across
> L73: |Agent Harness|Inferoa|Sessions, tools, plans, loops, resources, evidence, and prefix-cache discipline|Give the loo

## 星数曲线

```mermaid
xychart-beta
    title "agentic-in/inferoa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 565 --> 567
    line [566, 566]
```

2026-10-18 566 → 2026-10-29 566（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `dd5029f9f253` · [字段定义](../../DATASET.md)*
