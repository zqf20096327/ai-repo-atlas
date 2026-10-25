# crucible-security/crucible

⭐ 50 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/crucible-security/crucible) · [官网](https://crucible-security.github.io/crucible-website/) · 组织维护

**面向 LLM 智能体的自动化红队与安全测试 CLI 工具**

本地运行的 Python CLI（pip 安装），对暴露 HTTP 接口的 LLM 智能体执行自动化红队扫描：内置 90+ 攻击载荷（提示注入、越狱、目标劫持、记忆投毒、MCP 安全、幻觉检测等），按扣分制输出 A–F 评分与 JSON 报告，映射 OWASP LLM/Agentic Top 10，并可生成 EU AI Act 合规报告。面向在 CI/CD 中对智能体做上线前安全测试的开发者与安全工程师。支持 OpenAI/Anthropic/Groq/Ollama 等多种目标端点。已知限制：拒绝检测依赖关键词匹配（精确率约 0.842），MCP stdio 传输仅 Linux eBPF 覆盖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 90+ 攻击载荷覆盖提示注入、越狱、目标劫持、记忆投毒、MCP 安全等模块
- 扣分制 A–F 评分与 JSON 输出，可接入 CI/CD 按阈值失败构建
- 映射 OWASP LLM Top 10 与 Agentic Top 10，自动生成 EU AI Act 合规报告
- 本地 CLI、零数据留存、可离线运行；支持 --confidence 输出 bootstrap 置信区间

## 适用场景

- 上线前对 LLM 智能体端点跑自动化红队扫描并出报告
- 把安全扫描接入 CI 流水线，发现 CRITICAL 时阻断构建
- 对 MCP 服务器与工具调用流量做安全检测
- 为合规需求生成 EU AI Act 报告

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L9:  pytest for AI agents -- test, score, and harden before production
> L40: - **Automated red-teaming** -- 90+ real attack payloads run in under 60 seconds, not weeks of manual testing
> L42: - **CI/CD native** -- `crucible scan --output json` pipes into any pipeline; fail builds on low grades

## 星数曲线

```mermaid
xychart-beta
    title "crucible-security/crucible 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-25 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `39403cd9411d` · [字段定义](../../DATASET.md)*
