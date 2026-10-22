# arklexai/arksim

⭐ 234 · Python · Apache-2.0 · 推送 2026-08-05 · [GitHub](https://github.com/arklexai/arksim) · [官网](https://docs.arklex.ai) · 组织维护

**多轮对话模拟测试工具：用合成用户在上线前发现 agent 失败**

面向 AI agent 开发者的模拟评测工具：生成具有不同画像、目标与知识水平的 LLM 合成用户，与被测 agent 进行多轮对话，逐轮评估 helpfulness、faithfulness、目标完成度等指标并输出交互式报告。支持 Python 类、Chat Completions 端点与 A2A 协议接入 agent，兼容 14+ 框架，可作为 CI 质量门禁（低于阈值退出非零码）。以 pip 包分发，附带 Claude Code 技能包与 MCP server，数据在自有基础设施运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 合成用户生成多轮对话并逐轮评估
- 支持 Python 类 / Chat Completions / A2A 三种 agent 接入方式
- CI 集成：低于阈值时以非零码退出
- 附带 Claude Code 技能包与 MCP server

## 适用场景

- 上线前用合成用户测试 agent 的多轮对话表现
- 在 PR 流水线中把模拟评测设为质量门禁
- 定位 agent 在哪一轮、因何种原因失败

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L25: ArkSim generates LLM-powered synthetic users that hold realistic multi-turn conversations with your agent. Each use
> L103: - **Simulation, not just evaluation.** Most tools score conversations you already have. ArkSim generates them with
> L105: - **Any agent, any framework.** Works with 14+ frameworks through Chat Completions, A2A, or direct Python import.

## 星数曲线

```mermaid
xychart-beta
    title "arklexai/arksim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 232 --> 234
    line [233, 233]
```

2026-10-18 233 → 2026-10-22 233（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `167fe2a6ff1a` · [字段定义](../../DATASET.md)*
