# open-agent-ai-security/observra

⭐ 25 · HTML · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/open-agent-ai-security/observra) · [官网](https://open-agent-ai-security.github.io/observra/) · 组织维护

**框架无关的 AI agent 遥测与可观测性库**

Observra 是面向 AI agent 系统的观测与遥测框架，通过 Common Information Model 归一化事件，以零侵入方式捕获 LLM 调用、工具调用、token 用量、成本与错误，无需在每个 agent 内手写日志。支持 Google ADK、Claude SDK、OpenAI Agents SDK、LangChain/LangGraph、Pydantic AI 五个框架的专用接入 extras；后端默认写 JSONL 文件，也支持 webhook、多后端分发与 OTel span/log 导出。附带成本阈值告警、PII 脱敏、事件去重、提示注入检测启发式与 AES 字段加密等特性。Python 3.10+，Apache-2.0 许可，由 Exabeam 赞助并贡献初始代码。

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

- 零侵入捕获 LLM 调用/工具调用/成本/错误，按 CIM 归一化事件
- 五个框架专用 extras（ADK/Claude/OpenAI Agents/LangChain/Pydantic AI）
- 后端：JSONL 默认、webhook、多后端分发、OTel span/log 导出
- 内置成本告警、PII 脱敏、ReDoS 安全正则（RE2）、AES 字段加密、提示注入检测

## 适用场景

- 给已运行的 agent 加装观测，回答做了什么、花了多少、是否异常
- 把 agent 遥测以 OTel 导入 Dynatrace/Grafana 等 SIEM/分析管道
- 按会话追踪成本并在超阈值时告警

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L12: Capture every meaningful agent action (token usage, tool calls, cost, errors) with structured context based on the 
> L14: Zero custom instrumentation per-agent. Answer "what happened, how much did it cost, and was it normal?" for any age

## 星数曲线

```mermaid
xychart-beta
    title "open-agent-ai-security/observra 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-28 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4bfe39f11aed` · [字段定义](../../DATASET.md)*
