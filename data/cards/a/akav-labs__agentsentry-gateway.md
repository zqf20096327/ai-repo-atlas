# akav-labs/agentsentry-gateway

⭐ 10 · Rust · Apache-2.0 · 推送 2026-07-30 · [GitHub](https://github.com/akav-labs/agentsentry-gateway) · [官网](https://akav.io) · 组织维护

**LLM Agent 的 OpenAI 兼容安全网关：出口拦截泄漏与注入**

以透明代理方式部署在 Agent 与上游 LLM API 之间的安全网关：仅改一个 BASE_URL 环境变量即可接入，扫描出站请求中的密钥/PII 泄漏、越狱、提示注入与 MITRE ATLAS 技术，违规请求阻断，正常流量原样转发。基于 Rust 实现，正则/线性检测，单请求扫描约 0.75ms；无数据库、无遥测，全部在本机运行。支持流式响应的逐 token 出站 DLP 扫描与 Prometheus 指标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 73 条 DLP 规则 + 越狱/注入检测 + 97 项 MITRE ATLAS 技术
- Unicode/同形字混淆归一化以对抗绕过
- 流式响应（SSE）逐 token 出站泄漏扫描与截断
- Docker 一键运行，Prometheus 指标与结构化日志

## 适用场景

- 为企业内 Agent 出站流量拦截 API 密钥与 PII 泄漏
- 阻止越狱与提示注入请求到达上游 LLM API
- 共享内部端点统一注入网关密钥并审计调用方

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L8: **A transparent, OpenAI-compatible security gateway for LLM agents.**
> L66:  your agent ──▶ AgentSentry Gateway ──▶ OpenAI / Anthropic / Ollama / vLLM …
> L129: This is the **single-agent gateway** — the enforcement core. The full

## 星数曲线

```mermaid
xychart-beta
    title "akav-labs/agentsentry-gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `73648a86fe16` · [字段定义](../../DATASET.md)*
