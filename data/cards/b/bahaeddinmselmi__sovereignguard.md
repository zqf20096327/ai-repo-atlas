# bahaeddinmselmi/sovereignguard

⭐ 10 · Python · NOASSERTION · 推送 2026-03-13 · [GitHub](https://github.com/bahaeddinmselmi/sovereignguard) · [官网](https://github.com/bahaeddinmselmi/sovereignguard) · 个人维护

**给 EMEA 团队的 PII 脱敏 LLM 网关，助 GDPR 合规接入**

部署在应用与上游 LLM API 之间的隐私网关：出站请求中检测 PII（姓名/电话/证件号/IBAN 等），替换为可逆 token 并本地存储映射，上游仅收到 token 化负载，响应返回后自动还原。提供 OpenAI 兼容端点、API key 认证、限流、哈希链审计日志与熔断机制，映射后端支持内存/加密 SQLite/Redis/Vault，内置突尼斯、摩洛哥、法国本地化识别器。README 注明识别器为启发式模式，非法律替代品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可逆 token 化管线：检测→替换→转发→还原，上游不见原始 PII
- OpenAI 兼容网关（/v1/chat/completions 等）可 drop-in 接入
- 哈希链不可篡改审计日志与 fail-closed 熔断
- 多映射后端：memory/加密 SQLite/Redis/Vault KV v2

## 适用场景

- 让应用调用 OpenAI/Anthropic 时不上送客户原始 PII
- 满足欧盟数据主权要求的企业 LLM 功能落地
- 多实例部署下集中审计受监管的数据流

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: SovereignGuard is an open source AI privacy gateway that sits between your application and an external LLM provider,
> L98: - OpenAI-compatible APIs
> L229: - `POST /v1/chat/completions`

## 星数曲线

```mermaid
xychart-beta
    title "bahaeddinmselmi/sovereignguard 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-10 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `54dee1a028c7` · [字段定义](../../DATASET.md)*
