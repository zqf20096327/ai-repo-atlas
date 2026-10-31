# clay-good/mantissa-log

⭐ 14 · Python · MIT · 推送 2026-05-10 · [GitHub](https://github.com/clay-good/mantissa-log) · 个人维护

**开源云原生 SIEM：自然语言查日志、身份威胁检测与自动响应**

部署在 AWS/GCP/Azure 无服务器架构上的开源 SIEM：自然语言提问转 SQL（Athena/BigQuery/Synapse），查询前给出成本预估；支持 8 家 LLM 提供商做查询翻译与告警富化。功能含 ITDR（跨 Okta/Azure AD 等 5 个身份源的行为基线与 8 阶段攻击链追踪）、647 条 Sigma 检测规则、日志源健康监控、25+ 日志采集器与 SOAR 剧本。Terraform 部署，自称 alpha（v0.1.0），无规模化生产部署，检测为批处理（5-15 分钟延迟）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言转 SQL 的查询接口，含成本预估与会话上下文
- 647 条 Sigma 规则自动转换为云平台 SQL（49 条 ITDR 专用）
- 跨 5 个身份提供商的行为基线与风险评分（0-100）
- SOAR 剧本自动响应，危险动作需审批并有审计记录

## 适用场景

- 安全团队用自然语言查询日志而无需学习 SPL/KQL/Lucene
- 检测 Okta、Azure AD 等身份源的凭据攻击与权限提升
- 以无服务器架构替代商业 SIEM 控制日志分析成本

## 场景标签

`网络安全` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L64: - Plain English to SQL (Athena, BigQuery, or Synapse)
> L67: - 8 LLM providers: Anthropic Claude, OpenAI GPT-4, Google Gemini, AWS Bedrock, Azure OpenAI, GCP Vertex AI
> L231: - **LLM dependency**: Requires LLM API keys. Query quality depends on model capability. LLM-generated SQL may occa

## 星数曲线

```mermaid
xychart-beta
    title "clay-good/mantissa-log 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `4763a58df401` · [字段定义](../../DATASET.md)*
