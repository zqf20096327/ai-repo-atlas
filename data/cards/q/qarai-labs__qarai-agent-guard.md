# qarai-labs/qarai-agent-guard

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-11 · [GitHub](https://github.com/qarai-labs/qarai-agent-guard) · [官网](https://qarai-labs.github.io/qarai-agent-guard/) · 组织维护

**构建安全 AI agent 的 Python 工具包，防注入/越狱/PII 泄露**

Python 安全工具包，在 agent 读取、存储或向工具发送数据前进行检查，内置针对提示注入、越狱尝试、PII 泄露、XML 攻击与机密检测的安全规则，开箱支持英语、阿拉伯语与法语。通过 AgentGuard、Detector 与默认策略组成防护层，并提供 LangChain 中间件与 CrewAI 生命周期钩子两个集成包，注册后自动应用于每次 LLM 调用与工具调用。以 pip 包形式分发，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置提示注入/越狱/PII/XML 攻击/机密检测规则
- 开箱支持英语、阿拉伯语与法语
- LangChain 中间件集成包
- CrewAI 生命周期钩子全局注册，自动覆盖 LLM 与工具调用

## 适用场景

- 为我的 LangChain/CrewAI agent 加装提示注入与越狱防护
- 在 agent 处理数据前拦截 PII 泄露与机密暴露
- 多语言（英/阿/法）环境下的 agent 安全加固

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L18: **Qarai Agent Guard** is a Python toolkit for building secure AI agents.
> L20: It defends against prompt injection, jailbreaks, PII leakage, and other LLM security threats.
> L22: It includes **built-in security rules** for **prompt injection, jailbreak attempts, PII leakage, XML-based attacks,

## 星数曲线

```mermaid
xychart-beta
    title "qarai-labs/qarai-agent-guard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d83670d013bd` · [字段定义](../../DATASET.md)*
