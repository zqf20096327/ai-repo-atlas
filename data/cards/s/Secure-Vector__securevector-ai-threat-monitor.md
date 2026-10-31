# Secure-Vector/securevector-ai-threat-monitor

⭐ 15 · JavaScript · NOASSERTION · 推送 2026-10-30 · [GitHub](https://github.com/Secure-Vector/securevector-ai-threat-monitor) · [官网](https://securevector.io) · 组织维护

**AI Agent 安全与可观测平台：审计每次工具调用并执行允许/阻断策略**

本地优先（Apache 2.0、无遥测）的 agent 治理工具：通过插件接入 Claude Code、Codex、Copilot CLI、OpenCode 等编码 agent，或以 SDK/proxy/MCP 方式接入 LangChain、LangChain.js、CrewAI、Ollama 等；每次模型调用与工具调用按 allow/block/log-only 策略检查并记录在 SHA-256 哈希链日志中，含 108 条威胁规则（OWASP LLM Top 10、MITRE ATT&CK 映射）与可选离线 ML 模型、成本分析、SIEM 转发。提供 pip、npm、二进制安装包与 Terraform 自托管方式。连接器 fail-open。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每次工具调用按 allow/block/log-only 策略即时判定，阻断可转为限时审批
- 108 条威胁规则覆盖 OWASP LLM Top 10 与 MITRE ATT&CK 模式，含可选离线 ML 模型
- SHA-256 哈希链日志与逐规则证据台账，本地链可显示篡改
- 可在应用内启动 Claude Code/Codex 等会话并实时查看治理面板

## 适用场景

- 对编码 agent 的每次工具调用做允许/阻断审计
- 团队评估 agent 的数据外泄与提示注入防护
- 查看 agent 会话的调用轨迹、成本与外部主机访问记录
- 将安全事件转发到 SIEM 做离机留存

## 场景标签

`网络安全` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3:  Security, Observability and Governance for AI Agents
> L104: - **Catch it.** 108 rules covering the OWASP LLM Top 10, MITRE ATT&CK-mapped patterns and agent-attack chains, plu
> L119: |**Anything that calls an OpenAI-compatible API** (Ollama, Groq, n8n, Dify, any HTTP client)|The LLM proxy: **Conn

## 星数曲线

```mermaid
xychart-beta
    title "Secure-Vector/securevector-ai-threat-monitor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4dfb019edd57` · [字段定义](../../DATASET.md)*
