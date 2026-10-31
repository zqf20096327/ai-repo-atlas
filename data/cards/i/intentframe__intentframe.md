# intentframe/intentframe

⭐ 14 · Python · AGPL-3.0 · 推送 2026-07-27 · [GitHub](https://github.com/intentframe/intentframe) · [官网](https://www.intentframe.com) · 个人维护

**AI 治理与安全运行时：代理提议动作，策略验证后由独立 Executor 执行**

面向需要受控 agent 工具使用的开发者与企业：agent 只负责推理并提交结构化 intent，运行时先用确定性规则（硬阻断命令模式、行为拒绝类）校验，再由语义层（AI Guardian，读自然语言策略）审查，批准后由持有全部凭证的独立 Executor 进程执行，全程写审计日志。限制：AGPL-3.0 + Apache-2.0 双许可，需 Python 3.14+、macOS 14–26，v0.1.1 早期版本，仅管控影响用户世界的非确定性 AI 决策，不保护整个程序。README 记录了 100 条恶意 intent 的阻断测试及 91/100 的早期失败与修复过程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 与执行分离：LLM 决策→intent 验证→独立 Executor 执行，fail-closed
- 双层策略：确定性技术层先阻断，语义层按自然语言规则审查
- Executor 持有全部凭证、不含 AI、写审计链，单运行时服务所有 agent
- root 级攻击测试：100/100 恶意 intent 阻断、100/100 良性工作流放行

## 适用场景

- 客户侧 AI agent 涉及资金、消息、数据写入时按策略门控
- 企业部署 agent 时产出确定性审计证据供安全审查
- CISO 用统一策略面与审计链替代逐 agent 的提示词规则
- LangChain/AutoGen/OpenAI Agents SDK 通过 actor.submit 接入门控

## 场景标签

`Agent 框架` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L7:  IntentFrame is an AI governance and security runtime for controlled agent tool use: agents propose actions, policy 
> L90:     A["🤖 Agent<br/>(any LLM / framework)"] -->|"intent request"| V{{"🚪 IntentFrame<br/>policy boundary"}}
> L99: - **The Executor is the syscall layer for agency.** It is a separate IntentFrame-controlled process that turns appr

## 星数曲线

```mermaid
xychart-beta
    title "intentframe/intentframe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `499d5595fdad` · [字段定义](../../DATASET.md)*
