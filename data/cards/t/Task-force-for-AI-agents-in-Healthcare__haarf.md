# Task-force-for-AI-agents-in-Healthcare/haarf

⭐ 24 · Python · NOASSERTION · 推送 2026-06-11 · [GitHub](https://github.com/Task-force-for-AI-agents-in-Healthcare/haarf) · [官网](https://www.medrxiv.org/content/10.64898/2026.04.09.26350519v1) · 组织维护

**医疗自主 AI agent 的监管合规框架与红队评测工具**

由 Task Force for AI Agents in Healthcare 发布的统一、生命周期导向的监管框架，将 FDA、EU AI Act、NIST AI RMF、OWASP AISVS、ISO/IEC 42001 等要求综合为 8 个验证类别、279 条要求、三级风险分级。仓库附带红队评测 harness：以 Python 运行 6 类场景（未授权工具调用、禁忌用药、提示注入等），通过 RBAC、禁忌检查、注入清洗、熔断、审计日志五层中间件执行 HAARF 条件，与 baseline 对比，输出 UTSR/CMR/PISR 等指标。支持 Gemini 与 Claude 模型，数据全部为合成数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 279 条要求、8 个验证类别、3 级风险分级的框架规范
- 红队 harness 含 6 类攻击场景与五层中间件执行（RBAC/禁忌/注入清洗/熔断/审计）
- AnthropicProvider/GeminiProvider 抽象层支持 claude-* 与 gemini-* 模型
- 对 NIST AI RMF 覆盖 88%、FDA TPLC 84%、EU AI Act 71% 的映射表

## 适用场景

- 对医疗 AI agent 做未授权工具调用与提示注入的红队评测
- 按监管要求梳理医疗 agent 的合规检查清单
- 复现 HAARF 中间件与 baseline 的对比实验

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L12: The **Task Force for AI Agents in Healthcare** presents a **unified, lifecycle-centric regulatory framework** for a
> L25: ## Quick Start: Red-Team Evaluation
> L101: The harness uses Anthropic-format messages internally. The `providers.py` module provides:

## 星数曲线

```mermaid
xychart-beta
    title "Task-force-for-AI-agents-in-Healthcare/haarf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `7c433ee774af` · [字段定义](../../DATASET.md)*
