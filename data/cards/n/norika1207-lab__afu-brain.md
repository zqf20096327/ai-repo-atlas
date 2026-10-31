# norika1207-lab/afu-brain

⭐ 23 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/norika1207-lab/afu-brain) · [官网](https://charenix.com/static/alfred-lobster-brain-demo.html) · 个人维护

**给个人 Agent 的决策与安全闸门：模型提议、闸门判定能否执行**

面向 OpenClaw 兼容个人 Agent 的参考决策层：位于模型输出与工具执行之间，将私有长期记忆转化为技能路由、风险分类与审批闸门，输出结构化 BrainDecision 决策对象（execute/prepare/ask/block 四种执行模式）。提供确定性 MASL 闸门、突触引擎、公共 RAG 包、文件库检索契约与决策契约 schema。用户自带模型密钥与语音栈，支持本地-only、共享认知订阅、OpenClaw 执行三种集成模式。仓库声明证据为早期试点结果，首个版本刻意保持精简。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模型输出与工具执行之间的确定性 MASL 闸门（execute/prepare/ask/block 四模式）
- 结构化 BrainDecision 决策契约与 JSON schema
- 公共 RAG 包与命名空间路由（MASL 安全、OpenClaw 决策案例、记忆参数等）
- 记忆事件到行为变化的滞后审计（rolling cognition audit）

## 适用场景

- 为会执行真实操作的个人 Agent 加装审批闸门，阻止未批准的外部动作
- 构建本地优先的语音管家或带审批门的技能路由器
- 搭建与模型无关的 Agent 安全评测框架

## 场景标签

`Agent 记忆` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L48: control a home environment, prompt instructions are not enough. The system needs
> L306: The model can propose a decision. It cannot directly authorize execution.

## 星数曲线

```mermaid
xychart-beta
    title "norika1207-lab/afu-brain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `81a85d906f4a` · [字段定义](../../DATASET.md)*
