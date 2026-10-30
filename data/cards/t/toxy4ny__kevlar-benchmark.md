# toxy4ny/kevlar-benchmark

⭐ 34 · Python · MIT · 推送 2026-01-20 · [GitHub](https://github.com/toxy4ny/kevlar-benchmark) · 个人维护

**面向 AI Agent 安全的红队测试框架，覆盖 OWASP ASI 十大风险**

基于 OWASP Top 10 for Agentic Applications (2026) 的红队测试工具，自动化检测、利用并报告 Agent-Specific Injection（ASI）漏洞，按 ASI01–ASI10 优先级编排。每类风险下模拟真实攻击场景（如 EchoLeak、Inception），输出兼容 OWASP AIVSS 的 JSON 结构化报告，并提供 CLI 交互/非交互模式、CI/CD 集成与退出码分级。默认 mock 模式无需真实 agent；real 模式需 LangChain 与 Ollama。仅供授权红队测试使用，采用 CC BY-SA 4.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖全部 10 项 OWASP ASI 风险并附 2025 真实事件对照
- 输出兼容 OWASP AIVSS 的结构化 JSON 报告
- 支持 mock 与 real 两种 agent 测试模式
- 提供 CI/CD 集成与基于严重度的退出码（0/1/2/130）

## 适用场景

- 对自己的 AI agent 做注入类漏洞红队测试
- 在 CI/CD 流水线中自动检测 agent 安全风险并按严重度阻断
- 以 OWASP AIVSS 格式产出安全评估报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L11: Detect, exploit, and report **Agent-Specific Injection (ASI)** vulnerabilities before adversaries do.
> L12: Kevlar automates adversarial testing of all **10 OWASP ASI risks**, ordered by real-world criticality from **Append

## 星数曲线

```mermaid
xychart-beta
    title "toxy4ny/kevlar-benchmark 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-24", "2026-10-30"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-19 33 → 2026-10-30 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4257010fc967` · [字段定义](../../DATASET.md)*
