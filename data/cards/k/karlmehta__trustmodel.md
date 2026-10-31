# karlmehta/trustmodel

⭐ 14 · Python · NOASSERTION · 推送 2026-08-14 · [GitHub](https://github.com/karlmehta/trustmodel) · [官网](https://trustmodel.ai) · 组织维护

**给 AI 团队的信任评估工具：10 维打分、生产监控与策略治理**

面向 AI 开发与合规团队的开源本地工具（PyPI 包 trustmodel-local，MIT），含三个产品：Eval 用 LLM-as-judge（OpenAI/Anthropic，温度 0）或启发式回退对 AI 输出在 safety/fairness/accuracy 等 10 个维度打分并汇总 0–100 TrustScore；Monitor 通过装饰器与 OpenTelemetry 自动对生产 LLM 调用打分；Govern 用 YAML 策略包（eu-ai-act、nist-ai-rmf、nyc-ll144、owasp-llm）在输出到达用户前做允许/阻断裁决。另提供 MCP server 供 Claude Code/Cursor 等 agent 调用；校准云打分需免费 API key（5 credits），本地打分用自有 key 免计量。存在独立专有云 SDK（trustmodel 包）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 维 TrustScore 评估，LLM-as-judge 或无 key 启发式回退均可运行
- 装饰器式生产监控 + OpenTelemetry 导出与自动仪表化
- 法规映射 YAML 策略包：EU AI Act / NIST AI RMF / NYC LL144 / OWASP LLM
- MCP server 将 evaluate/govern 暴露给任意 MCP 客户端

## 适用场景

- 上线前对 AI 输出做安全与合规打分
- 生产环境持续监控 LLM 响应并在低于阈值时告警
- 按法规策略包阻断违规输出（如就业歧视话术）

## 场景标签

`模型评测` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L96: Score any AI output across 10 trust dimensions and roll it into a 0–100 **TrustScore**.
> L187: Enforce policy **before** AI output reaches a user or another tool. Open-source policy packs map

## 星数曲线

```mermaid
xychart-beta
    title "karlmehta/trustmodel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `fbdb7a58c6b4` · [字段定义](../../DATASET.md)*
