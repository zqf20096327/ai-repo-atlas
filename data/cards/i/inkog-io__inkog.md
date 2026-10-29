# inkog-io/inkog

⭐ 31 · Go · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/inkog-io/inkog) · [官网](https://inkog.io) · 组织维护

**AI agent 代码的静态安全扫描器：上线前查注入、失控循环与合规缺口**

面向 AI agent 开发与安全团队的静态分析工具，扫描 21 种框架（Python/TS/无代码）的 agent 代码，检测 token 轰炸、递归工具调用、提示注入汇聚点、缺少人工审批、跨租户泄漏与 MCP 工具投毒等 agent 特有问题；结果映射到 EU AI Act 第 14/15 条、NIST AI RMF、ISO 42001 与 OWASP LLM Top 10。可通过 Claude Code/Cursor/ChatGPT 的 MCP、CLI、npx 或 GitHub Actions 使用；扫描需 app.inkog.io 的 API key，CLI 为 Apache 2.0、引擎为专有实现。另有 Inkog Red 对运行中 agent 做对抗性探测。

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

- 静态检测 6 类 agent 特有漏洞（token 轰炸、提示注入汇聚点、MCP 工具投毒等）
- 发现按条款级映射到 EU AI Act / NIST / ISO 42001 / OWASP LLM Top 10
- 支持 21 种框架（LangChain、CrewAI、AutoGen、n8n、Dify 等）
- 提供 MCP 服务器审计、SKILL.md 包扫描与 5 档扫描策略

## 适用场景

- agent 应用上线前做安全与合规静态扫描
- 在 CI（GitHub Actions）中持续检查 agent 代码漏洞
- 审计 MCP 服务器与 Skill 包的安全性
- 生成 EU AI Act 人工监督等合规报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5:  Static analysis that catches the bugs only agent code can have — token bombing, prompt injection, missing oversight
> L32: Findings map directly to **EU AI Act Article 14 / 15**, **NIST AI RMF**, **ISO 42001**, and **OWASP LLM Top 10** — 

## 星数曲线

```mermaid
xychart-beta
    title "inkog-io/inkog 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-29 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `423fbcb91cec` · [字段定义](../../DATASET.md)*
