# galpt/kilocode-agents

⭐ 16 · Shell · CC-BY-4.0 · 推送 2026-05-27 · [GitHub](https://github.com/galpt/kilocode-agents) · 个人维护

**Kilo Code 的 16 个专职子代理预设与多代理流水线配置集**

面向 Kilo Code（VS Code 扩展与 Kilo CLI）的提示词与代理预设仓库：将软件工程任务拆解为分诊、上下文收集、设计、实现、集成、评审、修复、交付的流水线，各阶段由 Kilo Task() 工具强制执行，跳过阶段会产生工具错误。提供 16 个代理定义（1 个主编排者 ceo 与 15 个子代理，含 QA/安全/性能等多评审通道），以 .kilo/agent/*.md 为权威格式，JSON 为 VS Code 派生工件。要求 Kilo CLI v7.3.12 或更新版本，测试模型包括 Claude Opus、GPT-5.4、DeepSeek V4、MiniMax-M2.7。提示词采用 CC BY 4.0，代码与配置采用 Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 个代理定义：ceo 编排者 + 15 个专职子代理
- 流水线阶段由 Kilo Task() 工具强制，跳过即报错
- 同一 .md 配置文件兼容 CLI 与 VS Code 扩展
- 支持按项目覆写/禁用单个代理并指定子代理模型

## 适用场景

- 为 Kilo Code 配置结构化多代理软件工程流水线
- 让 AI 代理按阶段完成需求分诊到交付的完整流程
- 在 QA/安全/性能等多评审维度下做代码评审与修复

## 场景标签

`提示工程` `代码审查` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: A tool-enforced multi-agent pipeline architecture for Kilo Code. Decompose
> L52: Each stage is enforced by the `Task()` tool — skipping a stage produces an

## 星数曲线

```mermaid
xychart-beta
    title "galpt/kilocode-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `b2554c324e4b` · [字段定义](../../DATASET.md)*
