# ZenGuard-AI/fast-llm-security-guardrails

⭐ 155 · Python · MIT · 推送 2026-02-03 · [GitHub](https://github.com/ZenGuard-AI/fast-llm-security-guardrails) · [官网](https://zenguard.ai/) · 组织维护

**面向 AI Agent 的实时安全防护层：检测提示注入/越狱/PII 泄露**

ZenGuard 提供面向 AI Agent 运行时的信任层 SDK，通过检测器在运行时防护提示注入、越狱、PII 泄露、敏感信息与主题/关键词违规，支持允许/禁止主题检测。以 Python 包（pip/poetry）安装，通过 API key 接入 ZenGuard 基础设施，提供 BASE 免费限流层与企业 DEDICATED 层；v0.3.0 起多检测器并行仅限 DEDICATED 层。提供 LangChain/LlamaIndex 集成示例与 Colab 笔记、Salesforce (Agentforce) 集成指南。注意：仓库已归档为只读状态。

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

- 提示注入/越狱/PII/主题/关键词/密钥等多类检测器
- 分层基础设施：BASE 免费限流层与 DEDICATED 企业层
- LangChain 与 LlamaIndex 集成示例及 Colab 演示
- Salesforce (Agentforce) 集成指南

## 适用场景

- 在 AI Agent 运行时拦截提示注入与越狱尝试
- 检测并管理用户请求/响应中的 PII 与敏感数据
- 限制模型输出仅覆盖允许主题或过滤关键词

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L14: ZenGuard is a real-time trust layer for AI Agents. It protects AI agents during the runtime from prompt attacks, da
> L18: * **CX optimized Prompt Injection Detection**: Identifies and mitigates attempts to manipulate, exfiltrate propriet

## 星数曲线

```mermaid
xychart-beta
    title "ZenGuard-AI/fast-llm-security-guardrails 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 154 --> 156
    line [155, 155]
```

2026-10-18 155 → 2026-10-23 155（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `1e125bbf0ffb` · [字段定义](../../DATASET.md)*
