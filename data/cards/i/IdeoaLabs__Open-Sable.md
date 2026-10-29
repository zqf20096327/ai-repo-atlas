# IdeoaLabs/Open-Sable

⭐ 27 · Python · MIT · 推送 2026-05-22 · [GitHub](https://github.com/IdeoaLabs/Open-Sable) · [官网](https://opensable.com) · 组织维护

**本地优先的自主 AI agent 框架，长期运行执行真实任务**

面向希望在本地机器 7x24 运行自主 agent 的开发者的 Python 框架。提供多 agent 架构（按 profile 隔离身份、工具权限与记忆）、Ollama 优先的本地推理与云端回退、低显存模式、认知记忆栈与 ReAct 多步工具链，以及 Telegram 界面、RAG 文档流、GitHub/邮件/日历/多交易所交易等技能集成。README 标注 518 个测试与 128 个模块，提供树莓派安装脚本。v1.5-v1.7 引入大量名称风格化的“认知模块”，其有效性无法从 README 核验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ollama 优先本地推理，低显存模式与云端回退
- 多 agent profile 架构：隔离身份、权限、记忆与数据
- Telegram 界面、RAG、GitHub/邮件/日历/交易等 21+ 技能
- 树莓派安装脚本（自修复/校验模式）

## 适用场景

- 在本机长期运行一个可对接 Telegram 的自主 agent
- 通过工具链让 agent 执行邮件、日历、GitHub 等真实任务
- 低配硬件或树莓派上运行本地推理 agent

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L15: Open-Sable is a next-generation autonomous AI agent framework with Agentic AI cognitive subsystems. It runs 24/7 on
> L25: - Ollama-first local inference with cloud-provider fallback.

## 星数曲线

```mermaid
xychart-beta
    title "IdeoaLabs/Open-Sable 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-29 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `338dac85ce79` · [字段定义](../../DATASET.md)*
