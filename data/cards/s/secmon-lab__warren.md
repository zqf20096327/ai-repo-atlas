# secmon-lab/warren

⭐ 136 · Go · Apache-2.0 · 推送 2026-07-20 · [GitHub](https://github.com/secmon-lab/warren) · 组织维护

**AI 原生安全告警管理系统：自动分诊与调查告警**

面向安全运营团队（SOC）的告警管理平台：通过 webhook、Google Pub/Sub、AWS SNS 接收 GuardDuty、SIEM、EDR 等来源的告警，经 Rego/OPA 策略管道与 LLM 完成元数据生成、多 agent 并行富化（VirusTotal、Shodan、CrowdStrike Falcon 等）与分诊定级，结果以工单形式呈现于 Slack 与 React Web UI，团队成员可在 Slack 线程中 @warren 触发 orchestrator agent 派发子 agent 调查。agent 记忆系统从每次调查中提取声明并以向量嵌入与质量分积累组织知识。基础设施绑定 GCP：Vertex AI (Gemini)、Firestore、Cloud Run，需要 GCP 项目部署。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 策略驱动的告警处理管道（Rego/OPA 转换、富化、分诊）
- Slack 多 agent 调查：orchestrator 派发 BigQuery/Falcon/Slack 子 agent 并行工作
- agent 记忆系统：从调查中提取声明、向量嵌入存储、质量分演化与剪枝
- 集成 VirusTotal/OTX/Shodan/AbuseIPDB/URLScan 等威胁情报工具与 MCP 扩展

## 适用场景

- 安全团队通过 Slack 对告警进行 AI 辅助分诊与深入调查
- 自动富化和分类海量安全告警以减少重复人工工作
- 将团队调查经验沉淀为可复用的组织知识

## 场景标签

`网络安全` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: AI-native security alert management — not just AI-assisted, but built from the ground up to let AI agents perform th
> L6: 2. **AI triage** — LLM generates a summary, queries threat intelligence for enrichment, and assigns severity
> L31: Warren operates as a **Slack-native multi-agent system**. When an alert arrives, it is posted to a Slack channel wi

## 星数曲线

```mermaid
xychart-beta
    title "secmon-lab/warren 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 134 --> 137
    line [135, 136, 136]
```

2026-10-18 135 → 2026-10-23 136（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8da601618c0e` · [字段定义](../../DATASET.md)*
