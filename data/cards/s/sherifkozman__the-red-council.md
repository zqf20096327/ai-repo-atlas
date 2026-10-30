# sherifkozman/the-red-council

⭐ 17 · Python · MIT · 推送 2026-05-09 · [GitHub](https://github.com/sherifkozman/the-red-council) · [官网](https://theredcouncil.com) · 个人维护

**LLM 对抗安全测试平台：攻击、判定、加固、验证闭环**

面向 LLM 与 AI Agent 的自动化红队测试平台：红队 agent 基于来自 HarmBench/PyRIT 数据集的 165+ 知识库条目生成对抗提示，裁判 agent 评分目标响应是否泄露秘密或违规，蓝队 agent 自动加固系统提示词，编排器复跑攻击验证修复效果。v0.5.0 起支持基于 OWASP Agentic Top 10 的 agent 安全测试，提供 InstrumentedAgent SDK 包装任意 agent 捕获工具调用，并集成 LangChain/LangGraph/MCP。攻击生成、判定与防御使用 Gemini 3 Pro，需 Google Cloud 凭据；前端为 Next.js，需 Python 3.11+ 与 Node.js 18+。

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

- 攻击→判定→防御→验证的闭环红队工作流
- 基于 HarmBench/PyRIT 的 165+ 对抗知识库
- OWASP Agentic Top 10（ASI01-ASI10）agent 漏洞测试与 InstrumentedAgent SDK
- 支持任意 LLM 端点（OpenAI/Anthropic/Vertex/本地）与 FastAPI SSE 流式 API

## 适用场景

- 对自有 LLM 或 agent 系统做自动化红队安全测试
- 检测系统提示词的泄露与策略违规并自动加固
- 按 OWASP Agentic Top 10 输出漏洞报告与修复建议

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L12: The Red Council is an automated adversarial testing platform for Large Language Models. It implements a closed-loop
> L81: - **OWASP Agentic Top 10**: Test for all 10 agent-specific vulnerabilities (ASI01-ASI10)

## 星数曲线

```mermaid
xychart-beta
    title "sherifkozman/the-red-council 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `79d64a67fac0` · [字段定义](../../DATASET.md)*
